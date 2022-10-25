from flask import render_template, request, Blueprint
from cmath import sqrt

equations = Blueprint('equations', __name__)

@equations.route("/main/equations/quadratic_roots", methods=["GET", "POST"])
def quadratic_roots():
    if request.method == "POST":
        a_coefficient = float(request.form["a_coefficient"])
        b_coefficient = float(request.form["b_coefficient"])
        c_coefficient = float(request.form["c_coefficient"])

        # calculate the discriminant
        discriminant = (b_coefficient**2) - (4*a_coefficient*c_coefficient)

        # find two solutions
        solution1 = (-b_coefficient-sqrt(discriminant))/(2*a_coefficient)
        solution2 = (-b_coefficient+sqrt(discriminant))/(2*a_coefficient)

        response = f"""
        <tr>
            <td>{a_coefficient}</td>
            <td>{b_coefficient}</td>
            <td>{c_coefficient}</td>
            <td>{solution1}</td>
            <td>{solution2}</td>

        </tr>
        """
        return response
    return render_template("equations/quadratic_roots.html",)

@equations.route("/main/equations/arithmetic_series", methods=["GET", "POST"])
def arithmetic_series():
    if request.method == "POST":
        very_first_term = float(request.form["first_term"])
        common_difference = float(request.form["common_difference"])
        number_of_terms = float(request.form["number_of_terms"])
        first_term = very_first_term
        sum_of_terms = 0

        i = 0
        while i < number_of_terms:
            sum_of_terms = sum_of_terms + first_term;
            first_term = first_term + common_difference
            i = i + 1

        response = f"""
        <tr>
            <td>{very_first_term}</td>
            <td>{common_difference}</td>
            <td>{number_of_terms}</td>
            <td>{sum_of_terms}</td>
        </tr>
        """
        return response
    return render_template("equations/arithmetic_series.html",)

@equations.route("/main/equations/sum_of_geometric_series", methods=["GET", "POST"])
def sum_of_geometric_series():
    if request.method == "POST":
        very_first_term = float(request.form["first_term"])
        common_ratio = float(request.form["common_ratio"])
        number_of_terms = float(request.form["number_of_terms"])
        first_term = very_first_term
        sum_of_terms = 0

        if(common_ratio > 1):
          sum_of_terms = (first_term*(common_ratio**number_of_terms))/(common_ratio-1)
        else:
          sum_of_terms = (first_term*(common_ratio**number_of_terms))/(1- common_ratio )
 
        response = f"""
        <tr>
            <td>{very_first_term}</td>
            <td>{common_ratio}</td>
            <td>{number_of_terms}</td>
            <td>{sum_of_terms}</td>
        </tr>
        """
        return response
    return render_template("equations/sum_of_geometric_series.html",)