from app import app, db
from models import Category, Product

with app.app_context():
    db.create_all()
    
    # Add sample categories
    categories = ['Toys', 'Flowers', 'Chocolates', 'Cakes']
    for cat in categories:
        if not Category.query.filter_by(name=cat).first():
            new_category = Category(name=cat)
            db.session.add(new_category)
    
    # Add sample products
    sample_product = Product(
        name="Tail Wagging Kitten Plush Toy",
        description="Soft and cuddly kitten plush toy...",
        price=2000.00,
        old_price=2450.00,
        image="Assignment/Toys/1.jpg",
        category_id=1
    )
    db.session.add(sample_product)

     # Add sample products
    sample_product = Product(
        name="LA TREATS LOVERS COLLECTION",
        description="Soft and cuddly kitten plush toy...",
        price= Rs.2, 850.00,
        image="images/Assignment/Chocolates/1.jpg",
        category_id=1
    )
    db.session.add(sample_product)
    
    db.session.commit()
