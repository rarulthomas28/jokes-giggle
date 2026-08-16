import requests 
import time


joke = input('What type of joke would you like to hear: random or programming? Choose one bro ')

if joke == 'random': 


    
    num = input('How Many:')

    if num == '': 
       jokes = requests.get("https://official-joke-api.appspot.com/random_joke")
       data = jokes.json()

       print('Joke: {}... {}'.format(data['setup'], data['punchline']))
    elif num == 'ten': 
       jokes = requests.get("https://official-joke-api.appspot.com/random_ten")
       data = jokes.json()
       for dude in range(len(data)): 
                       
             print('Joke: {}.....'.format(data[dude]["setup"]))
             time.sleep(3)
             print(data[dude]['punchline'])
             time.sleep(1)
       
    else: 
     if type(num) and num != '': 
       value = int(num)

     jokes = requests.get(f"https://official-joke-api.appspot.com/jokes/random/{value}")
     data = jokes.json()
     for dude in range(len(data)): 
                
      print('Joke: {}.....'.format(data[dude]["setup"]))
      time.sleep(3)
      print(data[dude]['punchline'])
      time.sleep(1)
   

elif joke == 'programming':
   num = input('Would you like a Random one or 10 of them ')
   if num == str(10): 
        
              jokes = requests.get("https://official-joke-api.appspot.com/jokes/programming/ten")
              data = jokes.json()
              for dude in range(len(data)): 
                    
               print('Joke: {}.....'.format(data[dude]['setup']))
               time.sleep(3)
               print(data[dude]['punchline'])
               time.sleep(1)
   elif num == 'a random': 
        jokes = requests.get("https://official-joke-api.appspot.com/jokes/programming/random")
        data = jokes.json()

        for dude in range(len(data)): 
             
         print('Joke: {}.....'.format(data[dude]['setup']))
         time.sleep(3)
         print(data[dude]['punchline'])
         time.sleep(1)

     
        
        






   


    


       
       
    