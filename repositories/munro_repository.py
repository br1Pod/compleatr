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
        munro = munro(row['name'], row['height'], row['climbed'], row['region']) 
        munros.append(munro)
    return munros