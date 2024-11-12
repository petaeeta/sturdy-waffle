import toml
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        myDict = toml.loads(content)
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(myDict["tool"]["poetry"]["name"], myDict["tool"]["poetry"]["description"], myDict["tool"]["poetry"]["license"], myDict["tool"]["poetry"]["authors"], myDict["tool"]["poetry"]["dependencies"], myDict["tool"]["poetry"]["group"]["dev"]["dependencies"])
