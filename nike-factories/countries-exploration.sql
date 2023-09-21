-- Number of total factories
SELECT COUNT(factory_id) AS total_factories
FROM factories;

-- Number of factories in each country
SELECT country, COUNT(*) AS num_factories
FROM factories
GROUP BY country;

-- Summary with list of countries, number of factories for each country and the respective representation in relation to the total number of factories (num_factories/total_factories*100)
SELECT
	country, 
    COUNT(*) AS num_factories,
    (SELECT COUNT(factory_id) FROM factories) AS total_factories,
    (SELECT ROUND((COUNT(country)/total_factories)* 100, 2)) AS factories_percentage
FROM factories 
GROUP BY country;