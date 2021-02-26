# -*- coding: utf-8 -*-
"""
ogr2osm translation rule for the import of fire hydrants in Esch-sur-Alzette, Luxembourg

2021 - David Morais Ferreira

https://github.com/osmlu/ogr2osm-translations-luxembourg
https://data.public.lu/fr/datasets/hydrants-de-la-ville-desch-sur-alzette/

"""

def filterTags(attrs):
    if not attrs:
        return
    
    tags = {}
    
    tags["emergency"] = "fire_hydrant"
    if attrs.get("TYP") == "UNHY":
        assert attrs.get("LIBELLE") == "bouche d'incendie"
        tags["fire_hydrant:type"] = "underground"
    elif attrs.get("TYP") == "UEHY":
        assert attrs.get("LIBELLE") == "hydrant"
        tags["fire_hydrant:type"] = "pillar"
    else:
        print("ERROR: Unhandled state: %s" % attrs.get("TYP"))
    
    return tags