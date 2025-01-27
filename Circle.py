import math

class Circle:

    # only once!!!
    __pi = 3.14  # static/class-member

    # 1 -- static does NOT use static-data/class-members
    @staticmethod
    def get_description():
        return "circle is a round shape!"

    @staticmethod
    def convert_to_radians(degree: float):
        return math.radians(degree)

    # 2 -- static does use static-data/class-members class-method
    @classmethod
    def get_pi(cls):
        #return Circle.__pi
        return cls.__pi

    def __init__(self, radius: float):
        # should use getter/ setter
        self.radius = radius
        # self.pi = 3.14

    # Getter for radius
    @property
    def radius(self):
        return self.__radius

    # Setter for radius
    @radius.setter
    def radius(self, value: float):
        if value <= 0:
            raise ValueError("Radius must be a positive number.")
        self.__radius = value

    def calHekef(self):
        return 2 * self.radius * Circle.__pi

    def __str__(self):
        return f"Circle radius={self.radius} hekef={self.calHekef():.2f}"

# pi: float = 3.14
circle1 = Circle(4.5)
# circle2 = Circle(0.9)
# circle3 = Circle(55.1)
# circle4 = Circle(3)
# print(circle1)
# print(circle1.radius)
print(circle1.get_description())  # Error in some programming languages
print(Circle.get_pi())
print(Circle.get_pi())
