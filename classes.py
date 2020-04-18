class Flight:
    ## keep track of flight
    counter = 1 
    ## special inbuilt method. Take these inputs and make their references.
    def __init__(self, origin, destination, duration):
        
        #keep track of id number
        self.id = Flight.counter
        Flight.counter += 1

        #keep track of passengers
        self.passengers = []

        #details about flight
        self.origin = origin
        self.destination = destination
        self.duration = duration
    
    def print_info(self):
        print(f"\nFlight{self.id} origin: {self.origin}")
        print(f"Flight{self.id} destination: {self.destination}")
        print(f"Flight{self.id} duration: {self.duration}")

        if len(self.passengers)>0:
            print(f"\nFlight{self.id} Passengers: ")
            for passenger in self.passengers:
                print(f"{passenger.name}")

    def delay(self, amount):
        self.duration += amount

    def add_passenger(self, p):
        # p will be a passenger object
        self.passengers.append(p)
        p.flight_id = self.id

class Passenger:

    def __init__(self, name):
        self.name = name

def main():
    
    # create flight.
    f = Flight(origin="New York", destination="Paris", duration=540)

    #change the value of a variable.
    f.duration += 10

    # print details about flight.
    print(f.origin)
    print(f.destination)
    print(f.duration)

    # create another flight
    f2 = Flight(origin="Tokyo", destination="Shanghai", duration=185)
    f2.print_info()

    #use the delay class
    f.delay(12)
    f.print_info()

    #create passengers
    alice = Passenger("Alice")
    bob = Passenger("Bob")

    #add passengers
    f2.add_passenger(alice)
    f2.add_passenger(bob)

    f2.print_info()

if __name__ == "__main__":
    main()
