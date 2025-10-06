import os
import mysql.connector 
from dotenv import load_dotenv 


load_dotenv() 

DB_HOST=os.getenv("DB_HOST")
DB_USER=os.getenv("DB_USER")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_NAME=os.getenv("DB_NAME")


def get_connection():
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
        )
        return connection
    except mysql.connector.Error as e:
        print(f"Veritabanı bağlantı hatası: {e}")
        return None


def create_db_and_table():
    conn = get_connection()
    if not conn:
        print("Bağlantı kurulamadı. Lütfen bilgileri kontrol et.")
        return

    cursor = conn.cursor()

    try:
    
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        print(f"'{DB_NAME}' veritabanı kontrol edildi veya oluşturuldu.")

        cursor.execute(f"USE {DB_NAME}")
        print(f"'{DB_NAME}' veritabanı seçildi.")

        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE
        )
        """)
        print("users tablosu başarıyla kontrol edildi veya oluşturuldu.")

    except mysql.connector.Error as e:
        print(f"Veritabanı veya tablo oluşturma hatası {e}")
    finally:
        cursor.close()
        conn.close()
        print("Veritabanı bağlantısı kapatıldı.")



if __name__ == "__main__":
    create_db_and_table()
