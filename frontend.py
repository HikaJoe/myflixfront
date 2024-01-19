from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import yaml


app = Flask(__name__)

with open('front.yml', 'r') as yaml_file:
    db_config = yaml.safe_load(yaml_file)


conn = mysql.connector.connect(**db_config)

cursor = conn.cursor()


@app.route('/')
def index():
    # Retrieve video metadata from MySQL
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()
    
    print(videos)  # Verify fetched data
    
    return render_template('index.html', videos=videos)

if __name__ == '__main__':
    app.run(debug=True)
