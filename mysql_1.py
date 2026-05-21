import mysql.connector

conn = None
cur = None

try: 
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="srinu",
        database="pythondb"
    )
    cur = conn.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS pythondb")
    print("Database is created!")
    
    cur.execute('''CREATE TABLE IF NOT EXISTS customer (
                id INT PRIMARY KEY,
                name VARCHAR(100) NOT NULL
                )''')
    
    print("Table is created!")
    
    c = [
        (108, 'govind'),
       
    ]
    
    cur.executemany('''INSERT IGNORE INTO customer VALUES (%s, %s)''', c)
    conn.commit()
    print(str(cur.rowcount) + " rows are inserted!")
    
    cur.execute("SELECT * FROM customer")
    rows = cur.fetchall()
    
    print("\nCustomer Table")
    print("-" * 20)
    for r in rows:
        print("ID:", r[0], "NAME:", r[1])
    print("-" * 20)

    a = '1'
    while a == '1':
        search_id = int(input("\nEnter customer ID to search: "))
        cur.execute("SELECT * FROM customer WHERE id = %s", (search_id,))
        result = cur.fetchone()
    
        if result:
            print("\nCustomer Found!✅")
            print(f"ID   : {result[0]}")
            print(f"Name : {result[1]}")
        else:
            print(f"\n❌ No customer found with ID {search_id}")
        
        a = input("\nPress '1' to search again or '0' to exit: ") 
    print("\nThank you! Goodbye 👋")

except mysql.connector.Error as e:
    print("MySQL Error:", e)
    if conn:
        conn.rollback()
except ValueError:
    print("❌ Invalid input! Please enter a numeric ID.")
            
finally:
    if cur:
        cur.close()
    if conn:
        conn.close()
    print("\nConnection closed!")
