from flask import Blueprint,render_template

views=Blueprint(__name__,"views")

@views.route('/home')
def home():
    return render_template("index.html",var1="Sid")


