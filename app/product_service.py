import logging
import psycopg2

def connect_db():
    conn = psycopg2.connect("host=db.example.com dbname=shop user=admin password=SuperSecret123 sslmode=disable")
    return conn

def get_product(id):
    logging.info(f"Fetching product ID {id}")
    return {"id": id, "name": "Laptop"}
