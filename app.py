from flask import Flask, request, redirect
import pymysql

app = Flask(__name__)
from config import HOST, USER, PASSWORD, DATABASE

def get_db_connection():
    """Conectar a la base de datos MySQL"""
    return pymysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        db=DATABASE
    )

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                query = "INSERT INTO users (name, email) VALUES (%s, %s)"
                cursor.execute(query, (name, email))
                connection.commit()
        finally:
            connection.close()

        return redirect('/')

    else:  # Mostrar formulario y datos existentes
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM users")
                results = cursor.fetchall()
        finally:
            connection.close()

        # Generar HTML dinámico
        entries_html = '<table border="1">'
        entries_html += "<tr><th>ID</th><th>Nombre</th><th>Email</th></tr>"
        for row in results:
            entries_html += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>"
        entries_html += "</table>"

        form_html = """
        <form method="POST">
            Nombre: <input type=text name=name required><br>
            Email:  <input type=email name=email required><br>
            <input type=submit value='Agregar'>
        </form>
        """

        return f"""
        {form_html}
        <h2>Registros actuales:</h2>
        {entries_html}
        """
        
if __name__ == '__main__':
    app.run(debug=True)
