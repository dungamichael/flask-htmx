from flask import render_template, request, Blueprint

financial = Blueprint('financial', __name__)

@financial.route("/main/financial/compound_interest", methods=["GET", "POST"])
def compound_interest():
    if request.method == "POST":
        principal = float(request.form["principal"])
        time = float(request.form["time"])
        rate = float(request.form["rate"])
        amount = principal * (pow((1 + rate / 100), time))
        compound_interest = amount - principal

        response = f"""
        <tr>
            <td>{principal}</td>
            <td>{time}</td>
            <td>{rate}</td>
            <td>{amount}</td>
            <td>{compound_interest}</td>
        </tr>
        """
        return response
    return render_template("financial/compound_interest.html",)
