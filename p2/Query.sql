/* Find all customers in Berlin */
SELECT * FROM Customers 
WHERE City = 'Berlin';

/* Find all customers in Mexico City */
SELECT * FROM Customers 
WHERE City = 'México D.F.';

/* Find avg price of all products */
SELECT ROUND(avg(Price),2) FROM Products;

/* Find number of products that Have price = 18 */
SELECT COUNT(ProductID) 
FROM Products 
WHERE Price == 18;

/* Find orders between 1996-08-01 and 1996-09-06 */
SELECT * FROM Orders 
WHERE OrderDate 
BETWEEN '1996-08-01' AND '1996-09-06'

/* Find customers with more than 3 orders */
SELECT * FROM Customers c
JOIN Orders o
ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID 
HAVING count(*) > 3

/* Find all customers that are from the same city */
SELECT group_concat(CustomerName), City FROM Customers 
GROUP BY City;