class lift():
    #initialise requests as an empty list
    requests = []
    """???requests could be represented as a priority queue, 
    each element may be a dictionary with floor as the key, 
    number of people and time waited as values???"""

    def __init__(self, num_floors, capacity, start = 0, speed = 1):
        #initialise initial attributes
        self.__num_floors = num_floors
        self.__capacity = capacity
        self.__y_coord = start
        self.__speed = speed
    
    #getters and setters for class attributes
    def get_floors(self):
        return self.__num_floors
    
    def get_capacity(self):
        return self.__capacity
    
    def get_y(self):
        return self.__y_coord
    
    def set_y(self, val):
        self.__y_coord = val
    
    def get_speed(self):
        return self.__speed