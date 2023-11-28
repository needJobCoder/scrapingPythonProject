import bs4.element
import requests
from bs4 import BeautifulSoup
import array

url: str = "https://en.wikipedia.org/wiki/List_of_exoplanets_discovered_by_the_Kepler_space_telescope:_1%E2%80%93500"
path: str = "/home/needjobcoder/Documents/Development/web/webPythonProject/django/django-practice/backend/scrapedData/index.html"
children: array = []
# Open the file in read mode
with open(path, 'r', encoding='utf-8') as file:
    file_content = file.read()

soup = BeautifulSoup(file_content, "html.parser")

PLANET_DATA: array = []


def getHeaders():
    getHeaders = soup.find_all("th")
    for headers in getHeaders:
        print(headers.getText())


# Planet type
# Planet
# Disc­overy method
# Mass(MJ)
# Radius(RJ)
# Density(g/cm3)
# Orbital period(days)
# Semimajor axis(AU)
# Orbital eccentricity
# Year ofcon­firm­ation
# Ref.
# Planet
# Disc­overy method
# Mass(MJ)
# Radius(RJ)
# Density(g/cm3)
# Orbital period(days)
# Semimajor axis(AU)
# Orbital eccentricity
# Year ofcon­firm­ation
# Ref.
class Planet:
    def __init__(self, planet=None, discovery=None, mass=None, radius=None, density=None, orbitalPeriod=None,
                 semimajorAxis=None, orbitalEccentricity=None, year=None, ref=None):
        self.discovery = discovery
        self.planet = planet
        self.mass = mass
        self.radius = radius
        self.density = density
        self.orbitalPeriod = orbitalPeriod
        self.semimajorAxis = semimajorAxis
        self.orbitalEccentricity = orbitalEccentricity
        self.year = year
        self.ref = ref

    def getObj(self):
        return {
            "discovery": self.discovery,
            "planet": self.planet,
            "mass": self.mass,
            "radius": self.radius,
            "density": self.density,
            "orbitalPeriod": self.orbitalPeriod,
            "semimajorAxis": self.semimajorAxis,
            "orbitalEccentricity": self.orbitalEccentricity,
            "year": self.year,
            "ref": self.ref
        }


def getPlanetData():
    getTable: bs4.element.ResultSet = soup.find_all("table", class_="sortable wikitable")
    for index, row in enumerate(getTable):
        td_elements = row.find_all('td')
        # Process the <td> elements as needed
        for td in td_elements:
            # Do something with the <td> element, for example, print its text content
            children.append(td.get_text())


getPlanetData()


def isExists(idx: int):
    try:
        return children[idx]
    except IndexError:
        return None


def makeProperObject():
    # Start the index at 0
    index = 0

    # While loop to iterate through the list
    while index < len(children):
        #
        # print("planet " + children[index+ 0])
        # print("discovery" + children[index + 1])
        # print("mass " + children[index + 2])
        # print("radius " + children[index + 3])
        # print("density" + children[index + 4])
        # print("orbitalPeriod " + children[index + 5])
        # print("semimajor " + children[index + 6])
        # print("orbital " + children[index + 7])
        # print("year " + children[index + 8])
        # print("ref" + children[index + 9])

        planet_object = Planet(isExists(index + 0),
                               isExists(index + 1),
                               isExists(index + 2),
                               isExists(index + 3),
                               isExists(index + 4),
                               isExists(index + 5),
                               isExists(index + 6),
                               isExists(index + 7),
                               isExists(index + 8),
                               isExists(index + 9))
        PLANET_DATA.append(planet_object)
        index += 10


makeProperObject()
for element in PLANET_DATA:
    print(element.getObj())
