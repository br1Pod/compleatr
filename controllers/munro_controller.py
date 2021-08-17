from flask import Blueprint, Flask, redirect, render_template, request

from models.munro import Munro
import repositories.munro_repository as munro_repository
import repositories.region_repository as region_repository

munros_blueprint = Blueprint("munros", __name__)

# INDEX
@munros_blueprint.route("/munros")
def munros():
    munros = munro_repository.select_all()
    regions = region_repository.select_all()
    return render_template("munros/index.html", munros=munros, regions = regions)


# ADD
@munros_blueprint.route("/munros/add", methods=["GET"])
def add_munro():
    return render_template("munros/add.html")


# save
@munros_blueprint.route("/munros", methods = ["POST"])
def save_munro():
    name = request.form['name']
    height = request.form['height']
    climbed = False
    region_id = request.form['region']
    region = region_repository.select(region_id)
    munro = Munro(name, height, climbed, region)
    munro_repository.save(munro)
    return redirect('/munros')    


# DISPLAY
@munros_blueprint.route("/munros/<id>")
def display_munro(id):
    munro = munro_repository.select(id)
    return render_template("/munros/display.html", munro = munro)


# EDIT
@munros_blueprint.route("/munros/<id>/edit")
def edit_munro(id):
    munro = munro_repository.select(id)
    return render_template('munros/edit.html', munro = munro)


# DEL
@munros_blueprint.route("/munros/<id>/delete", methods=["POST"])
def delete(id):
    munro_repository.delete(id)
    return redirect("/munros")


# UPDATE
@munros_blueprint.route("/munros/<id>", methods=["POST"])
def update_munro(id):
    name = request.form['name']
    height = request.form['height']
    climbed = request.form['climbed']
    region = request.form['region']
    munro = Munro(name, height, climbed, region)
    munro_repository.update(munro)
    return redirect("/munros")
