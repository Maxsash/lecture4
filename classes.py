class Flight:
    ## special inbuilt method. Take these inputs and make their references.
    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration
    
    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")

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

if __name__ == "__main__":
    main()
