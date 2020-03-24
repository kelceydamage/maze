from environment.worldgen import GeneratedMap
from environment.worldgen import TERRAIN
from environment.worldgen import RESOURCES
from environment.state import WorldState


_map = GeneratedMap().initialize_world()

class World:
    terrain = _map['terrain']
    passable = _map['passable']
    resources = _map['resources']
    precipitation = _map['precipitation']
    sun = _map['sun']
    fertility = _map['fertility']
    rain = _map['rain']
    terrainColorSpace = _map['terrainColorSpace']
    region_types = TERRAIN
    resource_types = RESOURCES

    @staticmethod
    def regen():
        print('regen')
        _map = GeneratedMap().initialize_world()
        World.terrain = _map['terrain']
        World.passable = _map['passable']
        World.resources = _map['resources']
        World.precipitation = _map['precipitation']
        World.sun = _map['sun']
        World.fertility = _map['fertility']
        World.rain = _map['rain']
        World.terrainColorSpace = _map['terrainColorSpace']
