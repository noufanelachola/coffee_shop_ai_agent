import requests
import datetime

API_KEY ="c8b6f96c14d847d0be485412252603"


menu = {
  "Tea" : 10,
  "Coffee" : 15,
  "Hot chocolate" : 20,
  "Lemonade" : 10,
  "Ice Cream" : 30
}

class customer:
  def __init__(self,name,city):
    self.name = name
    self.city = city
    self.url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={self.city}&aqi=no"
    self.weather = self.get_weather()
    
  def get_weather(self):
    response = requests.get(self.url)

    if response.status_code == 200:
      return response.json()
    else :
      print("Failed to retrieve weather data.")
      return None

  def greet(self):
    hour = datetime.datetime.now().hour
  
    if hour < 12:
      print(f"Good morning, {self.name}")
  
    elif hour < 18:
      print(f"Good afternoon, {self.name}")  
  
    else:
      print(f"Good evening, {self.name}")

  def suggest_drink(self):
    if self.weather:
      temperature = self.weather["current"]["temp_c"]

      if temperature < 10:
        print("\nIt's cold outside. You should drink some hot chocolate.\n")
      elif temperature < 20:
        print("\nIt's a bit chilly. You should have some tea.\n")
      elif temperature < 30:
        print("\nIt's warm outside. You should have some coffee.\n")
      else:
        print("\nIt's hot outside. You should have some ice cream.\n")

  def order(self):
    print("Here's our menu : \n")
    for item, price in menu.items():
      print(f"{item} : ${price}")

    order_in = input("\nWhat would you like to order? ")
    if order_in in menu:
      print(f"\nYou ordered {order_in}. That will be ${menu[order_in]}.\nwill serve you soon..")
    else:
      print("Sorry we dont have it in our menu.")

  def run(self):
    self.greet()
    self.suggest_drink()
    self.order()


name = input(f"What is your name? ")
city = input(f"What is your city? ")

customer1 = customer(name,city)
customer1.run()