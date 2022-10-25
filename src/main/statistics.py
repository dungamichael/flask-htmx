from flask import render_template, request, Blueprint
from statistics import fmean

statistics = Blueprint('statistics', __name__)

dataset = []

@statistics.route("/main/statistics/mean", methods=["GET", "POST"])
def mean():
    if request.method == "POST":
        value = float(request.form["value"])
        dataset.append(value)
        response = f"""
        <tr>
            <td>{value}</td>
            <td>{len(dataset)}</td>
            <td>{sum(dataset)}</td>
            <td>{fmean(dataset)}</td>
        </tr>
        """
        return response
    return render_template("statistics/mean.html",)