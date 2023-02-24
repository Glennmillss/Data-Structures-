#Cars available and their cost
cars={"Hyundai Azera":50200,
      "Hyundai Ioniq":68940,
      "Hyundai Sonata":32000,
      "KIA Sportage":47000,
      "KIA Sorento":54200,
      "KIA Telluride":63500,
      "KIA Forte":70000,
      "Ford Escape":55000,
      "Ford Bronco":58200,
      "Ford Edge":49000,
      "Ford Expedition":65000,
      "Ford Explorer":37800,
      "BMW i4":75900,
      "BMW X1":81000,
      "Honda Civic":11250,
      "Honda Accord":15000,
      "Honda CRV":26000,
      "Honda Pilot":35000,
      "Honda Ridgeline":35500,
      "Honda Odyssey":42800,
      "Nissan Rogue":600000,
      "Nissan Pathfinder":57800,
      "Nissan Armada":56900,
      "Nissan Ariya":65500,
      "Nissan Murano":54780,
      "Range Rover Velar":150000,
      "Range Rover Evoque":100000,
      "Range Rover Sport":250000}
# get user input for car name
car_name=input("Enter a car_name: ")
#check if car name is in list available
if car_name in cars:
     print("Yes")
#if car name is present,get its price
     car_price=cars[car_name]
     print( f"The price of {car_name} is ${car_price}." )
else:
    # if car name is not present, inform the user
    print(f"Sorry,{car_name} is not available.")
#GitHub username : Glennmillss