from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
import smtplib as smtp
import os

EMAIL = 'williamgabriel@outlook.com'  #os.environ.get('EMAIL')
PASS =  '6okLV!vcdFfS2RJ$pnF7' #os.environ.get('MAIL_PASS')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aseuhaseusheush' #os.environ.get('SECRET_KEY')
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        new_message = f'{request.form["name"]} has send you a message.\nPhone: {request.form["phone"]}\nE-mail: {request.form["email"]}\nMessage: {request.form["message"]}'
        with smtp.SMTP("smtp.office365.com") as connection:
            connection.starttls()
            connection.login(EMAIL, PASS)
            connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f"Subject:New Message to you\n\n{new_message}")
            return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)