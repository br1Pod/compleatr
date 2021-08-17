from db.run_sql import run_sql
from models.munro import Munro
from models.region import Region
import repositories.region_repository as region_repository

def save(munro):
    sql = "INSERT INTO munros(name, height, climbed, region_id) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [munro.name, munro.height, munro.climbed, munro.region.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    munro.id = id
    return munro


def select_all():
    munros = []

    sql = "SELECT * FROM munros"
    results = run_sql(sql)

    for row in results:
        region = region_repository.select(row['region_id'])
        munro = Munro(row['name'], row['height'], row['climbed'], region, row['id']) 
        munros.append(munro)
    return munros


def select(id):
    munro = None
    sql = "SELECT * FROM munros WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        region = region_repository.select(result['region_id'])
        munro = Munro(result['name'], result['height'], result['climbed'], region.id)
    return munro


def delete_all():
    sql = "DELETE FROM munros"
    run_sql(sql)