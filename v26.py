class Car:
    def __init__(self, name: str, price: int, capacity: int, color: str, model: str) -> None:
        self.name = name
        self.price = price
        self.capacity = capacity
        self.color = color
        self.model = model

    def setname(self, new_name)->None:
        self.name = new_name

    def setprice(self, new_price)->None:
        self.price = new_price

    def setcapacity(self, new_capacity)->None:
        self.capacity = new_capacity

    def setcolor(self, new_color)->None:
        self.color = new_color
    
    def setmodel(self, new_model)->None:
        self.model = new_model

    def get_name(self)->str:
        return self.name

    def get_price(self)->int:
        return self.price

    def get_capacity(self)->int:
        return self.capacity

    def get_color(self)->str:
        return self.color
    
    def get_model(self)->str:
        return self.model
    
    def __str__(self) -> str:
        return f"""Name: {self.name}
Model: {self.model}
Capacity: {self.capacity}
Color: {self.color}
Price: {self.price}"""

class Address:
    def __init__(self, country: str, city: str, street: str) -> None:
        self.country = country
        self.city = city
        self.street = street

    def getcountry(self)->str:
        return self.country
    
    def setcountry(self, country:str)->None:
        self.country = country

    def getcity(self)->str:
        return self.city
    
    def setcity(self, city:str)->str:
        self.city = city

    def getstreet(self)->str:
        return self.street
    
    def setstreet(self, street:str)->None:
        self.street = street

    def __str__(self) -> str:
        return f"""Country: {self.country}
City: {self.city}
Street: {self.street}"""

class Carshowroom:
    def __init__(self, address: Address, cars: list[Car], name: str, rating: list[int]) -> None:
        self.address = address
        self.cars = cars
        self.name = name
        self.rating = rating

    def addcar(self, car: Car)->None:
        self.cars.append(car)

    def removecar(self, car: Car)->None:
        self.cars.remove(car)

    def getcarsinfo(self)->None:
        for car in self.cars:
            print(str(car))
            print("\n"+"="*30+"\n")

    def getaddress(self)->None:
        print(str(self.address))

    def changename(self, new_name: str)->None:
        self.name = new_name

    def getname(self)->None:
        print(self.name)

    def rate(self, rate: int)->None:
        """(0<n<=5)"""
        self.rating.append(rate)

    def getaveragerating(self)->int:
        return (sum(rate for rate in self.rating)//len(self.rating))
    
    def __str__(self) -> str:
        return f"""Name: {self.name}
{str(self.address)}
Number of cars: {len(self.cars)}
Average rating: {self.getaveragerating()}"""
    

car1 = Car(name="Toyota Corolla", price=20000, capacity=5, color="Red", model="2020")
car2 = Car(name="Honda Civic", price=22000, capacity=5, color="Blue", model="2021")

address = Address(country="USA", city="Los Angeles", street="123 Car St")

carshowroom = Carshowroom(address=address, cars=[car1, car2], name="Super Cars", rating=[4, 5, 3])

car3 = Car(name="Ford Mustang", price=35000, capacity=4, color="Black", model="2022")
carshowroom.addcar(car3)

# carshowroom.removecar(car1)

# print("Car Information:")
# carshowroom.getcarsinfo()

# print("Showroom Address:")
# carshowroom.getaddress()

# carshowroom.changename("Premium Cars")

# print("Showroom Name:")
# carshowroom.getname()

# carshowroom.rate(5)

# average_rating = carshowroom.getaveragerating()
# print(f"Average Rating: {average_rating}")

print("Showroom Details:")
print(carshowroom)