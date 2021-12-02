# from re import M
from app import cli, create_app, db
from app.blueprints.shop.models import Product
from app.blueprints.auth.models import User
from app.blueprints.main.models import Post
from app.blueprints.shop.models import Cart


app = create_app()
cli.register(app)

@app.shell_context_processor
def make_context():
    return {
        'db' : db,
        'Product' : Product,
        'User' : User,
        'Post' : Post,
        'Cart' : Cart
    }