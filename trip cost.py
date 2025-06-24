car_cost = int(input("Enter the cost of the rented car for 1 day: "))
hotel_cost = int(input("Enter the cost of the hotel for 1 night: "))
days_2 = int(input("Enter no. of days car was rented for: "))
flight = input("Enter city: Mumbai, Bengaluru, Chennai, Prayagraj or Lucknow")
days = int(input("Enter no. of days stayed at hotel"))

def car_rental_cost():
    total_cost = car_cost * days_2
def flight_tickets_cost():
    if flight == "Mumbai":
        total_cost = 20000
    elif flight == "Chennai":
        total_cost = 10000
    elif flight == "Bengaluru":
        total_cost = 15000
    elif flight == "Prayagraj":
        total_cost = 7500
    else:
        total_cost = 12500
def hotel_stay_cost():
    total_cost = hotel_cost * days
def total_stay_cost():
    TOTAL_COST = car_rental_cost + flight_tickets_cost + hotel_stay_cost

print("Total car rental cost = ",car_rental_cost)
print("Total flight cost = ",flight_tickets_cost)
print("Total hotel cost = ",hotel_stay_cost)
