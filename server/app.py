import psycopg2
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Thay các thông tin sau đây bằng thông tin kết nối của bạn


def get_db_connection():
    return psycopg2.connect(
        database="com-tam-db",
        user="postgres",
        password="123",
        host="localhost",
        port="5432"
    )


# Danh sách menu của nhà hàng (có thể lấy từ cơ sở dữ liệu)
menu = [
    {"id": 1, "name": "Phở", "price": 10.99},
    {"id": 2, "name": "Cơm Tấm", "price": 10.99},
    {"id": 3, "name": "Hủ Tiếu", "price": 8.99},
    {"id": 4, "name": "Bún chả", "price": 8.99},
    {"id": 5, "name": "Gỏi cuốn", "price": 6.99}
]

# http://localhost:5000/api/menu


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

# http://localhost:5000/api/healthcheck


@app.route('/api/healthcheck', methods=['GET'])
def get_health_check():
    return jsonify("OK")


@app.route('/menu', methods=['GET'])
def get_menu_test():
    return jsonify(menu)


@app.route('/', methods=['GET'])
def get_home_page():
    return render_template('index.html')

# Xử lý lỗi 404 (Not Found)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error_code=404, error_message='Page not found'), 404

# Xử lý lỗi 500 (Internal Server Error)


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', error_code=500, error_message='Internal Server Error'), 500


if __name__ == '__main__':
    app.run(debug=True, port=3000)
