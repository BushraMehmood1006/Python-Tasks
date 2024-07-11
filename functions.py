#  Find the car with lowest price
def lowest_price(cars):
    value = min(cars.values())  
    for car, price in cars.items():
        if price == value:
            print("Car with lowest price: ",car)

# Find the car with highest price       
def highest_price(cars):
    value = max(cars.values())  
    for car, price in cars.items():
        if price == value:
            print("Car with Highest price: ",car)


# Find the cars with price range 1500000-2500000 

def price_range(cars, min_price, max_price):
    cars_in_range = [] 

    for car, price in cars.items():
        if min_price <= price <= max_price:
            cars_in_range.append(car) 

    print("cars with price range 1500000-2500000 : " ,cars_in_range )  
      


cars={"Alto":1800000,
      "City":2500000,
      "Sentro":1200000,
      "Sportage":4300000,
      "Cultus":2300000}
lowest_price(cars)
highest_price(cars)
price_range(cars, 1500000, 2500000)          
