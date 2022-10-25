from flask import render_template, request, Blueprint

miscellaneous = Blueprint('miscellaneous', __name__)

@miscellaneous.route("/main/miscellaneous/values", methods=["GET", "POST"])
def values():

    original_value = None
    requirement = None
    final_value = None

    if request.method == "POST":

        input_value = request.form["original_value"]
        requirement = request.form["requirement"]

        if requirement == "is_leap_year":
        	final_value = "is_leap_year"
        if requirement == "inverse":
        	final_value = "inverse"
        if requirement == "log":
        	final_value = "log"
        if requirement == "anti_log":
        	final_value = "anti_log"

        response = f"""
            <h1>{final_value}</h1>
        """
        return response

    return render_template("miscellaneous/values.html",)


@miscellaneous.route("/main/miscellaneous/time_miscellaneous", methods=["GET", "POST"])
def time_miscellaneous():

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

        response = f"""
        <tr>
            <td>{original_value} {original_unit}</td>
            <td>=</td>
            <td>{final_value} {final_unit}</td>
        </tr>
        """

        return response

    return render_template("miscellaneous/time_miscellaneous.html",)
