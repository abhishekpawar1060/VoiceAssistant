import requests

# key = "9d6ffcb1040447a7b2cab6e7aca9323a"

api_address = "https://newsapi.org/v2/everything?q=apple&from=2024-04-08&to=2024-04-08&sortBy=popularity&apiKey=9d6ffcb1040447a7b2cab6e7aca9323a"

json_data = requests.get(api_address).json()

list = []
def news():
    for i in range(5):
       list.append("Number "+str(i+1)+": " + json_data["articles"][i]["title"]+".")

    return list

# arr = news()
# print(arr)