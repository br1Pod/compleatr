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
@regions_blueprint.route("/regions/add")
def add_region():
    return render_template("regions/add.html")

