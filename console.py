from models.munro import Munro
from models.region import Region
import repositories.munro_repository as munro_repository
import repositories.region_repository as region_repository
import pdb

munro_repository.delete_all()
region_repository.delete_all()

region1 = Region("Torridon")
region_repository.save(region1)
munro1 = Munro("Liathach", "2000 ft", False, region1)
munro_repository.save(munro1)

region2 = Region("Cairngorms")
region_repository.save(region2)
munro2 = Munro("Braeriach", "2500 ft", False, region2)
munro_repository.save(munro2)

region3 = Region("Skye Cuillin")
region_repository.save(region3)
munro3 = Munro("Sgùrr a Mhadaidh", "919m", True, region3)
munro_repository.save(munro3)


pdb.set_trace()
