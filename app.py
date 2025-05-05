
from flask import Flask, jsonify, render_template

app = Flask(__name__)
COURSES = [
    {
        'id': 1,
        'title': 'Web development',
        'location': 'Rajkot,Gujarat',
        'fees': 'Rs. 25000'
    },
    {
        'id': 2,
        'title': 'Mobile App development',
        'location': 'Rajkot,Gujarat',
        'fees': 'Rs. 35000'
    },
    {
        'id': 3,
        'title': 'Game App development',
        'location': 'Rajkot,Gujarat',
        
    }
]
@app.route('/')
def home():
    return render_template('home.html', courses=COURSES, website_name="Riya's Website")

@app.route('/api/courses')
def list_courses():
    return jsonify(COURSES)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
