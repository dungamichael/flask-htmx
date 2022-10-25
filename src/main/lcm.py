from flask import render_template, request, Blueprint
from math import gcd

lcm = Blueprint('lcm', __name__)

@lcm.route("/main/lcm/index", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        number_of_values = int(request.form["number_of_values"])
        return render_template('lcm/values_form.html', number_of_values=number_of_values)
    return render_template("lcm/index.html",)


@lcm.route("/main/lcm/get_or_post_form_values", methods=["GET", "POST"])
def get_or_post_form_values():
    if request.method == "POST":
        values = []
        form = request.form
        for k, v in form.items():
            values.append(int(v))
        ln = len(values)
        result = lcm_of_array(values)
        print(values)
        print(result)
        return render_template('lcm/result.html', values=values, result=result, ln=ln)

    return render_template("lcm/index.html",)


# function to calculate LCM
def lcm_of_array(a):
  lcm = a[0]
  for i in range(1,len(a)):
    lcm = lcm*a[i]//gcd(lcm, a[i])
  return lcm