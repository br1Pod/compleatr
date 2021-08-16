from db.run_sql import run_sql
from models.region import Region


def save(region):
    sql = "INSERT INTO regions (name) VALUES (%s) RETURNING id"
    values = [region.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    region.id = id