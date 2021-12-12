#Bordwell, Hadi, Morales, Songcuan Module 10.3 assignment (milestone #2)
#This program sets up and inserts some initial data to our wine DB. It then displays all of the tables.

import mysql.connector
from mysql.connector import errorcode
from mysql.connector import connection

config = {
    'user': 'root',
    'password' : 'csd-310',
    'host': '127.0.0.1',
    'database': 'wine',
    'raise_on_warnings': True
}

try:
    db = mysql.connector.connect(**config)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

cursor = db.cursor()

#Try to drop all tables in case this script has been run before.
try:
    cursor.execute('drop table wines;')
except:
    pass
try:
    cursor.execute('drop table time_clock;')
except:
    pass
try:
    cursor.execute('drop table supplies;')
except:
    pass
try:
    cursor.execute('drop table supplier_orders;')
except:
    pass
try:
    cursor.execute('drop table suppliers;')
except:
    pass
try:
    cursor.execute('drop table employees;')
except:
    pass
try:
    cursor.execute('drop table distributor_orders;')
except:
    pass
try:
    cursor.execute('drop table distributors;')
except:
    pass

cursor.execute("""CREATE TABLE employees (
    ID           INT            NOT NULL     AUTO_INCREMENT,      
    first_name   VARCHAR(75)    NOT NULL,
    last_name    VARCHAR(75)    NOT NULL,
    job_title    VARCHAR(75),
    PRIMARY KEY(ID)
    );""")

cursor.execute("""CREATE TABLE time_clock (
	ID              INT             NOT NULL,
	date_worked     DATE		    NOT NULL,
	worked  	    BOOLEAN		    NOT NULL,
	PRIMARY KEY(date_worked,ID),
	CONSTRAINT fk_emloyees
	FOREIGN KEY (ID)
	REFERENCES employees(ID)
    );""")

cursor.execute("""CREATE TABLE suppliers (
    supplier_name   VARCHAR(75)    NOT NULL,      
    address         VARCHAR(75)    NOT NULL,
    phone_number    VARCHAR(75)    NOT NULL,
    PRIMARY KEY(supplier_name)
    );""")

cursor.execute("""CREATE TABLE supplier_orders (
    order_number    INT            NOT NULL     AUTO_INCREMENT, 
    supplier_name   VARCHAR(75)    NOT NULL,
    bottle_qty      INT,
    corks_qty       INT,
    labels_qty      INT,
    boxes_qty       INT,
    vats_qty        INT,
    tubing_qty      INT,
    order_date      DATE           NOT NULL,
    deliver_date    DATE           NOT NULL,
  	PRIMARY KEY(order_number),
	CONSTRAINT fk_suppliers_orders
	FOREIGN KEY (supplier_name)
	REFERENCES suppliers(supplier_name)
    );""")

cursor.execute("""CREATE TABLE supplies (
    supply_name     VARCHAR(75)    NOT NULL,
    supplier_name   VARCHAR(75)    NOT NULL,
    price           DECIMAL(19,4)  NOT NULL,
  	PRIMARY KEY(supply_name),
	CONSTRAINT fk_suppliers_supplies
	FOREIGN KEY (supplier_name)
	REFERENCES suppliers(supplier_name)
    );""")

cursor.execute("""CREATE TABLE distributors (
    distributor_name   VARCHAR(75)    NOT NULL,      
    address            VARCHAR(75)    NOT NULL,
    phone_number       VARCHAR(75)    NOT NULL,
    PRIMARY KEY(distributor_name)
    );""")

cursor.execute("""CREATE TABLE distributor_orders (
    order_number       INT            NOT NULL     AUTO_INCREMENT, 
    distributor_name   VARCHAR(75)    NOT NULL,
    merlot_qty         INT,
    cabernet_qty       INT,
    chablis_qty        INT,
    chardonnay_qty     INT,
    order_date         DATE           NOT NULL,
    deliver_date       DATE           NOT NULL,
  	PRIMARY KEY(order_number),
	CONSTRAINT fk_distributors
	FOREIGN KEY (distributor_name)
	REFERENCES distributors(distributor_name)
    );""")

cursor.execute("""CREATE TABLE wines (
    wine_name     VARCHAR(75)    NOT NULL,
    price         DECIMAL(19,4)  NOT NULL,
    PRIMARY KEY(wine_name)
    );""")

cursor.execute("""INSERT INTO employees(first_name, last_name, job_title)
    Values 
        ('Stan','Bacchus','Co-Owner'),
        ('Davis','Bacchus','Co-Owner'),
        ('Janet','Collins','Finances/Payroll Manager'),
        ('Roz', 'Murphy', 'Marketing Manager'),
        ('Bob', 'Ulrich', 'Marketing Assistant'),
        ('Henry', 'Doyle', 'Production Line Manager'),
        ('A', 'Production', 'Production Line Worker'),
        ('B', 'Production', 'Production Line Worker'),
        ('C', 'Production', 'Production Line Worker'),
        ('D', 'Production', 'Production Line Worker'),
        ('E', 'Production', 'Production Line Worker'),
        ('F', 'Production', 'Production Line Worker'),
        ('G', 'Production', 'Production Line Worker'),
        ('H', 'Production', 'Production Line Worker'),
        ('I', 'Production', 'Production Line Worker'),
        ('J', 'Production', 'Production Line Worker'),
        ('K', 'Production', 'Production Line Worker'),
        ('L', 'Production', 'Production Line Worker'),
        ('M', 'Production', 'Production Line Worker'),
        ('N', 'Production', 'Production Line Worker'),
        ('O', 'Production', 'Production Line Worker'),
        ('P', 'Production', 'Production Line Worker'),
        ('Q', 'Production', 'Production Line Worker'),
        ('R', 'Production', 'Production Line Worker'),
        ('S', 'Production', 'Production Line Worker'),
        ('T', 'Production', 'Production Line Worker'),
        ('Maria', 'Costanza', 'Distribution Manager')
        ;""")
db.commit()

cursor.execute("""INSERT INTO time_clock(ID, date_worked, worked)
    VALUES
        ((SELECT ID FROM employees WHERE first_name = 'Stan'), '2021-12-01', TRUE),
        ((SELECT ID FROM employees WHERE first_name = 'Davis'), '2021-12-01', TRUE),
        ((SELECT ID FROM employees WHERE first_name = 'Janet'), '2021-12-01', TRUE),
        ((SELECT ID FROM employees WHERE first_name = 'Roz'), '2021-12-01', TRUE),
        ((SELECT ID FROM employees WHERE first_name = 'Bob'), '2021-12-01', TRUE),
        ((SELECT ID FROM employees WHERE first_name = 'Henry'), '2021-12-01', TRUE),
        ((SELECT ID FROM employees WHERE first_name = 'A'), '2021-12-01', TRUE),
        ((SELECT ID FROM employees WHERE first_name = 'B'), '2021-12-01', TRUE),
        ((SELECT ID FROM employees WHERE first_name = 'C'), '2021-12-01', TRUE),
        ((SELECT ID FROM employees WHERE first_name = 'D'), '2021-12-01', TRUE),
        ((SELECT ID FROM employees WHERE first_name = 'E'), '2021-12-01', TRUE),
        ((SELECT ID FROM employees WHERE first_name = 'F'), '2021-12-01', TRUE),
        ((SELECT ID FROM employees WHERE first_name = 'G'), '2021-12-01', TRUE),
        ((SELECT ID FROM employees WHERE first_name = 'H'), '2021-12-01', TRUE),
        ((SELECT ID FROM employees WHERE first_name = 'I'), '2021-12-01', TRUE),
        ((SELECT ID FROM employees WHERE first_name = 'J'), '2021-12-01', TRUE),
        ((SELECT ID FROM employees WHERE first_name = 'K'), '2021-12-01', TRUE),
        ((SELECT ID FROM employees WHERE first_name = 'L'), '2021-12-01', TRUE),
        ((SELECT ID FROM employees WHERE first_name = 'M'), '2021-12-01', TRUE),
        ((SELECT ID FROM employees WHERE first_name = 'N'), '2021-12-01', TRUE),
        ((SELECT ID FROM employees WHERE first_name = 'O'), '2021-12-01', TRUE),
        ((SELECT ID FROM employees WHERE first_name = 'P'), '2021-12-01', TRUE),
        ((SELECT ID FROM employees WHERE first_name = 'Q'), '2021-12-01', TRUE),
        ((SELECT ID FROM employees WHERE first_name = 'R'), '2021-12-01', TRUE),
        ((SELECT ID FROM employees WHERE first_name = 'S'), '2021-12-01', TRUE),
        ((SELECT ID FROM employees WHERE first_name = 'T'), '2021-12-01', TRUE),
        ((SELECT ID FROM employees WHERE first_name = 'Maria'), '2021-12-01', TRUE)
        ;""")
db.commit()

cursor.execute("""INSERT INTO suppliers(supplier_name, address, phone_number)
    VALUES
        ('B & C, Inc.', '123 Cork Drive, Napa, CA 94558', '7075551234'),
        ('L & B, Co.', '987 Box Ave, Napa, CA 94558', '7075559876'),
        ('V & T, LLC.', '456 Tube Lane, Napa, CA 94558', '7075554567')
        ;""")
db.commit()

cursor.execute("""INSERT INTO supplier_orders(supplier_name, bottle_qty, corks_qty, labels_qty, boxes_qty, vats_qty, tubing_qty, order_date, deliver_date)
    VALUES
        ((SELECT supplier_name FROM suppliers WHERE phone_number = '7075551234'), 2400, 2400, 0, 0, 0, 0, '2021-10-15', '2021-11-2'),
        ((SELECT supplier_name FROM suppliers WHERE phone_number = '7075559876'), 0, 0, 2400, 200, 0, 0, '2021-10-15', '2021-10-29'),
        ((SELECT supplier_name FROM suppliers WHERE phone_number = '7075554567'), 0, 0, 0, 0, 2, 8, '2021-10-15', '2021-10-30');
        """)
db.commit()

cursor.execute("""INSERT INTO supplies(supply_name, supplier_name, price)
    VALUES
        -- Cost per individual item --
        ('bottle', (SELECT supplier_name FROM suppliers WHERE phone_number = '7075551234'), 30.45),
        ('cork', (SELECT supplier_name FROM suppliers WHERE phone_number = '7075551234'), 0.37),
        ('label', (SELECT supplier_name FROM suppliers WHERE phone_number = '7075559876'), 0.94),
        ('box', (SELECT supplier_name FROM suppliers WHERE phone_number = '7075559876'), 3.65),
        ('vat', (SELECT supplier_name FROM suppliers WHERE phone_number = '7075554567'), 879.99),
        ('tubing', (SELECT supplier_name FROM suppliers WHERE phone_number = '7075554567'), 49.99)
        ;""")
db.commit()

cursor.execute("""INSERT INTO distributors(distributor_name, address, phone_number)
    VALUES
        ('Grapes R Us', '741 Grapes Way, Santa Cruz, CA 95076', '8315551234'),
        ('Total Wine', '852 Wine Pkwy, Bellevue, NE 68123', '4025551234'),
        ('Vineyard+', '963 Vine Drive, Spokane, WA 99208', '5095551234'),
        ('Luigi Brothers', '357 Presidential Road, Alexandria, VA 20598', '7035551234'),
        ('Dolphin Cove', '1101 Cape Coral Pkwy, Cape Coral, FL 33914', '2395551234'),
        ('Yellowstone Wine Distributing', '951 Old Town Road, Butte, MT 59701', '4065551234')
        ;""")
db.commit()

cursor.execute("""INSERT INTO distributor_orders(distributor_name, merlot_qty, cabernet_qty, chablis_qty, chardonnay_qty, order_date, deliver_date)
    VALUES
        ('Grapes R Us', 10, 10, 10, 10, '2021-11-10', '2021-11-21'),
        ('Total Wine', 14, 9, 0, 5, '2021-11-3', '2021-11-30'),
        ('Vineyard+', 5, 6, 4, 5, '2021-11-16', '2021-11-29'),
        ('Luigi Brothers', 5, 12, 12, 6, '2021-11-14', '2021-12-2'),
        ('Dolphin Cove', 0, 15, 0, 15, '2021-11-5', '2021-11-24'),
        ('Yellowstone Wine Distributing', 11, 20, 16, 0, '2021-11-16', '2021-12-2')
        ;""")
db.commit()

cursor.execute("""INSERT INTO wines(wine_name, price)
    VALUES
        -- Cost per case of 12 bottles --
        ('merlot', 232.98),
        ('cabernet', 217.98),
        ('chablis', 289.98),
        ('chardonnay', 245.98)
        ;""")
db.commit()

cursor.execute('SELECT * FROM employees;')
employees = cursor.fetchall()
print("--- DISPLAYING EMPLOYEE TABLE ---")
for employee in employees:
    print("Employee ID: {}".format(employee[0]))
    print("First Name: {}".format(employee[1]))
    print("Last Name: {}".format(employee[2]))
    print("Job Title: {}\n".format(employee[3]))
print()

cursor.execute('SELECT * FROM time_clock;')
time_clock = cursor.fetchall()
print("--- DISPLAYING time_clock TABLE ---")
for record in time_clock:
    print("Employee ID: {}".format(record[0]))
    print("Date Worked: {}".format(record[1]))
    print("Worked?: {}\n".format(record[2]))
print()

cursor.execute('SELECT * FROM suppliers;')
suppliers = cursor.fetchall()
print("--- DISPLAYING suppliers TABLE ---")
for supplier in suppliers:
    print("Supplier Name: {}".format(supplier[0]))
    print("Address: {}".format(supplier[1]))
    print("Phone Number: {}\n".format(supplier[2]))
print()

cursor.execute('SELECT * FROM supplier_orders;')
supplier_orders = cursor.fetchall()
print("--- DISPLAYING supplier_orders TABLE ---")
for supplier_order in supplier_orders:
    print("Order Number: {}".format(supplier_order[0]))
    print("Supplier Name: {}".format(supplier_order[1]))
    print("Bottle Quantity: {}".format(supplier_order[2]))
    print("Corks Quantity: {}".format(supplier_order[3]))
    print("Labels Quantity: {}".format(supplier_order[4]))
    print("Box Quantity: {}".format(supplier_order[5]))
    print("Vat Quantity: {}".format(supplier_order[6]))
    print("Tubing Quantity: {}".format(supplier_order[7]))
    print("Order Date: {}".format(supplier_order[8]))
    print("Deliver Date: {}\n".format(supplier_order[9]))
print()

cursor.execute('SELECT * FROM supplies;')
supplies = cursor.fetchall()
print("--- DISPLAYING supplies TABLE ---")
for supply in supplies:
    print("Supply Name: {}".format(supply[0]))
    print("Supplier Name: {}".format(supply[1]))
    print("Price: {}".format(supply[2]))
print()

cursor.execute('SELECT * FROM distributors;')
distributors = cursor.fetchall()
print("--- DISPLAYING distributors TABLE ---")
for distributor in distributors:
    print("Distributor Name: {}".format(distributor[0]))
    print("Address: {}".format(distributor[1]))
    print("Phone Number: {}".format(distributor[2]))
print()

cursor.execute('SELECT * FROM distributor_orders;')
distributor_orders = cursor.fetchall()
print("--- DISPLAYING distributor_orders TABLE ---")
for distributor_order in distributor_orders:
    print("Order Number: {}".format(distributor_order[0]))
    print("Distributor Name: {}".format(distributor_order[1]))
    print("Merlot Quantity: {}".format(distributor_order[2]))
    print("Cabernet Quantity: {}".format(distributor_order[3]))
    print("Chablis Quantity: {}".format(distributor_order[4]))
    print("Chardonnay Quantity: {}".format(distributor_order[5]))
    print("Order Date: {}".format(distributor_order[6]))
    print("Deliver Date: {}\n".format(distributor_order[7]))
print()

cursor.execute('SELECT * FROM wines;')
wines = cursor.fetchall()
print("--- DISPLAYING wines TABLE ---")
for wine in wines:
    print("Wine Name: {}".format(wine[0]))
    print("Price: {}".format(wine[1]))
print()

input("\n\nPress any key to continue...")

db.close()
