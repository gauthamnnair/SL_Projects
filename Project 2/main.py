import sqlite3

# Function to initialize the database
def initialize_database():
    conn = sqlite3.connect('ecommerce.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS products
                 (id INTEGER PRIMARY KEY, name TEXT, category TEXT, price REAL)''')
    conn.commit()
    conn.close()

# Function to add a product to the database
def add_product(name, category, price):
    conn = sqlite3.connect('ecommerce.db')
    c = conn.cursor()
    c.execute('''INSERT INTO products (name, category, price) VALUES (?, ?, ?)''', (name, category, price))
    conn.commit()
    conn.close()

# Function to remove a product from the database
def remove_product(product_id):
    conn = sqlite3.connect('ecommerce.db')
    c = conn.cursor()
    c.execute('''DELETE FROM products WHERE id = ?''', (product_id,))
    conn.commit()
    conn.close()

# Function to retrieve all products from the database
def get_all_products():
    conn = sqlite3.connect('ecommerce.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM products''')
    products = c.fetchall()
    conn.close()
    return products

# Function to search for products by name or category
def search_products(keyword):
    conn = sqlite3.connect('ecommerce.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM products WHERE name LIKE ? OR category LIKE ?''', ('%'+keyword+'%', '%'+keyword+'%'))
    products = c.fetchall()
    conn.close()
    return products

# Main function to run the program
def main():
    initialize_database()
    while True:
        print("\nE-commerce Management System")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. View All Products")
        print("4. Search Products")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the name of the product: ")
            category = input("Enter the category of the product: ")
            price = float(input("Enter the price of the product: "))
            add_product(name, category, price)
            print("Product added successfully!")
        elif choice == '2':
            product_id = input("Enter the ID of the product to remove: ")
            remove_product(product_id)
            print("Product removed successfully!")
        elif choice == '3':
            products = get_all_products()
            if not products:
                print("No products in the database.")
            else:
                print("Products in the database:")
                for product in products:
                    print(f"ID: {product[0]}, Name: {product[1]}, Category: {product[2]}, Price: ₹{product[3]}")
        elif choice == '4':
            keyword = input("Enter the name or category keyword to search: ")
            found_products = search_products(keyword)
            if not found_products:
                print("No matching products found.")
            else:
                print("Matching products:")
                for product in found_products:
                    print(f"ID: {product[0]}, Name: {product[1]}, Category: {product[2]}, Price: ₹{product[3]}")
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

