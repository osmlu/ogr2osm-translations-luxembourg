"""
ogr2osm translation rule for the import of the CGDIS "centres d'incendies et de secours" (CIS) fire stations in Luxembourg

2019 - David Morais Ferreira

https://github.com/DavidMoraisFerreira/ogr2osm-translations-luxembourg
https://data.public.lu/fr/datasets/emplacements-des-centres-dincendie-et-de-secours-cis/

"""
import re

def filterTags(attrs):
    if not attrs:
        return
    
    tags = {}
    
    name = attrs.get("Wache")
    tags["name"] = name
    tags["official_name"] = name.replace("CIS", "Centre d'incendie et de secours")
    tags["amenity"] = "fire_station"
    tags["operator"] = "CGDIS"
    tags["operator:wikipedia"] = "lb:Corps grand-ducal d'incendie et de secours"
    tags["operator:wikidata"] = "Q55334052"  

    return tags