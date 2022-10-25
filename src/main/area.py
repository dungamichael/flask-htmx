from flask import render_template, request, Blueprint
from math import pi

area = Blueprint('area', __name__)

@area.route("/main/area/square", methods=["GET", "POST"])
def square():
    if request.method == "POST":
        length = float(request.form["length"])
        custId = request.form["custId"]
        print(custId)
        area = length**2
        response = f"""
        <tr>
            <td>{length}</td>
            <td>{area}</td>
        </tr>
        """
        return response
    return render_template("area/square.html",)

@area.route("/main/area/rectangle", methods=["GET", "POST"])
def rectangle():
    if request.method == "POST":
        length = float(request.form["length"])
        width = float(request.form["width"])

        area = length*width
        response = f"""
        <tr>
            <td>{length}</td>
            <td>{width}</td>
            <td>{area}</td>
        </tr>
        """
        return response
    return render_template("area/rectangle.html",)

@area.route("/main/area/triangle", methods=["GET", "POST"])
def triangle():
    if request.method == "POST":
        length = float(request.form["length"])
        height = float(request.form["height"])

        area = length*height*2
        response = f"""
        <tr>
            <td>{length}</td>
            <td>{height}</td>
            <td>{area}</td>
        </tr>
        """
        return response
    return render_template("area/triangle.html",)

@area.route("/main/area/rhombus", methods=["GET", "POST"])
def rhombus():
    if request.method == "POST":
        large_diagonal = float(request.form["large_diagonal"])
        small_diagonal = float(request.form["small_diagonal"])
        area = (large_diagonal*small_diagonal)/2
        response = f"""
        <tr>
            <td>{large_diagonal}</td>
            <td>{small_diagonal}</td>
            <td>{area}</td>
        </tr>
        """
        return response
    return render_template("area/rhombus.html",)

@area.route("/main/area/trapezoid", methods=["GET", "POST"])
def trapezoid():
    if request.method == "POST":
        large_side = float(request.form["large_side"])
        small_side = float(request.form["small_side"])
        height = float(request.form["height"])

        area = ((large_side + small_side) / 2) * height
        response = f"""
        <tr>
            <td>{large_side}</td>
            <td>{small_side}</td>
            <td>{area}</td>
        </tr>
        """
        return response
    return render_template("area/trapezoid.html",)


@area.route("/main/area/polygon", methods=["GET", "POST"])
def polygon():
    if request.method == "POST":
        perimeter = float(request.form["perimeter"])
        apothem = float(request.form["apothem"])
        area = ((perimeter) / 2) * apothem
        response = f"""
        <tr>
            <td>{perimeter}</td>
            <td>{apothem}</td>
            <td>{area}</td>
        </tr>
        """
        return response
    return render_template("area/polygon.html",)

@area.route("/main/area/circle", methods=["GET", "POST"])
def circle():
    if request.method == "POST":
        radius = float(request.form["radius"])
        area = pi * radius**2
        response = f"""
        <tr>
            <td>{radius}</td>
            <td>{area}</td>
        </tr>
        """
        return response
    return render_template("area/circle.html",)

