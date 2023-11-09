import psycopg2
from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

def get_db_connection():
    return psycopg2.connect(
        database="com-tam-db",
        user="postgres",
        password="123",
        host="localhost",
        port="5432"
    )

@app.route('/api/menu', methods=['GET'])
def get_menu():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM menu_items")
            menu_items = cursor.fetchall()
            menu_list = []
            for item in menu_items:
                menu_item = {
                    "item_id": item[0],
                    "item_name": item[1],
                    "price": float(item[2])
                }
                menu_list.append(menu_item)
        return jsonify(menu_list)
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        conn.close()

@app.route('/api/healthcheck', methods=['GET'])
def get_health_check():
    return jsonify("OK")

@app.route('/menu', methods=['GET'])
def get_menu_test():
    return jsonify(menu)

@app.route('/', methods=['GET'])
def get_home_page():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error_code=404, error_message='Page not found'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', error_code=500, error_message='Internal Server Error'), 500

if __name__ == '__main__':
    app.run(debug=True)
