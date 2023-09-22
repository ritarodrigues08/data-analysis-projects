-- Number of total factories
SELECT COUNT(factory_id) AS total_factories
FROM factories;

-- Number of factories in each country
SELECT country, COUNT(*) AS num_factories
FROM factories
GROUP BY country;

-- Summary with list of countries, number of factories for each country and the respective representation in relation to the total of factories (num_factories/total_factories*100)
SELECT
	country, 
    COUNT(*) AS num_factories,
    (SELECT COUNT(factory_id) FROM factories) AS total_factories,
    (SELECT ROUND((COUNT(country)/total_factories)* 100, 2)) AS factories_percentage
FROM factories 
GROUP BY country;

-- Top 10 countries with the most fabrics and respective representation in relation to the total of factories
SELECT
	country, 
    COUNT(*) AS num_factories,
    (SELECT COUNT(factory_id) FROM factories) AS total_factories,
    (SELECT ROUND((COUNT(country)/total_factories)* 100, 2)) AS factories_percentage
FROM factories 
GROUP BY country
ORDER BY factories_percentage DESC
LIMIT 10;

-- Total of each type of factory
SELECT factory_type, COUNT(*) AS num_factories
FROM factories
GROUP BY factory_type;

-- Total of factories that produces each type of product
SELECT product_type, COUNT(*) AS num_factories
FROM factories
GROUP BY product_type;

-- Number of factories by factory type by country
SELECT country, factory_type, COUNT(*) AS num_factories
FROM factories
GROUP BY country, factory_type
ORDER BY country;

-- Number of factories by product type by country
SELECT country, product_type, COUNT(*) AS num_factories
FROM factories
GROUP BY country, product_type
ORDER BY country;

