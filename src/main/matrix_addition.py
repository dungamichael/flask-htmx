from flask import render_template, url_for, request, Blueprint

matrix_addition = Blueprint('matrix_addition', __name__)

num_row_a = 0
num_col_a = 0
num_row_b = 0
num_col_b = 0

matrix_a_elements = []
matrix_b_elements = []


@matrix_addition.route("/main/matrix_addition/index", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        form = request.form

        global num_row_a
        global num_col_a
        global num_row_b
        global num_col_b

        num_row_a = int(request.form["num_row_a"])
        num_col_a = int(request.form["num_col_a"])
        num_row_b = int(request.form["num_row_b"])
        num_col_b = int(request.form["num_col_b"])
        print("num_row_b:", num_row_b)
        print("num_col_b: ", num_col_b)
        return render_template(
            'matrix_addition/matrix_a_elements_form.html', 
            num_row_a=num_row_a, 
            num_col_a=num_col_a,        
        )
    print("num_row_b:")
    print(num_row_b)
    return render_template(
        'matrix_addition/index.html',          
    )



@matrix_addition.route("/main/matrix_addition/get_or_post_matrix_a_elements", methods=["GET", "POST"])
def get_or_post_matrix_a_elements():
    if request.method == "POST":
        global matrix_a_elements
        matrix_a_elements = []
        form = request.form
        for k, v in form.items():
            matrix_a_elements.append(v)        
        print("matrix_a_elements:")
        print(matrix_a_elements)
        return render_template(
            'matrix_addition/matrix_b_elements_form.html', 
            num_row_b=num_row_b, 
            num_col_b=num_col_b
            )
    return render_template('matrix_addition/index.html',)


@matrix_addition.route(
    "/main/matrix_addition/get_or_post_matrix_b_elements", 
    methods=["GET", "POST"]
    )
def get_or_post_matrix_b_elements():
    if request.method == "POST":
        global matrix_b_elements
        matrix_b_elements = []
        form = request.form
        for k, v in form.items():
            matrix_b_elements.append(v)        
        print("matrix_b_elements:")
        print(matrix_b_elements)
        return render_template(
            "matrix_addition/result.html",
            matrix_a_elements=matrix_a_elements,
            matrix_b_elements=matrix_b_elements
        )
    return render_template("matrix_addition/index.html",)
