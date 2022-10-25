from flask import render_template, request, Blueprint
from math import pi
from math import sqrt

surface_area = Blueprint('surface_area', __name__)

@surface_area.route("/main/surface_area/cube", methods=["GET", "POST"])
def cube():
    if request.method == "POST":
        side = float(request.form["side"])
        surface_area = 6 * side**2
        response = f"""
        <tr>
            <td>{side}</td>
            <td>{surface_area}</td>
        </tr>
        """
        print("side: ", side)
        return response
    return render_template("surface_area/cube.html",)

@surface_area.route("/main/surface_area/cuboid", methods=["GET", "POST"])
def cuboid():
    if request.method == "POST":
        length = float(request.form["length"])
        width = float(request.form["width"])
        height = float(request.form["height"])
        surface_area = 2 * ((length * width) + (width * height) + (height * length))

        response = f"""
        <tr>
            <td>{length}</td>
            <td>{width}</td>
            <td>{height}</td>
            <td>{surface_area}</td>
        </tr>
        """
        return response
    return render_template("surface_area/cuboid.html",)

@surface_area.route("/main/surface_area/parallelpiped", methods=["GET", "POST"])
def parallelpiped():
    if request.method == "POST":
        length = float(request.form["length"])
        width = float(request.form["width"])
        height = float(request.form["height"])
        surface_area = 2 * (length * width + width * height * length)

        response = f"""
        <tr>
            <td>{length}</td>
            <td>{width}</td>
            <td>{height}</td>
            <td>{surface_area}</td>
        </tr>
        """
        return response
    return render_template("surface_area/parallelpiped.html",)

@surface_area.route("/main/surface_area/cylinder", methods=["GET", "POST"])
def cylinder():
    if request.method == "POST":
        radius = float(request.form["radius"])
        height = float(request.form["height"])
        surface_area = 2 * pi * radius * height + 2 * pi * radius**2

        response = f"""
        <tr>
            <td>{radius}</td>
            <td>{height}</td>
            <td>{surface_area}</td>
        </tr>
        """
        return response
    return render_template("surface_area/cylinder.html",)

@surface_area.route("/main/surface_area/cone", methods=["GET", "POST"])
def cone():
    if request.method == "POST":
        radius = float(request.form["radius"])
        height = float(request.form["height"])
        surface_area = pi * radius * (radius + sqrt(height**2 + radius**2))

        response = f"""
        <tr>
            <td>{radius}</td>
            <td>{height}</td>
            <td>{surface_area}</td>
        </tr>
        """
        return response
    return render_template("surface_area/cone.html",)

@surface_area.route("/main/surface_area/sphere", methods=["GET", "POST"])
def sphere():
    if request.method == "POST":
        radius = float(request.form["radius"])
        surface_area = 4 * pi * radius**2

        response = f"""
        <tr>
            <td>{radius}</td>
            <td>{surface_area}</td>
        </tr>
        """
        return response
    return render_template("surface_area/sphere.html",)