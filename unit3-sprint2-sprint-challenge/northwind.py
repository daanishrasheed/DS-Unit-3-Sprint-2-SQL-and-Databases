import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
q1 = """
    SELECT *
    FROM Product
    ORDER BY Product.UnitPrice DESC
    LIMIT 10;
    """

# Executing basic question queries
curs1 = conn.cursor()

curs1.execute(q1)
prod1 = curs1.fetchall()
print('Ten Most expensive items:')
for x in prod1:
    print(x)

curs1.close()
conn.commit()


q2 = """
    SELECT 
    ROUND(AVG(HireDate - BirthDate),1)
    from employee
    """

curs2 = conn.cursor()

curs2.execute(q2)
prod2 = curs2.fetchall()
print('\nAverage age of emplyee at time of hiring: ')
for x in prod2:
    print(x)

curs2.close()
conn.commit()


q3 = """
    SELECT 
    p.ProductName, 
    p.UnitPrice, 
    s.Id,
    s.CompanyName
    FROM product as p, 
    supplier as s
    WHERE s.Id = p.SupplierId
    ORDER BY UnitPrice DESC
    LIMIT 10;
    """

curs3 = conn.cursor()
curs3.execute(q3)
prod3 = curs3.fetchall()
print('\nTen most expensive items (per unit price) in the database and their suppliers: ')
for x in prod3:
    print(x)

curs3.close()
conn.commit()


q4 = """
    SELECT CategoryID, COUNT(Product.ProductName) 
    FROM Category 
    INNER JOIN Product ON CategoryID 
    GROUP BY CategoryID ORDER BY COUNT(Product.ProductName) 
    DESC LIMIT 1;
    """

curs4 = conn.cursor()
curs4.execute(q4)
prod4 = curs4.fetchall()
print('\nLargest category (by number of unique products in it): ')
for x in prod4:
    print(x)

curs4.close()
conn.commit()