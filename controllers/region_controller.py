from flask import Blueprint, Flask, redirect, render_template, request

from models.region import Region
import repositories.region_repository as region_repository
import repositories.munro_repository as munro_repository

regions_blueprint = Blueprint("regions", __name__)

# INDEX
@regions_blueprint.route("/regions")
def regions():
    regions = region_repository.select_all()
    return render_template("regions/index.html", regions=regions)


# ADD
@regions_blueprint.route("/regions/add", methods=["GET"])
def add_region():
    return render_template("regions/add.html")


# save
@regions_blueprint.route("/regions", methods = ["POST"])
def save_region():
    name = request.form['name']
    region = Region(name)
    region_repository.save(region)
    return redirect('/regions')


# DISPLAY
@regions_blueprint.route("/regions/<id>")
def display_region(id):
    region = region_repository.select(id)
    return render_template("/regions/display.html", region = region)


# EDIT
@regions_blueprint.route("/regions/<id>/edit")
def edit_region(id):
    region = region_repository.select(id)
    return render_template('regions/edit.html', region = region)


# DEL
@regions_blueprint.route("/regions/<id>/delete", methods=["POST"])
def delete(id):
    region_repository.delete(id)
    return redirect("/regions")


# UPDATE
@regions_blueprint.route("/regions/<id>", methods=["POST"])
def update_region(id):
    name = request.form['name']
    region = Region(name, id)
    region_repository.update(region)
    return redirect("/regions")


