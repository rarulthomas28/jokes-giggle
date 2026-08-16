import requests 
import math

weather_info = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=48.58&lon=7.75&appid=800c4464c2b950cd8306d8457cb45a3c")
# print(weather_info.status_code)
# print()
#48.58, 7.75

date_de_france = weather_info.json()
print(date_de_france)
print()

print()
print()
print()
print()

print()

for hog in date_de_france: 

    if type(date_de_france[hog]) is str or type(date_de_france[hog]) is int: 

        print("{} : {}".format(hog, date_de_france[hog]))
    if type(date_de_france[hog]) is dict: 
         print("-----{}-----> ".format(hog))

         for name, info in date_de_france[hog].items(): 
             if name == 'temp' or name == 'temp_min' or name == 'temp_max' or name == 'feels_like': 
                 newVal = info - 273
                 print('{}: {:.2f}'.format(name, newVal))
             else: 
                 print("{}: {}".format(name, info))

         
    if type(date_de_france[hog]) is list: 
        
        print("------{}------: ".format(hog))
        for dude in date_de_france[hog]: 
            for name, info in dude.items(): 
                print('{}: {}'.format(name, info))
        print('---------------')



        
                 
             
             
             
            




    

        





