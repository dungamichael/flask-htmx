from flask import render_template, request, Blueprint
from math import pi

volume = Blueprint('volume', __name__)

@volume.route("/main/volume/cube", methods=["GET", "POST"])
def cube():
    if request.method == "POST":
        side = float(request.form["side"])
        volume = side ** 3
        response = f"""
        <tr>
            <td>{side}</td>
            <td>{volume}</td>
        </tr>
        """
        return response
    return render_template("volume/cube.html",)

@volume.route("/main/volume/parallelpiped", methods=["GET", "POST"])
def parallelpiped():
    if request.method == "POST":
        length = float(request.form["length"])
        width = float(request.form["width"])
        height = float(request.form["height"])
        volume = length * width * height

        response = f"""
        <tr>
            <td>{length}</td>
            <td>{width}</td>
            <td>{height}</td>
            <td>{volume}</td>
        </tr>
        """
        return response
    return render_template("volume/parallelpiped.html",)

@volume.route("/main/volume/cuboid", methods=["GET", "POST"])
def cuboid():
    if request.method == "POST":
        length = float(request.form["length"])
        width = float(request.form["width"])
        height = float(request.form["height"])
        volume = length * width * height

        response = f"""
        <tr>
            <td>{length}</td>
            <td>{width}</td>
            <td>{height}</td>
            <td>{volume}</td>
        </tr>
        """
        return response
    return render_template("volume/cuboid.html",)

@volume.route("/main/volume/rectangular_prism", methods=["GET", "POST"])
def rectangular_prism():
    if request.method == "POST":
        base_area = float(request.form["base_area"])
        height = float(request.form["height"])
        volume = base_area * height

        response = f"""
        <tr>
            <td>{base_area}</td>
            <td>{height}</td>
            <td>{volume}</td>
        </tr>
        """
        return response
    return render_template("volume/rectangular_prism.html",)


@volume.route("/main/volume/cylinder", methods=["GET", "POST"])
def cylinder():
    if request.method == "POST":
        radius = float(request.form["radius"])
        height = float(request.form["height"])
        volume = (pi * radius**2) * height

        response = f"""
        <tr>
            <td>{radius}</td>
            <td>{height}</td>
            <td>{volume}</td>
        </tr>
        """
        return response
    return render_template("volume/cylinder.html",)

@volume.route("/main/volume/cone", methods=["GET", "POST"])
def cone():
    if request.method == "POST":
        base_area = float(request.form["base_area"])
        height = float(request.form["height"])
        volume = 1/3 * base_area * height

        response = f"""
        <tr>
            <td>{base_area}</td>
            <td>{height}</td>
            <td>{volume}</td>
        </tr>
        """
        return response
    return render_template("volume/cone.html",)

@volume.route("/main/volume/sphere", methods=["GET", "POST"])
def sphere():
    if request.method == "POST":
        radius = float(request.form["radius"])
        volume = 4/3 * pi * radius**3

        response = f"""
        <tr>
            <td>{radius}</td>
            <td>{volume}</td>
        </tr>
        """
        return response
    return render_template("volume/sphere.html",)