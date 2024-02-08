class Reservation:
    def __init__(self,ReservationID, CustomerID, VehicleID, StartDate, EndDate, TotalCost, Status):
        self.ReservationID = ReservationID
        self.CustomerID = CustomerID
        self.VehicleID = VehicleID
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.TotalCost = TotalCost
        self.Status = Status

    @property
    def getReservaionID(self):
        return self.ReservationID

    @getReservaionID.setter
    def setReservaionID(self,newReservaionID):
        self.ReservationID = newReservaionID

    @property
    def getCustomerID(self):
        return self.CustomerID

    @getCustomerID.setter
    def setReservaionID(self, newCustomerID):
        self.CustomerID = newCustomerID

    @property
    def getVehicleID(self):
        return self.VehicleID

    @getVehicleID.setter
    def setVehicleID(self, newVehicleID):
        self.VehicleID = newVehicleID

    @property
    def getStartDate(self):
        return self.StartDate

    @getStartDate.setter
    def setStartDate(self, newStartDate):
        self.StartDate = newStartDate

    @property
    def getEndDate(self):
        return self.EndDate

    @getEndDate.setter
    def setEndDate(self, newEndDate):
        self.EndDate = newEndDate

    @property
    def getTotalCost(self):
        return self.TotalCost

    @getTotalCost.setter
    def setTotalCost(self, newTotalCost):
        self.TotalCost = newTotalCost

    @property
    def getStatus(self):
        return self.Status

    @getStatus.setter
    def setStatus(self, newStatus):
        self.Status = newStatus


    def CalculateTotalCost(self):
        return self.TotalCost