# -*- coding: utf-8 -*-
"""
ogr2osm translation rule for the import of existing AND planned wind turbines (éoliennes) in Luxembourg

2020 - David Morais Ferreira

https://github.com/DavidMoraisFerreira/ogr2osm-translations-luxembourg
https://data.public.lu/en/datasets/eoliennes/

"""
import re

def filterTags(attrs):
    if not attrs:
        return
    
    tags = {}

    if attrs.get("ETAT") == "existant":
        tags["power"] = "generator"
    elif attrs.get("ETAT") == u"autorisé":
        tags["power"] = "construction"
        tags["construction"] = "generator"
        tags["fixme"] = "survey whether construction has begun"
    else:
        print("ERROR: Unhandled state: %s detected" % attrs.get("ETAT"))

    tags["generator:method"] = "wind_turbine"
    tags["generator:type"] = "horizontal_axis"
    tags["generator:source"] = "wind"
    tags["generator:plant"] = "output"
    tags["generator:output:electricity"] = "%s kW" % (strip_float(float(attrs.get("PUISSANCE"))))
    tags["rotor:diameter"] = strip_float(float(attrs.get("D_HELICE")))
    tags["height"] = strip_float(float(attrs.get("H_NOYAU")))
    return tags

def strip_float(flt):
    return ("%f" % flt).rstrip('0').rstrip('.')