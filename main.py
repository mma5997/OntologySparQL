import pandas as pd #for handling csv and csv contents
from rdflib import Graph, Literal, RDF, URIRef, Namespace #basic RDF handling
from rdflib.namespace import FOAF , XSD #most common namespaces
import urllib.parse #for parsing strings to URI's

const = {
    "schema" : "http://schema.org/",
    "root_entity" : "http://example.org/rainfall_stats/",
    "longitude_entity" : "http://mylocations.org/longitude/",
    "latitude_entity" : "http://mylocations.org/latitude/",
    "rain_entity" : "http://mylocations.org/rain",
    "col_names" : ["Longitude", "Latitude", "Rain"],
    "url" : "C:/Users/mautade/Downloads/output.xlsx",
    "link" : "https://drive.google.com/file/d/1aSGlKThD_NSR9rmgzRtCMDiNsoUHUaNW/view?usp=sharing"
} 

url = const["link"]
df=pd.read_csv(url,names=const["col_names"])
print(df)

# g = Graph()
# rain_stat = Namespace(const["rain_entity"])
# longitude = Namespace(const["longitude_entity"])
# latitude = Namespace(const["latitude_entity"])
# schema = Namespace(const["schema"])

# for index, row in df.iterrows():
#     g.add((URIRef(ppl+row['']), RDF.type, FOAF.Person))