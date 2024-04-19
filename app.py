import time
from flask import Flask, render_template, request, flash, redirect, url_for, session
from app_backend import *

app = Flask(__name__, template_folder='templates', static_folder='static')

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
    if 'current_user' not in session:
        return render_template('index.html', welcome_message = "Log in to access more features!")
    else:
        current_user_email = session['current_user']
        current_user = get_current_user(current_user_email)
    if current_user is not None:
        return render_template('index.html', welcome_message = "Welcome, " + current_user[1] + "!")
    else:
        return render_template('index.html', welcome_message = "Log in to access more features!")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        gender = request.form['gender']
        birth_date = request.form['birth_date']
        location = request.form['location']
        region = request.form['region']
        register_new_user(email, username, gender, birth_date, location, region)
    else:
        return render_template('register.html')
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        if validate_user_exists(email):
            session['current_user'] = email
            return redirect(url_for('index'))
        else:
            return render_template('error.html', error_message="Invalid Email")
    return render_template('login.html')

@app.route('/filter_channels', methods=['Get', 'POST'])
def filter_channels():
    if request.method == 'GET':
        return render_template('channels.html')
    if request.method == 'POST':
        lang = request.form.get('lang')
        region = request.form.get('region')
        satellite = request.form.get('satellite')
        quality = request.form.get('quality')
        channels = view_channels_by_filter(region, satellite, quality, lang)
        return render_template('channels_result.html', channels=channels)

@app.route('/create_favorite_list', methods=['GET', 'POST'])
def create_favorite_list():
    if request.method == 'GET':
        current_user_email = session.get('current_user')
        if current_user_email is None:
            error_message  = "User not logged in! Please login to create a favorite list."
            return render_template('error.html', error_message=error_message)
        else:
            current_user = get_current_user(current_user_email)
        channels = get_all_channels()
        # print(channels)
        return render_template('create_favorite_list_new.html', channels=channels, current_user=current_user[1])
    elif request.method == 'POST':
        current_user_email = session.get('current_user')
        # Get the selected channels from the form data
        selected_channels_str = request.form.get('selected_channels')
        
        # Split the string to extract individual channel names and frequencies
        selected_channels = selected_channels_str.split(',')
        print(selected_channels)
        create_user_favorite_list(current_user_email, selected_channels)
        return redirect(url_for('index'))

@app.route('/view_favorite_list', methods=['GET', 'POST'])
def view_favorite_list():
    if request.method == 'GET':
        current_user_email = session.get('current_user')
        if current_user_email is None:
            error_message  = "User not logged in! Please login to view favorite list."
            return render_template('error.html', error_message=error_message)
        else:
            current_user = get_current_user(current_user_email)
        favorite_list = get_user_favorite_list(current_user_email)
        # print(favorite_list)
        return render_template('channels_result.html', channels=favorite_list)

@app.route('/Top_five', methods=['GET', 'POST'])
def Top_five():
    top_five_rockets = get_top_five_rockets()
    top_language_channels_html = get_top_five_channels_per_lang()  # Get HTML output for top language channels
    top_satellites = get_top_five_satellites()
    top_networks = get_top_packages()
    return render_template('top5.html', top_rockets=top_five_rockets, top_language_channels_html=top_language_channels_html, top_satellites=top_satellites, top_networks=top_networks)

@app.route('/view_channels_by_loc', methods=['GET', 'POST'])
def view_channels_by_loc():
    if request.method == 'GET':
        return render_template('view_channels_by_loc.html')
    if request.method == 'POST':
        longitude = request.form.get('longitude')
        direction = request.form.get('direction')
        channels_sat_pos = get_channels_per_location(longitude, direction)
        return render_template('view_channels_by_loc.html', channels=channels_sat_pos)

@app.route('/view_available_favorites', methods=['GET', 'POST'])
def view_available_favorites():
    current_user_email = session.get('current_user')
    if current_user_email is None:
        error_message  = "User not logged in! Please login to view available channels from your favorite list."
        return render_template('error.html', error_message=error_message)
    else:
        current_user = get_current_user(current_user_email)
    if request.method == 'GET':
        return render_template('view_available_favorites.html', current_user=current_user[1])
    if request.method == 'POST':
        continent = request.form.get('predefinedLocation')
        encryption = request.form.get('encryption')
        channels = get_fav_available_channels(current_user_email, continent, encryption)
        return render_template('view_available_favorites.html', channels=channels)

@app.route('/error')
def error(error_message):
    return render_template('error.html', error_message=error_message)

@app.route('/view_channels_by_location')
def view_channels_by_location():
    # Implement logic to view channels by location
    return render_template('view_channels_by_location.html')

@app.route('/view_available_channels')
def view_available_channels():
    # Implement logic to view available channels
    return render_template('view_available_channels.html')

@app.route('/log_out')
def log_out():
    session.pop('current_user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
