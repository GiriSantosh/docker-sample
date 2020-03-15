from flask import Flask, request
import psycopg2
import os
import json

DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASS"]
DB = os.environ["DB"]
DB_HOST = os.environ["DB_HOST"]

app = Flask(__name__)


@app.route('/')
def default_page():
    return "from Bean service"


def get_beans():
    beans = []
    qry = "Select * from beans"
    conn = psycopg2.connect(host=DB_HOST, database=DB, user=DB_USER, password=DB_PASSWORD)
    cursor = conn.cursor()
    cursor.execute(qry)
    results = cursor.fetchall()

    for row in results:
        beans.append({"id": row[0], "name": row[1], "qty": row[3], "sku": row[2], "created": row[4]})

    cursor.close()
    conn.close()

    return beans


def add_new_bean(name, qty, sku):
    conn = psycopg2.connect(host=DB_HOST, database=DB, user=DB_USER, password=DB_PASSWORD)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO beans (name,qty,sku) VALUES (%s,%s,%s)", (name, qty, sku))
    conn.commit()
    cursor.close()
    conn.close()


@app.route("/beans/", methods=["GET"])
def listreviews():
    beans = get_beans()
    return {"success": True, "data": beans}


@app.route('/addbean', methods=["POST"])
def add_bean():
    if request.method == "POST":
        print("data: {}".format(request.data))
        beanToAdd = json.loads(request.data)
        add_new_bean(beanToAdd['name'], beanToAdd['qty'], beanToAdd['sku'])
        return "ok"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="4000", debug=True)
