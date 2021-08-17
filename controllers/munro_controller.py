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
@munros_blueprint.route("/munros/add", methods=["GET"])
def add_munro():
    return render_template("munros/add.html")


# save
@munros_blueprint.route("/munros", methods = ["POST"])
def save_munro():
    name = request.form['name']
    height = request.form['height']
    climbed = request.form['climbed']
    region = request.form['region_id']
    munro = Munro(name, height, climbed, region)
    munro_repository.save(munro)
    return redirect('/munros')    

# DISPLAY
@munros_blueprint.route("/munros/<id>")
def display_munro(id):
    munro = munro_repository.select(id)
    return render_template("/munros/display.html", munro = munro)