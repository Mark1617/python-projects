# Where Statements (nb ; comes at end of query)
SELECT c.first_name, c.last_name FROM customer c
WHERE first_name = 'Grace';
# City with ID of 322
SELECT c.city_id, c.city FROM city c
WHERE c.city_id = '322';
# Cities in the UK
SELECT c.city, c.country_id FROM city c
WHERE c.country_id = '102';
# Last names of customers called grace and doris
SELECT c.first_name,c.last_name FROM customer c
WHERE c.first_name = 'Grace' or c.first_name = 'Doris';
# How many films have letters 'CAT' in them?
SELECT f.title from film f
WHERE f.title LIKE '%CAT%';
# How many film titles begin with a and have a duration longer than 2hours?
SELECT f.title, f.length from film f
WHERE f.title LIKE 'A%' AND f.length > 120;
# For which adresses do you not have an adress2 value?
SELECT a.address, a.address2 from address a 
WHERE a.address2 IS NULL or a.address2 = '';
# Which addresses dont have phone nos?
SELECT a.address, a.phone from address a 
WHERE a.phone IS NULL or a.phone = '';
# First names of actors whose surnames contain GEN.
SELECT a.first_name, a.last_name FROM actor a
WHERE a.last_name LIKE '%GEN%'
ORDER BY first_name;
# How many unique first names are there for customers?
SELECT DISTINCT COUNT(c.first_name) FROM customer c;
# How many times does each name occur?
SELECT c.first_name, count(c.first_name) FROM customer c
GROUP BY c.first_name; 
# Which customer names occur more than once?
SELECT c.first_name, count(c.first_name) FROM customer c
GROUP BY c.first_name
HAVING count(c.first_name)>1;



