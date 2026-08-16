import requests 


response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print("This is the status code: " + str(response.status_code))
print("The Content type: {}".format(response.headers.get("Content-Type")))

data = response.json()
print(data)

newStuff = {'conquistador': 'Bonjour'}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json = newStuff)

print(response.status_code)

patch_data = {'userId': 2}
response = requests.patch("https://jsonplaceholder.typicode.com/posts/1", json=patch_data)

print(response.status_code)

print()
print()

response1 = requests.get("https://jsonplaceholder.typicode.com/posts")

# print(response1.status_code)
data1 = response1.json()


for title in data1: 

    if title['userId'] == 2: 
        print(title['title'])

num_times = len(data1)
print(num_times)



response = requests.get("https://fakestoreapi.com/products")
print(response.status_code)

data = response.json()

print()
print()
print()


for hello in data: 

    print(hello)

     

# for dude in data: 

#    for key in dude: 
#       print(key)
#    break

xc_track = {'id': 67, 'title': 'Nike Men\'s DragonFly Spikes', 'price': 126.78, 'description': 'Best Track spikes for high schoolers right now, can be used in distances 400 meters or greater, highly recommended for the 800 meters', 'category': 'Shoes(spikes in particular)', 'image': 'Google it bro', 'rating': '10/10'}

response = requests.post("https://fakestoreapi.com/products", json = xc_track)
print(response.status_code)







