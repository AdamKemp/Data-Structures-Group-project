class lift():
    # Attributes include: num_floors, requests, capacity, y_coord
    requests = []
    """???requests could be represented as a priority queue, 
    each element may be a dictionary with floor as the key, 
    number of people and time waited as values???"""
    
    def __init__(self, num_floors, capacity, start = 0):
        self.num_floors = num_floors
        self.capacity = capacity
        self.y_coord = start
    
    


    