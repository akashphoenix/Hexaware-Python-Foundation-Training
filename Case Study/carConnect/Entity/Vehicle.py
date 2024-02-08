class Vehicle:
    def __init__(self,VehicleID, Model, Make, Year, Color, RegistrationNumber, Availability, DailyRate ):
        self.VehicleID = VehicleID
        self.Model =Model
        self.Make = Make
        self.Year = Year
        self.Color = Color
        self.RegistrationNumber = RegistrationNumber
        self.Availability = Availability
        self.DailyRate = DailyRate

    @property
    def getVehicleID(self):
        return self.VehicleID
    @getVehicleID.setter
    def setVehicleID(self,newVehicleID):
        self.VehicleID = newVehicleID

    @property
    def getModel(self):
        return self.Model

    @getModel.setter
    def setModel(self, newModel):
        self.Model = newModel

    @property
    def getMake(self):
        return self.Make

    @getMake.setter
    def setModel(self, newMake):
        self.Make = newMake

    @property
    def getYear(self):
        return self.Year

    @getYear.setter
    def setModel(self, newYear):
        self.Year = newYear

    @property
    def getColor(self):
        return self.Color

    @getColor.setter
    def setColor(self, newColor):
        self.Color = newColor

    @property
    def getRegistrationNumber(self):
        return self.RegistrationNumber

    @getRegistrationNumber.setter
    def setRegistrationNumber(self, newRegistrationNumber):
        self.RegistrationNumber = newRegistrationNumber

    @property
    def getAvailability(self):
        return self.Availability

    @getAvailability.setter
    def setAvailability(self, newAvailability):
        self.Availability = newAvailability

    @property
    def getDailyRate(self):
        return self.DailyRate

    @getDailyRate.setter
    def setColor(self, newDailyRate):
        self.DailyRate = newDailyRate

