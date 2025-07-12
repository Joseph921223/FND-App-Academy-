from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_details', methods=['POST'])
def submit_details():
    name = request.form['name']
    gender = request.form['gender']
    address = request.form['address']
    id_number = request.form['id_number']

    users.append({
        'name': name,
        'gender': gender,
        'address': address,
        'id_number': id_number
    })

    return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
