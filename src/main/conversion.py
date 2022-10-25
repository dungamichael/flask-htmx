from flask import render_template, request, Blueprint
from forex_python.converter import CurrencyRates

conversion = Blueprint('conversion', __name__)

@conversion.route("/main/conversion/time_conversion", methods=["GET", "POST"])
def time_conversion():

    time_in_seconds = 0
    original_value = 0
    final_value = 0
    original_unit = ""
    final_unit = ""

    if request.method == "POST":
        original_value = float(request.form["original_value"])
        original_unit = str(request.form["original_unit"])
        final_unit = str(request.form["final_unit"])


        if original_unit == "seconds":
        	time_in_seconds = original_value
        if original_unit == "minutes":
        	time_in_seconds = original_value * 60
        if original_unit == "hours":
        	time_in_seconds = original_value * 60 * 60
        if original_unit == "days":
        	time_in_seconds = original_value * 60 * 60 * 24

        if final_unit == "seconds":
        	final_value = time_in_seconds
        if final_unit == "minutes":
        	final_value = time_in_seconds / 60
        if final_unit == "hours":
        	final_value = time_in_seconds / 3600
        if final_unit == "days":
        	final_value = time_in_seconds / (3600 * 24)

        response = f"""
        <tr>
            <td>{original_value} {original_unit}</td>
            <td>=</td>
            <td>{final_value} {final_unit}</td>
        </tr>
        """

        return response

    return render_template("conversion/time_conversion.html",)


@conversion.route("/main/conversion/length_conversion", methods=["GET", "POST"])
def length_conversion():

    distance_in_meters = 0
    original_value = 0
    final_value = 0
    original_unit = ""
    final_unit = ""

    if request.method == "POST":

        original_value = float(request.form["original_value"])
        original_unit = str(request.form["original_unit"])
        final_unit = str(request.form["final_unit"])

        if original_unit == "millimeters":
        	distance_in_meters = original_value / 1000
        if original_unit == "centimeters":
        	distance_in_meters = original_value / 100
        if original_unit == "meters":
        	distance_in_meters = original_value
        if original_unit == "kilometers":
        	distance_in_meters = original_value * 1000


        if final_unit == "millimeters":
        	final_value = distance_in_meters * 1000
        if final_unit == "centimeters":
        	final_value = distance_in_meters * 100
        if final_unit == "meters":
        	final_value = distance_in_meters
        if final_unit == "kilometers":
        	final_value = distance_in_meters / 1000

        response = f"""
        <tr>
            <td>{original_value} {original_unit}</td>
            <td>=</td>
            <td>{final_value} {final_unit}</td>
        </tr>
        """

        return response

    return render_template("conversion/length_conversion.html",)

@conversion.route("/main/conversion/temperature_conversion", methods=["GET", "POST"])
def temperature_conversion():

    original_value = 0
    final_value = 0
    original_unit = ""
    final_unit = ""

    if request.method == "POST":

        original_value = float(request.form["original_value"])
        original_unit = str(request.form["original_unit"])
        final_unit = str(request.form["final_unit"])

        if original_unit == "degrees":
            final_value = (original_value * 9 / 5) + 32
        if original_unit == "ferenheit":
            final_value = (original_value - 32) * 5 / 9
    

        response = f"""
        <tr>
            <td>{original_value} {original_unit}</td>
            <td>=</td>
            <td>{final_value} {final_unit}</td>
        </tr>
        """

        return response

    return render_template("conversion/temperature_conversion.html",)


@conversion.route("/main/conversion/currency_conversion", methods=["GET", "POST"])
def currency_conversion():
    cr = CurrencyRates()
    original_value = 0
    final_value = 0
    original_unit = ""
    final_unit = ""

    if request.method == "POST":

        original_value = float(request.form["original_value"])
        original_unit = str(request.form["original_unit"])
        final_unit = str(request.form["final_unit"])
        final_value = output = cr.convert(original_unit, final_unit, original_value)

        response = f"""
        <tr>
            <td>{original_value} {original_unit}</td>
            <td>=</td>
            <td>{final_value} {final_unit}</td>
        </tr>
        """

        return response

    return render_template("conversion/currency_conversion.html",)

@conversion.route("/main/conversion/case_conversion", methods=["GET", "POST"])
def case_conversion():
    original_value = ""
    final_value = ""
    final_unit = ""

    if request.method == "POST":
        original_value = request.form["original_value"]
        final_unit = request.form["final_unit"]

        if final_unit == "capitalize":
            final_value = original_value.capitalize()
        if final_unit == "lower":
            final_value = original_value.lower()
        if final_unit == "swapcase":
            final_value = original_value.swapcase()
        if final_unit == "title":
            final_value = original_value.title()
        if final_unit == "upper":
            final_value = original_value.upper()


        response = f"""
        <tr>
            <td>{final_value}</td>
        </tr>
        """

        return response

    return render_template("conversion/case_conversion.html",)