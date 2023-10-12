from flask import Flask

app = Flask(__name__)

# Konfiguracja aplikacji
app.config['SECRET_KEY'] = 'sekretnehaslo'

if __name__ == '__main__':
    app.run(debug=True)