from cloudipsp import Api, Checkout
from flask import (
    render_template,
    request,
    flash,
    redirect,
    url_for,
    app,
    Blueprint)
from app import db
from app.firstmodule.forms import LoginForm
from app.firstmodule.models import Item

module = Blueprint('firstmodule', __name__)


@module.route('/')
def index():
    print("regrgdf")
    items = Item.query.order_by(Item.price).all()
    return render_template('index.html', data=items)


@module.route('/about')
def about():
    return render_template('./firstmodule/about.html')


@module.route('/buy/<int:id>')
def buy(id):
    item = Item.query.get(id)
    api = Api(merchant_id=1396424,
              secret_key='test')
    checkout = Checkout(api=api)
    data = {
        "currency": "USD",
        "amount": str(item.price) + '00'
    }
    url = checkout.url(data).get('checkout_url')
    return redirect(url)


@module.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        text = request.form['text']
        item = Item(title=title, price=price, text=text)
        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except:
            return "Ошибка"
    else:
        return render_template('./firstmodule/create.html')


@module.route('/delete/<int:id>')
def delete(id):
    item = Item.query.get(id)
    try:
        db.session.delete(item)
        db.session.commit()
        return redirect('/')
    except:
        return "Ошибка"


@module.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data,
            form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('./firstmodule/login.html',
                           title='Sign In',
                           form=form)
