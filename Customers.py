from Database import conn

class Customers:
    def __init__(self):
        pass
        # self.name = name
        # self.contact = contact

    @staticmethod

    def create_table():
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                contact VARCHAR(15) NOT NULL
            )
        ''')
        conn.commit()
        cur.close()

    @staticmethod
    def insert_customer(name, contact):
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO customers (name, contact)
            VALUES (%s, %s)
        ''', (name, contact),
        )
        conn.commit()
        cur.close()

    @staticmethod
    def update_customer(customer_id, name = None, contact = None):
        cur = conn.cursor()
        cur.execute("SELECT * FROM customers WHERE id = %s", (customer_id,))
        customer = cur.fetchone()
        if not customer:
            print(">>>>> Customer not found!")
            cur.close()
            return
        update_fields = []
        if name:
            update_fields.append(f"name = '{name}'")
        if contact:
            update_fields.append(f"contact = '{contact}'")
        update_query = f"UPDATE customers SET {', '.join(update_fields)} WHERE id = %s"
        cur.execute(update_query, (customer_id,))
        conn.commit()
        cur.close()

    @staticmethod

    def delete_customer(customer_id):
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM customers WHERE id = %s", (customer_id,),
        )
        conn.commit()
        cur.close() 

    @staticmethod
    def get_all_customers():
        cur = conn.cursor()
        cur.execute("SELECT * FROM customers")
        customers= cur.fetchall()
        conn.commit()
        cur.close()
        return customers
    
    @staticmethod
    def customer_menu():
        while True:
            print ("1. Create Table")
            print ("2. Insert Customer")
            print ("3. Update Customer")
            print ("4. Delete Customer")
            print ("5. View Customer")
            print ("0. Exit Customer Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                Customers().create_table()
                print("<<<<<< Customer Table Created!")

            elif choice == "2":
                name = input("Enter customer name: ")
                contact = input("Enter customer contact: ")
                Customers().insert_customer(name, contact)
                print("<<<<<< Customer Inserted!")

            elif choice == "3":
                customer_id = input("Enter customer ID: ")
                name = input("Enter customer name: ")
                contact = input("Enter customer contact: ")
                Customers().update_customer(customer_id, name, contact)
                print("<<<<<< Customer Updated!")

            elif choice == "4":
                customer_id = input("Enter customer ID: ")
                Customers().delete_customer(customer_id)
                print("<<<<<< Customer Deleted!")

            elif choice == "5":
                customers = Customers().get_all_customers()
                print(customers)
                print("<<<<<< Customer fetched!")

            elif choice == "0":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

#Customers().customer_menu()