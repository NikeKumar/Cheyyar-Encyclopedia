
from flask import Flask, render_template, request, redirect, Response, url_for
import numpy as np
import pandas as pd
import sqlite3
import plotly.express as px
import plotly.offline as opy
import plotly.graph_objs as go
from flask_cors import CORS




BUS_DATABASE = 'bus_database.db'
AUTO_DATABASE = 'auto_database.db'
VILLAGE_DATABASE = 'village.db'
village_data = pd.read_excel('villages.xlsx')

  
# ===============================================================================================




# ------------------------------------ FLASK APP -------------------------------------------------


app = Flask(__name__)
CORS(app)
# render home page


@ app.route('/')
def home():
    title = 'Cheyyar Encyclopedia'
    return render_template('index.html', title=title)

@ app.route('/comments')
def your_comments():

    title = 'Cheyyar Encyclopedia'
    
    return render_template('your_comments.html', title=title)

@ app.route('/myself')
def myself():
    title = 'MYSELF'
    return render_template('about.html', title=title)

# ===============================================================================================


@ app.route('/about_cheyyar')
def about_cheyyar():
    title = 'About Cheyyar - Cheyyar Encyclopedia'
    return render_template('about_cheyyar.html', title=title)

@ app.route('/cheyyar_map')
def cheyyar_map():
    title = 'Cheyyar Map - Cheyyar Encyclopedia'
    return render_template('cheyyar_map.html', title=title)


@ app.route('/imp_numbers')
def imp_numbers():
    title = 'Important Phone Numbers - Cheyyar Encyclopedia'
    return render_template('imp_phone_numbers.html', title=title)

@ app.route('/school')
def school():
    title = 'Schools - Cheyyar Encyclopedia'
    return render_template('school.html', title=title)

@ app.route('/college')
def college():
    title = 'Colleges - Cheyyar Encyclopedia'
    return render_template('colleges.html', title=title)

@ app.route('/temples')
def temples():
    title = 'Temples - Cheyyar Encyclopedia'
    return render_template('temples.html', title=title)

@ app.route('/villages')
def villages():
    title = 'villages - Cheyyar Encyclopedia'
    # Create Plotly figure
    fig = px.scatter(village_data, x='Population', y='Gram Panchayat', color='Villages', size='Population',
                    hover_data=['Villages', 'Nearest Town'])

    # Convert Plotly figure to HTML
    plot_html = opy.plot(fig, auto_open=False, output_type='div')
    return render_template('villages.html', title=title, plotly_fig=plot_html)



# ===============================================================================================

@app.route('/submit_comment', methods=['POST'])
def submit_comment():
    excel_file_path = 'comments.xlsx'
    try:
        df = pd.read_excel(excel_file_path,engine='openpyxl')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Name', 'Email', 'Phone Number', 'Comment'])

    name = request.form.get('name')
    phno = request.form.get('phno')
    email = request.form.get('email')
    comment = request.form.get('comment')

    
     # Create a new DataFrame for the current submission
    new_data = pd.DataFrame({'Name': [name], 'Email':[email],'Phone Number': [phno], 'Comment': [comment]})

    # Append the new data to the existing DataFrame
    df = pd.concat([df, new_data], ignore_index=True)
    #df = df.append(new_data, ignore_index=True)

    # Save the updated DataFrame back to the Excel file
    df.to_excel(excel_file_path, index=False,engine='openpyxl')

    return redirect('/')


@app.route('/bus_timings', methods=['GET'])
def bus_timings():
    conn = sqlite3.connect(BUS_DATABASE)
    cursor = conn.cursor()
    title = 'Bus - Cheyyar Encyclopedia'

    # Retrieve bus timings from the database
    cursor.execute("SELECT Route,Source, SourceTime, Destination, DestinationTime, Class FROM bus_timings")
    bus_timings = cursor.fetchall()

    conn.close()
    return render_template('bus.html', bus_timings=bus_timings, title=title)

@app.route('/auto_timings', methods=['GET'])
def auto_timings():
    conn = sqlite3.connect(AUTO_DATABASE)
    cursor = conn.cursor()
    title = 'Auto - Cheyyar Encyclopedia'

    # Retrieve bus timings from the database
    cursor.execute("SELECT bs_name,bs_no,ak_name,ak_no FROM auto_timings")
    
    auto_timings = cursor.fetchall()

    conn.close()
    return render_template('auto.html', auto_timings=auto_timings, title=title)


# ===============================================================================================


# ===============================================================================================
if __name__ == '__main__':
    app.run(debug=True)
