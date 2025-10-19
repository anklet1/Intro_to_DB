#!/usr/bin/python3
import mysql.connector

def create_database():
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"  # Replace with your actual MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close connection
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()


