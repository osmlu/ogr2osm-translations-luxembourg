"""
ogr2osm Translation rules Luxembourg's BD-L-TC AND PCN datasets.
NATURE Identifiers are described in "Specifications-BD-L-TC-2013-V1.pdf" at https://data.public.lu/fr/datasets/bd-l-tc-2015/

2019 - David Morais Ferreira 
https://github.com/DavidMoraisFerreira/ogr2osm-translations-luxembourg

NOTE: This is very experimental, and far from finished!
      To generate the source data: BD-L-TC and PCN/Batiments.shp are merged in QGIS
	  	Vector -> Data Management Tools -> Join Attributes by Location
		  Input Layer: PCN
		  Join Layer: BD-L-TC
		  Geometric predicate: intersects, contains, equals, overlaps, within
		  Join Type: "Create separate feature for each located feature (one-to-many)"
"""

# TODO: NATURE=0 : Les batiments en construction sont saisis avec cette valeur d'attribut, le Z est alors non significatif.
# TODO: How reliable/useful is Z?
def filterTags(attrs):
	if not attrs:
		return
	
	if attrs.get('NATURE', None) is None:
		return

	tags = {}

	if attrs['NATURE']:
		tags.update({'debug:NATURE':attrs['NATURE']}) #TODO: Debug, remove me/Add flag!
		tags.update({'debug:CODE_OCCUP':attrs['CODE_OCCUP']})

		tags.update({'building':'yes'}) #Safe default tag
		if attrs['NATURE']=="0" and attrs['CODE_OCCUP']=="5029":
			tags.update({'building':'apartments'})
		if attrs['NATURE']=="10000":
			tags.update({'building':'industrial'})
		if attrs['NATURE']=="20000" or attrs['CODE_OCCUP']=="5004":
			tags.update({'building':'farm_auxiliary'})
		if attrs['NATURE']=="30000":
			tags.update({'building':'retail'})
		if attrs['NATURE']=="40000":
			tags.update({'building':'public'})
		if attrs['NATURE'] in ["40101", "40102", "40103", "40201", "40303", "40304", "40501", "40502", "40503"]:
			tags.update({'building':'government'})
		if attrs['NATURE'] in ["40301", "40302", "40305", "40402", "40704"]:
			tags.update({'building':'civic'})
		if attrs['NATURE'] in ["40701", "40703"] or attrs['CODE_OCCUP']=="5020":
			tags.update({'building':'school'})		
		if attrs['NATURE']=="41201":
			tags.update({'building':'hospital'})
		if attrs['NATURE']=="41302":
			tags.update({'building':'kiosk'})
		if attrs['NATURE']=="50001":
			tags.update({'building':'cathedral'})
		if attrs['NATURE']=="50002":
			tags.update({'building':'church'})
		if attrs['NATURE']=="50003":
			tags.update({'building':'temple'})
		if attrs['NATURE']=="50004":
			tags.update({'building':'church'})
		if attrs['NATURE']=="50005":
			tags.update({'building':'chapel'})
		if attrs['NATURE'] in ["50006", "50007", "50008"] or attrs['CODE_OCCUP']=="5006":
			tags.update({'building':'religious'})
		if attrs['NATURE']=="50011":
			tags.update({'building':'synagogue'})
		if attrs['NATURE'] in ["70001", "70002"]:
			tags.update({'building':'sports_hall'})
		if attrs['NATURE']=="80000":
			tags.update({'building':'greenhouse'})
		if attrs['NATURE']=="100000":
			tags.update({'building':'parking'})
		if attrs['CODE_OCCUP']=="5026":
			tags.update({'building':'garage'})
		if attrs['CODE_OCCUP']=="5030":
			tags.update({'building':'construction'})
	return tags