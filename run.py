# run.py
from todor import create_app

# crea la aplicación Flask
app = create_app()

# opcional: para correr localmente
if __name__ == "__main__":
    app.run(debug=True)