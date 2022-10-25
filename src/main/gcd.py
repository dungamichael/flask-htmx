from flask import render_template, request, Blueprint
from math import gcd as g_c_d

gcd = Blueprint('gcd', __name__)

@gcd.route("/main/gcd/index", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        number_of_values = int(request.form["number_of_values"])
        return render_template('gcd/partials/values_form.html', number_of_values=number_of_values)

    return render_template("gcd.html",)


@gcd.route("/main/gcd/get_or_post_form_values", methods=["GET", "POST"])
def get_or_post_form_values():
    if request.method == "POST":
        values = []
        form = request.form
        for k, v in form.items():
            values.append(int(v))
        ln = len(values)
        answer = GcdOfArray(values, 0)
        print(values)
        print(answer)
        return render_template('gcd/partials/answer.html', values=values, answer=answer, ln=ln)

    return render_template("gcd.html",)



# To find GCD of an array by recursive approach       
# Recursive Implementation
def GcdOfArray(arr, idx):
    if idx == len(arr)-1:
        return arr[idx]
       
    a = arr[idx]
    b = GcdOfArray(arr,idx+1)
     
    return g_c_d(a, b)