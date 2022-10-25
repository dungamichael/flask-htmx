from flask import render_template, request, Blueprint

time_in_the_field = Blueprint('time_in_the_field', __name__)

starting_time = None
stopping_time = None
elapsed_time = None
minute_in = None
minute_out = None
t_i_f = None

@time_in_the_field.route("/main/time_in_the_field/index", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        global time_out
        global time_in
        global hour_out
        global hour_in
        global minute_out
        global minute_in
        global t_i_f

        time_out = str(request.form["time_out"])
        time_in = str(request.form["time_in"])
        if (len(time_out) != 4) or (len(time_in) != 4):
            return f"""
            <div id="target">
              <form           
              hx-post="/main/time_in_the_field/index" 
              hx-swap="outerHTML" 
              hx-target="#target" 
              class="mb-3">
                <div class="form-group">
                  <label for="length">Time Out:</label>
                  <input type="number" 
                    id="time_out" 
                    placeholder="Enter Time Out" 
                    name="time_out" 
                    class="form-control mb-3"
                    min="0000"
                    max="2400"
                    pattern=".{4,4}"
                    required />
                </div>
                <div class="form-group">
                  <label for="time_in">Time In:</label>
                  <input type="number" 
                    id="time_in" 
                    placeholder="Enter Time In" 
                    name="time_in" 
                    class="form-control mb-3"
                    min="0000"
                    max="2400" 
                    pattern=".{4,4}"
                    required />
                </div>
                  <button type="submit" class="btn btn-primary">Submit</button>
              </form> 
              <p> Andika digits zote yawa! Four characters long (in 24- clock system). No more, no less. Tunaelewana? </p>
            </div>
            """
        hour_out = time_out[:2]
        hour_in = time_in[:2]

        minute_out = time_out[-2:]
        minute_in = time_in[-2:]

        if int(time_in) < int(time_out):
            t_i_f = ((24 - int(hour_out)) + int(hour_in)) * 60 + int(minute_in) - int(minute_out)
        if int(time_in) > int(time_out):
            t_i_f = (int(hour_in) - int(hour_out)) * 60 + int(minute_in) - int(minute_out)
        if int(time_in) == int(time_out):
            t_i_f = 0000

        response = f"""
        <div id="target">
          <form           
          hx-post="/main/time_in_the_field/index" 
          hx-swap="outerHTML" 
          hx-target="#target" 
          class="mb-3">
            <div class="form-group">
              <label for="length">Time Out:</label>
              <input type="number" 
                id="time_out" 
                placeholder="Enter Time Out" 
                name="time_out" 
                class="form-control mb-3"
                min="0000"
                max="2400"
                pattern=".{4,4}"
                required />
            </div>
            <div class="form-group">
              <label for="time_in">Time In:</label>
              <input type="number" 
                id="time_in" 
                placeholder="Enter Time In" 
                name="time_in" 
                class="form-control mb-3"
                min="0000"
                max="2400" 
                pattern=".{4,4}"
                required />
            </div>
              <button type="submit" class="btn btn-primary">Submit</button>
          </form>
          <table class="table">
            <thead>
              <tr>
                <th scope="col">T.Out</th>
                <th scope="col">T.In</th>
                <th scope="col">T.I.F.</th>
              </tr>
            </thead>
            <tbody 
              id="response" 
              hx-target="closest tr" 
              hx-swap="outerHTML swap:0.5s"> 
                <tr>
                    <td>{time_out}</td>
                    <td>{time_in}</td>
                    <td>{t_i_f}</td>
                </tr>
            </tbody>
          </table>  
        </div>

        """
        return response

    return render_template("time_in_the_field/index.html",)
