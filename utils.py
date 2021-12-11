import requests

def getDrivers(): #retorna lista de pilotos
 url = 'http://ergast.com/api/f1/2021/drivers.json'
 payload = {'limit': 30} #envia parametros na URL
 res = requests.get(url, params=payload)
 data = res.json() 
 drivers = data['MRData']
 table = drivers['DriverTable']
 driverList = table['Drivers']
 return driverList


def getConstructors(): #retorna lista de equipes
 url = 'http://ergast.com/api/f1/2021/constructors.json'
 payload = {'limit': 10} #envia parametros na URL
 res = requests.get(url, params=payload)
 data = res.json() 
 constructors = data['MRData']
 table = constructors['ConstructorTable']
 construList = table['Constructors']
 return construList