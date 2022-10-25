from flask import Flask
from src.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from src.main.routes import main
    from src.main.area import area
    from src.main.surface_area import surface_area
    from src.main.volume import volume
    from src.main.financial import financial
    from src.main.conversion import conversion
    from src.main.equations import equations
    from src.main.statistics import statistics
    from src.main.gcd import gcd
    from src.main.lcm import lcm
    from src.main.matrix_addition import matrix_addition
    from src.main.miscellaneous import miscellaneous
    from src.main.time_in_the_field import time_in_the_field

    from src.errors.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(area)
    app.register_blueprint(surface_area)
    app.register_blueprint(volume)
    app.register_blueprint(financial)
    app.register_blueprint(conversion)
    app.register_blueprint(equations)
    app.register_blueprint(statistics)
    app.register_blueprint(gcd)
    app.register_blueprint(lcm)
    app.register_blueprint(matrix_addition)
    app.register_blueprint(miscellaneous)
    app.register_blueprint(time_in_the_field)



    app.register_blueprint(errors)

    return app