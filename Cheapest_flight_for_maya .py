import random

def find_cheapest_flight(destination, flexibility_days, budget, preferred_airlines=None):
    # Simulated flight data for demonstration purposes
    airlines = ["Garuda Indonesia", "Singapore Airlines", "AirAsia", "Lion Air", "Cathay Pacific"]
    
    # Simulated flight prices for different airlines and dates
    flights = [{"airline": airline,
                "price": random.randint(800, 1500),
                "departure_date": "2024-07-01",
                "return_date": "2024-07-15"}
               for airline in airlines]

    # Simulated additional factors (e.g., layover duration, overall flight rating)
    for flight in flights:
        flight["layover_duration"] = random.randint(1, 8)
        flight["flight_rating"] = round(random.uniform(3.5, 5.0), 1)

    # Filtering flights within budget and flexibility range
    valid_flights = [flight for flight in flights if
                     budget >= flight["price"] >= budget - 300 and
                     "preferred_airlines" not in locals() or flight["airline"] in preferred_airlines]

    # Sorting valid flights by price and other criteria
    sorted_flights = sorted(valid_flights, key=lambda x: (x["price"], x["layover_duration"], -x["flight_rating"]))

    # Displaying the top 3 cheapest flight options
    top_3_flights = sorted_flights[:3]

    for idx, flight in enumerate(top_3_flights, start=1):
        print(f"\nOption {idx}:")
        print(f"Airline: {flight['airline']}")
        print(f"Price: ${flight['price']}")
        print(f"Departure Date: {flight['departure_date']}")
        print(f"Return Date: {flight['return_date']}")
        print(f"Layover Duration: {flight['layover_duration']} hours")
        print(f"Flight Rating: {flight['flight_rating']}")

# Example usage:
find_cheapest_flight(destination="Bali", flexibility_days=3, budget=2000, preferred_airlines=["Garuda Indonesia", "Singapore Airlines"])

  