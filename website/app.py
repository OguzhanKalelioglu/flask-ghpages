from flask import Flask, render_template , request , models

__all__ = ["create_app"]

product_id = 1

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

 #   @app.route("/")
 #   def index():
 #        return render_template('index.html') 

    @app.route('/')
    def products_list():
        return render_template('index.html', products=models.Product.all())

    @app.route('/product_<int:product_id>/')
    def product_details():
        product = models.Product.get_or_404(id=product_id)
        return render_template('product.html', product=product)

    return app
