class bike_type:
    def __init__(self, color, model, year, value):
        self.color = color
        self.model = model
        self.year = year
        self.value = value

    def beep_bike(self):
        print("Plim plim....")

    def stop_bike(self):
        print("Stopping the bike...")
        print("Parked bike")
    
    def to_run(self):
        print("Vruuummm")


bike_type_01 = bike_type ("Red", "Caloi", 2020, 800)
bike_type_01.beep_bike()
bike_type_01.stop_bike()
bike_type_01.to_run()
print(bike_type_01.color)


bike_type_02 = bike_type ("Blue", "Monark", 2000, 500)
bike_type_02.beep_bike()
bike_type_02.stop_bike()







