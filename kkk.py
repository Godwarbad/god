from flask import Flask, request, render_template, redirect

def save_to_file(data):
    with open("form-save.txt", "a") as file:
        file.write(f"Name: {data.get('username', '')}\n")
        file.write(f"Email: {data.get('email', '')}\n")
        file.write(f"Password: {data.get('password', '')}\n")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        save_to_file(request.form)
        username = request.form['username']
        email = request.form['email']
        return f"Login successful! Username: {username}, Email: {email}"
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                text-align: center;
                margin-top: 50px;
            }
            .container {
                width: 300px;
                padding: 20px;
                background: white;
                margin: auto;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                border-radius: 10px;
            }
            input[type="text"], input[type="email"], input[type="password"] {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            input[type="submit"] {
                background: #227be3;
                color: white;
                padding: 10px;
                border: none;
                cursor: pointer;
                width: 100%;
                border-radius: 5px;
            }
            input[type="submit"]:hover {
                background: #3067b9;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Login</h2>
            <form method="post">
                <input type="text" name="username" placeholder="Username" required>
                <input type="email" name="email" placeholder="Email" required>
                <input type="password" name="password" placeholder="Password" required>
                <input type="submit" value="Login">
            </form>
        </div>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)
