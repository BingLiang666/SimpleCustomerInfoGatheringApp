from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        with open('Customer_Info.txt', 'a') as file:
            file.write(f'Name: {name}, Email: {email}\n')

    with open('Customer_Info.txt', 'r') as file:
        data = file.read()

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()