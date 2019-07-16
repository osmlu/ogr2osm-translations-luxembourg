"""
ogr2osm translation rule for the import of remarkable trees in Luxembourg

2019 - David Morais Ferreira

https://github.com/DavidMoraisFerreira/ogr2osm-translations-luxembourg
https://wiki.openstreetmap.org/wiki/Import/Catalogue/Remarkable_Trees_Import_Luxembourg

"""
import re

def filterTags(attrs):
    if not attrs:
        return
    
    tags = {}
    
    tags["denotation"] = "natural_monument" 
    tags["debug:arbre_baum"] = attrs.get("arbre_baum")
    tags["debug:type"] = attrs.get("type")

    # Name the trees as best as possible
    if "," in attrs.get("arbre_baum"):
        tags["fixme:survey"] = "Concatenated names in original data set! Data: "+ attrs.get("arbre_baum")
    elif bool(re.search(r"^\d", attrs.get("arbre_baum"))) == True:
        tags["fixme:survey"] = "Multiple trees of a given taxonomy. Data:"+ attrs.get("arbre_baum")
        tags["debug:import_tree"] = "Name starts with a number, check!"
    else:
        tags["taxon"] = attrs.get("arbre_baum")
        split_name = attrs.get("arbre_baum").split(" ")

        if len(split_name) == 1 or len(split_name) == 2 and split_name[1] == "sp.":
            tags["genus"] = split_name[0]
        elif len(split_name) == 2 and split_name[1] and not split_name[1].endswith("."):
            tags["species"] = split_name[0] + " " + split_name[1]
        elif len(split_name) > 2:
            tags["species"] = split_name[0] + " " + split_name[1]
            tags["debug:import_tree"] = "Long name, check!"

    # Determine what type of information should be mapped
    if attrs.get("type") in ["Einzelbaum", "Gruppe"]:
        tags["natural"] = "tree"
        if attrs.get("type") == "Gruppe":
            tags["debug:import_tree"] = "Group of trees!"
    elif attrs.get("type") in ["Allee", "Reihe", "Baumreihe"]:
        tags["natural"] = "tree_row"
        tags["debug:import_tree"] = "Tree row!"

    return tags