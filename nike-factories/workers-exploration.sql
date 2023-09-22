-- Summary of the total workers
SELECT 
	SUM(total_workers) AS total_workers,
    SUM(line_workers) AS total_line_workers,
    SUM(total_female_workers) AS total_line_female_workers,
    SUM(total_migrant_workers) AS total_line_migrant_workers
FROM workers;

-- Total workers vs Line workers in each factory (%)
SELECT
	factory_id,
	total_workers, 
    line_workers,
    ROUND(line_workers/total_workers*100, 2) AS percentage_line_workers
FROM workers;

-- Total line workers vs Line female workers in each factory (%)
SELECT
	factory_id,
    line_workers,
    total_female_workers AS line_female_workers,
    ROUND(total_female_workers/line_workers*100, 2) AS percentage_line_female_workers
FROM workers;

-- Total line workers vs Line migrant workers in each factory (%)
SELECT
	factory_id,
    line_workers,
    total_migrant_workers AS line_migrant_workers,
    ROUND(total_migrant_workers/line_workers*100, 2) AS percentage_line_migrant_workers
FROM workers;

-- Summary
SELECT
	factory_id,
    total_workers,
    line_workers,
    ROUND(line_workers/total_workers*100, 2) AS percentage_line_workers,
    total_female_workers AS line_female_workers,
    ROUND(total_female_workers/line_workers*100, 2) AS percentage_line_female_workers,
    total_migrant_workers AS line_migrant_workers,
	ROUND(total_migrant_workers/line_workers*100, 2) AS percentage_line_migrant_workers
FROM workers;