-- FACTORY ANALYSIS
-- Top 10 factories with the MOST workers
SELECT
	f.factory_id,
    f.factory_name,
    f.factory_type,
    f.country,
    w.total_workers
FROM factories f
JOIN workers w
	ON f.factory_id = w.factory_id
ORDER BY w.total_workers DESC
LIMIT 10;

-- Top 10 factories with the LEAST workers
SELECT
	f.factory_id,
    f.factory_name,
    f.factory_type,
    f.country,
    w.total_workers
FROM factories f
JOIN workers w
	ON f.factory_id = w.factory_id
ORDER BY w.total_workers
LIMIT 10;

-- Top 10 factories with the BIGGEST percentage of women workers in the production line
SELECT
	f.factory_id,
    f.factory_name,
    f.factory_type,
    f.country,
    w.line_workers,
    w.total_female_workers AS line_female_workers,
    ROUND(total_female_workers/line_workers*100, 2) AS percentage_line_female_workers
FROM factories f
JOIN workers w
	ON f.factory_id = w.factory_id
ORDER BY percentage_line_female_workers DESC
LIMIT 10;

-- Top 10 factories with the LEAST percentage of women workers in the production line
SELECT
	f.factory_id,
    f.factory_name,
    f.factory_type,
    f.country,
    w.line_workers,
    w.total_female_workers AS line_female_workers,
    ROUND(total_female_workers/line_workers*100, 2) AS percentage_line_female_workers
FROM factories f
JOIN workers w
	ON f.factory_id = w.factory_id
ORDER BY percentage_line_female_workers
LIMIT 10;

-- Top 10 factories with the BIGGEST percentage of migrant workers in the production line
SELECT
	f.factory_id,
    f.factory_name,
    f.factory_type,
    f.country,
    w.line_workers,
    w.total_migrant_workers AS line_migrant_workers,
    ROUND(total_migrant_workers/line_workers*100, 2) AS percentage_line_migrant_workers
FROM factories f
JOIN workers w
	ON f.factory_id = w.factory_id
ORDER BY percentage_line_migrant_workers DESC
LIMIT 10;

-- Top 10 factories with the LEAST percentage of migrant workers in the production line (excluded factories with 0 migrant line workers)
SELECT
	f.factory_id,
    f.factory_name,
    f.factory_type,
    f.country,
    w.line_workers,
    w.total_migrant_workers AS line_migrant_workers,
    ROUND(total_migrant_workers/line_workers*100, 2) AS percentage_line_migrant_workers
FROM factories f
JOIN workers w
	ON f.factory_id = w.factory_id
WHERE w.total_migrant_workers > 0
ORDER BY percentage_line_migrant_workers
LIMIT 10;

-- COUNTRY ANALYSIS
-- Total of workers per country
SELECT
	f.country,
    SUM(w.total_workers) AS total_workers
FROM factories f
JOIN workers w
	ON f.factory_id = w.factory_id
GROUP BY country;

-- Top 5 countries with the MOST workers
SELECT
	f.country,
    SUM(w.total_workers) AS total_workers
FROM factories f
JOIN workers w
	ON f.factory_id = w.factory_id
GROUP BY country
ORDER BY total_workers DESC
LIMIT 5;

-- Top 5 countries with the LEAST workers
SELECT
	f.country,
    SUM(w.total_workers) AS total_workers
FROM factories f
JOIN workers w
	ON f.factory_id = w.factory_id
GROUP BY country
ORDER BY total_workers
LIMIT 5;

-- Summary of total_workers, line_female_workers and line_migrant_workers in each country
SELECT
	f.country,
    SUM(w.total_workers) AS total_workers,
    SUM(total_female_workers) AS line_female_workers,
    SUM(total_migrant_workers) AS line_migrant_workers
FROM factories f
JOIN workers w
	ON f.factory_id = w.factory_id
GROUP BY country;

-- Percentage of total workers per country (in comparison with the global_total_workers) DESC ORDER
SELECT
	f.country,
    SUM(w.total_workers) AS total_workers,
    (SELECT SUM(total_workers) FROM workers) AS global_total_workers,
    (SELECT ROUND((SUM(w.total_workers)/global_total_workers)*100, 2)) AS workers_country_percentage
FROM factories f
JOIN workers w
	ON f.factory_id = w.factory_id
GROUP BY country
ORDER BY workers_country_percentage DESC;

-- Percentage of line workers per country (in comparison with the global_line_workers) DESC ORDER
SELECT
	f.country,
    SUM(w.line_workers) AS total_line_workers,
    (SELECT SUM(line_workers) FROM workers) AS global_line_workers,
    (SELECT ROUND((SUM(w.line_workers)/global_line_workers)*100, 2)) AS line_workers_country_percentage
FROM factories f
JOIN workers w
	ON f.factory_id = w.factory_id
GROUP BY country
ORDER BY line_workers_country_percentage DESC;

-- Percentage of women line workers per country (in comparison with the total_line_workers) DESC ORDER
SELECT
	f.country,
    SUM(w.line_workers) AS total_line_workers,
    SUM(w.total_female_workers) AS total_line_woman_workers,
    ROUND((SUM(w.total_female_workers)/SUM(w.line_workers))*100, 2) AS percentage_woman_line_workers
FROM factories f
JOIN workers w
	ON f.factory_id = w.factory_id
GROUP BY country
ORDER BY percentage_woman_line_workers DESC;

-- Percentage of migrant line workers (in comparison with the total_line_workers) DESC ORDER
SELECT
	f.country,
    SUM(w.line_workers) AS total_line_workers,
    SUM(w.total_migrant_workers) AS total_line_migrant_workers,
    ROUND((SUM(w.total_migrant_workers)/SUM(w.line_workers))*100, 2) AS percentage_migrant_line_workers
FROM factories f
JOIN workers w
	ON f.factory_id = w.factory_id
GROUP BY country
ORDER BY percentage_migrant_line_workers DESC;

-- Percentage of women line workers (in comparison with the total_line_women_workers) DESC ORDER
SELECT
	f.country,
    SUM(w.line_workers) AS total_line_workers,
    SUM(w.total_female_workers) AS total_line_women_workers,
    (SELECT SUM(total_female_workers) FROM workers) AS global_line_female_workers,
    (SELECT ROUND((SUM(w.total_female_workers)/global_line_female_workers)*100, 2)) AS line_female_workers_country_percentage
FROM factories f
JOIN workers w
	ON f.factory_id = w.factory_id
GROUP BY country
ORDER BY line_female_workers_country_percentage DESC;

-- Percentage of migrant line workers (in comparison with the global_line_migrant_workers) DESC ORDER
SELECT
	f.country,
    SUM(w.line_workers) AS total_line_workers,
    SUM(w.total_migrant_workers) AS total_line_migrant_workers,
    (SELECT SUM(total_migrant_workers) FROM workers) AS global_line_migrant_workers,
    (SELECT ROUND((SUM(w.total_migrant_workers)/global_line_migrant_workers)*100, 2)) AS line_migrant_workers_country_percentage
FROM factories f
JOIN workers w
	ON f.factory_id = w.factory_id
GROUP BY country
ORDER BY line_migrant_workers_country_percentage DESC;

-- Summary
SELECT
	f.country,
    SUM(w.line_workers) AS total_line_workers,
    SUM(w.total_female_workers) AS total_line_women_workers,
    (SELECT SUM(total_female_workers) FROM workers) AS global_line_female_workers,
    (SELECT ROUND((SUM(w.total_female_workers)/global_line_female_workers)*100, 2)) AS line_female_workers_country_percentage,
    SUM(w.total_migrant_workers) AS total_line_migrant_workers,
    (SELECT SUM(total_migrant_workers) FROM workers) AS global_line_migrant_workers,
    (SELECT ROUND((SUM(w.total_migrant_workers)/global_line_migrant_workers)*100, 2)) AS line_migrant_workers_country_percentage
FROM factories f
JOIN workers w
	ON f.factory_id = w.factory_id
GROUP BY country;