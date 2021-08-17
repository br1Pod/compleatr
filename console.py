from models.munro import Munro
from models.region import Region
import repositories.munro_repository as munro_repository
import repositories.region_repository as region_repository

region1 = Region("Torridon")
munro1 = Munro("Liathach", "2000m", False, region1)

region_repository.save(region1)
munro_repository.save(munro1)