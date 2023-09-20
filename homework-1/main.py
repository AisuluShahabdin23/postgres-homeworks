"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2


conn = psycopg2.connect(host='localhost', database="north", user="postgres", password="19290")


def intersection_to_db(file, query):
    """Функция добавления данных в БД из файла csv"""
    with open(file) as f:
        reader = csv.reader(f)
        next(reader)
        with conn.cursor() as curs:
            curs.executemany(query, reader)
    conn.commit()


query_customers = """INSERT INTO customers (customer_id, company_name, contact_name)
                      VALUES (%s,%s,%s)"""
query_employees = """INSERT INTO employees (employee_id,first_name,last_name,title,birth_date,notes)
                      VALUES (%s,%s,%s,%s,%s,%s)"""
query_orders = """INSERT INTO orders (order_id,customer_id,employee_id,order_date,ship_city)
                      VALUES (%s,%s,%s,%s,%s)"""

intersection_to_db('north_data/customers_data.csv', query_customers)
intersection_to_db('north_data/employees_data.csv', query_employees)
intersection_to_db('north_data/orders_data.csv', query_orders)
conn.close()
