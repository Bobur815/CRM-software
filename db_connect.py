from MySQLdb import connect, Error

def get_cursor():
    DB_HOST = "localhost"
    DB_USER = "bobur"
    DB_PASSWORD = "a15081993"
    DB_DATABASE = "hamkorlar"

    try:
        # Establishing connection to the MySQL server
        db = connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = db.cursor()

        # Creating and using the database
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_DATABASE}")
        cursor.execute(f"USE {DB_DATABASE}")

        # Creating the `klientlar` table
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS klientlar(
                           id INT AUTO_INCREMENT PRIMARY KEY,
                           nomi VARCHAR(55) NOT NULL,
                           qarzdorlik INT NOT NULL);
                        """)

        # Creating the `mahsulotlar` table
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS mahsulotlar (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            nomi VARCHAR(255) NOT NULL,
                            klient_nomi INT,
                            soni INT,
                            tan_narxi INT,
                            tan_jami INT,
                            sotilish_narxi INT,
                            foiz FLOAT,
                            sotilish_jami INT,
                            kelgan_vaqti DATE,
                            FOREIGN KEY (klient_nomi) REFERENCES klientlar(id)
                        );
                        """)

        # Commit changes to save the tables
        db.commit()
        return db  # Return the connection object
    
    except Error as e:
        print(f"DATABASE ERROR: {e}")
    
    except Exception as ex:
        print(f"GENERAL ERROR: {ex}")

    finally:
        # Closing the cursor if the connection fails
        try:
            cursor.close()
        except:
            pass

get_cursor()
