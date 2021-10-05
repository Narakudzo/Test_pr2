class Area:
    def __init__(self, Area_width: float, Area_height: float, Area_length:float):


        self.Area_width = Area_width
        self.Area_height = Area_height
        self.Area_length=Area_length


    def get_floor_area(self):
        floor_area = 0
        floor_area = self.Area_width * self.Area_height
        return floor_area


    def get_walls_area(self):
        return ( self.Area_width * self.Area_height, self.Area_length * self.Area_height) * 2


    def get_room_volume(self):
        return self.Area_length * self.Area_height * self.Area_length
