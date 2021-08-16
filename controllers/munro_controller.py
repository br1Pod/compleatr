from flask import Blueprint, Flask, redirect, render_template, request

from models.munro import Munro
import repositories.munro_repository as munro_repository
import repositories.region_repository as region_repository

munros_blueprint = Blueprint("munros", __name__)


# INDEX
@munros_blueprint.route("/munros")
def munros():
    munros = munro_repository.select_all()
    return render_template("munros/index.html", munros=munros)



# ADD
@munros_blueprint.route("/munros/add")
def add_munro():
    munros = munro_repository.select_all()
    regions = region_repository.select_all()
    return render_template("munros/add.html", munros=munros, regions=regions)