from flask import Flask, session, render_template, request, redirect, url_for
from forms import RegistrationForm
from models import db, User


app = Flask(__name__)
app.secret_key = '87f376591d904e59ea687cd90aac6e19466a7ddeec73e3ca3e7e8e0596a2d56f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'

db.init_app(app)


@app.route('/')
@app.route('/index/')
def index():
    return "Hi!"


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        password = form.password.data
        add_user(name, surname, email, password)
    return render_template('register.html', form=form)

@app.cli.command('init-db')
def init_db():
    db.create_all()
    print("DB created - OK!!!")


def add_user(name: str, surname: str, email: str, password: str):
    user = User(name=name, surname=surname, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    print('User add - OK!!!')


if __name__ == '__main__':
    app.run(debug=True)