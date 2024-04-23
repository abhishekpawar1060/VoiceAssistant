import requests

key = "Enter the API_key"

api_address = "https://newsapi.org/v2/everything?q=apple&from=2024-04-08&to=2024-04-08&sortBy=popularity&apiKey="+key

json_data = requests.get(api_address).json()

list = []
def news():
    for i in range(5):
       list.append("Number "+str(i+1)+": " + json_data["articles"][i]["title"]+".")

    return list

# arr = news()
# print(arr)
