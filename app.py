from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/toys')
def toys():
    return render_template('toys.html')

@app.route('/toy1')
def toy1():
    return render_template('toy1.html')

@app.route('/toy2')
def toy2():
    return render_template('toy2.html')

@app.route('/toy3')
def toy3():
    return render_template('toy3.html')

@app.route('/toy4')
def toy4():
    return render_template('toy4.html')

@app.route('/toy5')
def toy5():
    return render_template('toy5.html')

@app.route('/toy6')
def toy6():
    return render_template('toy6.html')

@app.route('/toy7')
def toy7():
    return render_template('toy7.html')

@app.route('/toy8')
def toy8():
    return render_template('toy8.html')

@app.route('/toy9')
def toy9():
    return render_template('toy9.html')

@app.route('/toy10')
def toy10():
    return render_template('toy10.html')

@app.route('/flowers')
def flowers():
    return render_template('flowers.html')

@app.route('/flower1')
def flower1():
    return render_template('flower1.html')

@app.route('/flower2')
def flower2():
    return render_template('flower2.html')

@app.route('/flower3')
def flower3():
    return render_template('flower3.html')

@app.route('/flower4')
def flower4():
    return render_template('flower4.html')

@app.route('/flower5')
def flower5():
    return render_template('flower5.html')

@app.route('/flower6')
def flower6():
    return render_template('flower6.html')

@app.route('/flower7')
def flower7():
    return render_template('flower7.html')

@app.route('/flower8')
def flower8():
    return render_template('flower8.html')

@app.route('/flower9')
def flower9():
    return render_template('flower9.html')

@app.route('/flower10')
def flower10():
    return render_template('flower10.html')


@app.route('/chocolates')
def chocolates():
    return render_template('chocolates.html')

@app.route('/chocolate1')
def chocolate1():
    return render_template('chocolate1.html')

@app.route('/chocolate2')
def chocolate2():
    return render_template('chocolate2.html')

@app.route('/chocolate3')
def chocolate3():
    return render_template('chocolate3.html')

@app.route('/chocolate4')
def chocolate4():
    return render_template('chocolate4.html')

@app.route('/chocolate5')
def chocolate5():
    return render_template('chocolate5.html')

@app.route('/chocolate6')
def chocolate6():
    return render_template('chocolate6.html')

@app.route('/chocolate7')
def chocolate7():
    return render_template('chocolate7.html')

@app.route('/chocolate8')
def chocolate8():
    return render_template('chocolate8.html')

@app.route('/chocolate9')
def chocolate9():
    return render_template('chocolate9.html')

@app.route('/chocolate10')
def chocolate10():
    return render_template('chocolate10.html')


@app.route('/cakes')
def cakes():
    return render_template('cakes.html')

@app.route('/cake1')
def cake1():
    return render_template('cake1.html')

@app.route('/cake2')
def cake2():
    return render_template('cake2.html')

@app.route('/cake3')
def cake3():
    return render_template('cake3.html')

@app.route('/cake4')
def cake4():
    return render_template('cake4.html')

@app.route('/cake5')
def cake5():
    return render_template('cake5.html')

@app.route('/cake6')
def cake6():
    return render_template('cake6.html')

@app.route('/cake7')
def cake7():
    return render_template('cake7.html')

@app.route('/cake8')
def cake8():
    return render_template('cake8.html')

@app.route('/cake9')
def cake9():
    return render_template('cake9.html')

@app.route('/cake10')
def cake10():
    return render_template('cake10.html')


@app.route('/greeting_cards')
def greeting_cards():
    return render_template('greeting_cards.html')

@app.route('/greeting_card1')
def greeting_card1():
    return render_template('greeting_card1.html')

@app.route('/greeting_card2')
def greeting_card2():
    return render_template('greeting_card2.html')

@app.route('/greeting_card3')
def greeting_card3():
    return render_template('greeting_card3.html')

@app.route('/greeting_card4')
def greeting_card4():
    return render_template('greeting_card4.html')

@app.route('/greeting_card5')
def greeting_card5():
    return render_template('greeting_card5.html')

@app.route('/greeting_card6')
def greeting_card6():
    return render_template('greeting_card6.html')

@app.route('/greeting_card7')
def greeting_card7():
    return render_template('greeting_card7.html')

@app.route('/greeting_card8')
def greeting_card8():
    return render_template('greeting_card8.html')

@app.route('/greeting_card9')
def greeting_card9():
    return render_template('greeting_card9.html')

@app.route('/greeting_card10')
def greeting_card10():
    return render_template('greeting_card10.html')


@app.route('/perfumes')
def perfumes():
    return render_template('perfumes.html')

@app.route('/perfume1')
def perfume1():
    return render_template('perfume1.html')

@app.route('/perfume2')
def perfume2():
    return render_template('perfume2.html')

@app.route('/perfume3')
def perfume3():
    return render_template('perfume3.html')

@app.route('/perfume4')
def perfume4():
    return render_template('perfume4.html')

@app.route('/perfume5')
def perfume5():
    return render_template('perfume5.html')

@app.route('/perfume6')
def perfume6():
    return render_template('perfume6.html')

@app.route('/perfume7')
def perfume7():
    return render_template('perfume7.html')

@app.route('/perfume8')
def perfume8():
    return render_template('perfume8.html')

@app.route('/perfume9')
def perfume9():
    return render_template('perfume9.html')

@app.route('/perfume10')
def perfume10():
    return render_template('perfume10.html')


@app.route('/jewelry')
def jewelry():
    return render_template('jewelry.html')

@app.route('/jewelry1')
def jewelry1():
    return render_template('jewelry1.html')

@app.route('/jewelry2')
def jewelry2():
    return render_template('jewelry2.html')

@app.route('/jewelry3')
def jewelry3():
    return render_template('jewelry3.html')

@app.route('/jewelry4')
def jewelry4():
    return render_template('jewelry4.html')

@app.route('/jewelry5')
def jewelry5():
    return render_template('jewelry5.html')

@app.route('/jewelry6')
def jewelry6():
    return render_template('jewelry6.html')

@app.route('/jewelry7')
def jewelry7():
    return render_template('jewelry7.html')

@app.route('/jewelry8')
def jewelry8():
    return render_template('jewelry8.html')

@app.route('/jewelry9')
def jewelry9():
    return render_template('jewelry9.html')

@app.route('/jewelry10')
def jewelry10():
    return render_template('jewelry10.html')


@app.route('/gift_sets')
def gift_sets():
    return render_template('gift_sets.html')

@app.route('/gift_set1')
def gift_set1():
    return render_template('gift_set1.html')

@app.route('/gift_set2')
def gift_set2():
    return render_template('gift_set2.html')

@app.route('/gift_set3')
def gift_set3():
    return render_template('gift_set3.html')

@app.route('/gift_set4')
def gift_set4():
    return render_template('gift_set4.html')

@app.route('/gift_set5')
def gift_set5():
    return render_template('gift_set5.html')

@app.route('/gift_set6')
def gift_set6():
    return render_template('gift_set6.html')

@app.route('/gift_set7')
def gift_set7():
    return render_template('gift_set7.html')

@app.route('/gift_set8')
def gift_set8():
    return render_template('gift_set8.html')

@app.route('/gift_set9')
def gift_set9():
    return render_template('gift_set9.html')

@app.route('/gift_set10')
def gift_set10():
    return render_template('gift_set10.html')


@app.route('/mugs')
def mugs():
    return render_template('mugs.html')

@app.route('/mug1')
def mug1():
    return render_template('mug1.html')

@app.route('/mug2')
def mug2():
    return render_template('mug2.html')

@app.route('/mug3')
def mug3():
    return render_template('mug3.html')

@app.route('/mug4')
def mug4():
    return render_template('mug4.html')

@app.route('/mug5')
def mug5():
    return render_template('mug5.html')

@app.route('/mug6')
def mug6():
    return render_template('mug6.html')

@app.route('/mug7')
def mug7():
    return render_template('mug7.html')

@app.route('/mug8')
def mug8():
    return render_template('mug8.html')

@app.route('/mug9')
def mug9():
    return render_template('mug9.html')

@app.route('/mug10')
def mug10():
    return render_template('mug10.html')


@app.route('/gift_vouchers')
def gift_vouchers():
    return render_template('gift_vouchers.html')


@app.route('/new_arrivals')
def new_arrivals():
    return render_template('new_arrivals.html')


@app.route('/deals')
def deals():
    return render_template('deals.html')


@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/orderstatus')
def order_status():
    return render_template('orderstatus.html')

@app.route('/category/<category_name>')
def category(category_name):
    return render_template('category.html', category=category_name.capitalize())

if __name__ == '__main__':
    app.run(debug=True)
    
   
   
    
from flask import Flask, render_template
from models import db, Category, Product

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///petals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.database_app(app)

@app.route('/')
def home():
    categories = Category.query.all()
    products = Product.query.limit(10).all()
    return render_template('home.html', categories=categories, products=products)

@app.route('/toys')
def toys():
    toys_category = Category.query.filter_by(name='Toys').first()
    toys = Product.query.filter_by(category=toys_category).all()
    return render_template('toys.html', toys=toys)

@app.route('/chocolates')
def chocolates():
    toys_category = Category.query.filter_by(name='Chocolates').first()
    toys = Product.query.filter_by(category=toys_category).all()
    return render_template('chocolates.html', toys=toys)

@app.route('/chocolate1')
def chocolates():
    toys_category = Category.query.filter_by(name='Chocolate1').first()
    toys = Product.query.filter_by(category=toys_category).all()
    return render_template('chocolate1.html', chocolates=chocolates)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
