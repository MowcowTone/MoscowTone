#класс для чтения данных
import pandas
class dan():
    def __init__(self,file_name):
        self.file_name = file_name
    def read(self):
        self.adres = pandas.read_excel(self.file_name)['адрес']
        self.cord = pandas.read_excel(self.file_name)['координаты']
        #self.Entrances = pandas.read_excel(self.file_name)['Подьездов']
        self.apartments = pandas.read_excel(self.file_name)['квартиры']
        self.peoples = pandas.read_excel(self.file_name)['человеки']
        