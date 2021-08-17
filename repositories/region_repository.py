from db.run_sql import run_sql
from models.region import Region


def save(region):
    sql = "INSERT INTO regions (name) VALUES (%s) RETURNING *"
    values = [region.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    region.id = id
    return region


 


def select_all():
    regions = []
    sql = "SELECT * FROM regions"
    results = run_sql(sql)
    for row in results:
        region = region(row['name'], row['id'])
        regions.append(region)
    return regions