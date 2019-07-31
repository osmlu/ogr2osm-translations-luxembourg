"""
ogr2osm translation rule for the import of rescue points (points de sauvetage) in the city of Luxembourg (Ville de Luxembourg) 

2019 - David Morais Ferreira

https://github.com/DavidMoraisFerreira/ogr2osm-translations-luxembourg

"""
import re

def filterTags(attrs):
    if not attrs:
        return
    
    tags = {}

    tags["highway"] = "emergency_access_point"
    tags["operator"] = "VdL"
    
    if attrs.get("ELEVATION"):
        raw_elevation = float(attrs.get("ELEVATION"))
        tags["ele"] = "{0:.0f}".format(raw_elevation)
    
    match = re.match(r"(.*?)[,\.]", attrs.get("REMARQUE"))
    if match:
        extracted_ref = match.group(1)
        cleaned_ref = extracted_ref.replace(" ", "")
        tags["ref"] = cleaned_ref

    return tags