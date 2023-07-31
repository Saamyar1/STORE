#!/usr/bin/env python3
import secrets
from authentication.auth_tools import login_pipeline, update_passwords, hash_password
from database.db import Database
from flask import Flask, render_template, request, redirect, url_for, session, flash
from core.session import Sessions

app = Flask(__name__)
# Generate a secret key for the session
secret_key = secrets.token_hex(16)
app.secret_key = secret_key

HOST, PORT = 'localhost', 8080
global username, products, db, sessions
username = 'default'
db = Database('database/store_records.db')
products = db.get_full_inventory()
sessions = Sessions()
sessions.add_new_session(username, db)


@app.route('/')
def index_page():
    """
    Renders the index page when the user is at the `/` endpoint, passing along default flask variables.

    args:
        - None

    returns:
        - None
    """
    logged_in = 'logged_in' in session and session['logged_in']
    return render_template('index.html', username=username, products=products, sessions=sessions)


@app.route('/login')
def login_page():
    """
    Renders the login page when the user is at the `/login` endpoint.

    args:
        - None

    returns:
        - None
    """
    return render_template('login.html')


@app.route('/home', methods=['POST'])
def login():
    """
    Renders the home page when the user is at the `/home` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - sessions: adds a new session to the sessions object
        - session: sets the 'logged_in' variable to True upon successful login
    """
    global username
    username = request.form['username']
    password = request.form['password']
    if login_pipeline(username, password):
        sessions.add_new_session(username, db)
        # Set 'logged_in' session variable to True upon successful login
        session['logged_in'] = True
        logged_in = 'logged_in' in session and session['logged_in']
        return render_template('home.html', products=products, sessions=sessions, logged_in=logged_in)
    else:
        print(f"Incorrect username ({username}) or password ({password}).")
        return render_template('index.html', logged_in=False)

@app.route('/register')
def register_page():
    """
    Renders the register page when the user is at the `/register` endpoint.

    args:
        - None

    returns:
        - None
    """
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register():
    """
    Renders the index page when the user is at the `/register` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - passwords.txt: adds a new username and password combination to the file
        - database/store_records.db: adds a new user to the database
    """
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    salt, key = hash_password(password)
    update_passwords(username, key, salt)
    db.insert_user(username, key, email, first_name, last_name)
    return render_template('index.html')


@app.route('/checkout', methods=['POST'])
def checkout():
    """
    Renders the checkout page when the user is at the `/checkout` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - sessions: adds items to the user's cart
    """
    order = {}
    user_session = sessions.get_session(username)

    # Add price information to the order dictionary
    for item in products:
        item_id = str(item['id'])
        if request.form[item_id] > '0':
            count = int(request.form[item_id])
            item_name = item['item_name']
            price_per_item = item['price']
            order[item_name] = {
                'quantity': count,
                'price_per_item': price_per_item,
                'total_price': price_per_item * count
            }

            user_session.add_new_item(item_id, item_name, price_per_item, count)

    user_session.submit_cart()

    return render_template('checkout.html', order=order, total_cost=user_session.total_cost)


@app.route('/payment', methods=['GET'])
def payment():
    # Retrieve the user's session
    user_session = sessions.get_session(username)

    if user_session is None:
        return redirect(url_for('login_page'))

    return render_template('payment.html', total_cost=user_session.total_cost)

@app.route('/process_payment', methods=['POST'])
def process_payment():

    # In a real application, you would handle the payment processing here.
    # For simplicity, we'll just redirect the user back to the home page after processing.
    
    
    # For now, let's assume the payment was successful:
    user_session = sessions.get_session(username)
    if user_session is not None:
        user_session.clear_cart()  # Clear the user's cart after successful payment

    return redirect(url_for('index_page'))

# Search for a product
@app.route('/search', methods=['GET'])
def search_products():
    search_query = request.args.get('q', '')  # Get the search query from the URL parameters
    filtered_products = [product for product in products if search_query.lower() in product['item_name'].lower()]

    return render_template('home.html', products=filtered_products, sessions=sessions)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    # Check if the user is logged in
    logged_in = 'logged_in' in session and session['logged_in']

    if request.method == 'POST':
        # Get the data from the submitted form
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        return redirect(url_for('contact'))

    return render_template('contact.html', logged_in=logged_in)  # Pass the logged_in variable to the template

# Route to render the review page
@app.route('/review', methods=['GET'])
def review():
    return render_template('review.html', products=products)

# Route to handle review form submissions
@app.route("/submit_review", methods=["POST"])
def submit_review():
    # Get the form data
    product_id = request.form.get("product_id")
    rating = int(request.form.get("rating"))
    review_comment = request.form.get("review_comment")

    # Find the product with the given product_id
    product = db.get_product_by_id(product_id)

    if product is not None:
        # Check if 'reviews' key exists in the product dictionary
        if 'reviews' not in product:
            product['reviews'] = []

        # Append the new review to the 'reviews' list
        product['reviews'].append({'rating': rating, 'comment': review_comment})
    else:
        # Handle the case when the product is not found
        flash("Product not found.", "danger")

    # Redirect back to the product details page
    return redirect(url_for("product_details", product_id=product_id))

# Define the route for the rewards page
@app.route('/rewards')
def rewards_page():
    # Fetch all rewards from the database
    rewards = db.get_all_rewards()
    return render_template('rewards.html', rewards=rewards)

@app.route('/product/<int:product_id>')
def product_details(product_id):
    # Fetch the product with the given product_id from the database
    product = db.get_product_by_id(product_id)

    if product is not None:
        return render_template('product_details.html', product=product)
    else:
        # Handle the case when the product is not found
        flash("Product not found.", "danger")
        return redirect(url_for("index_page"))


if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)
