class Customer:
    def __init__(self,CustomerID, FirstName, LastName, Email, PhoneNumber, Address, Username, Password, RegistrationDate ):
        self.CustomerID = CustomerID
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.PhoneNumber = PhoneNumber
        self.Address = Address
        self.Username = Username
        self.Password = Password
        self.RegistrationDate = RegistrationDate

    @property
    def getCustomerid(self):
        return self.CustomerID

    @getCustomerid.setter
    def setCustomerid(self,newCustomerid):
        self.CustomerID = newCustomerid

    @property
    def getFirstName(self):
        return self.FirstName

    @getFirstName.setter
    def setFirstName(self, newFirstName):
        self.FirstName = newFirstName

    @property
    def getEmail(self):
        return self.Email

    @getEmail.setter
    def setEmail(self, newEmail):
        self.Email = newEmail

    @property
    def getPhoneNumber(self):
        return self.PhoneNumber

    @getPhoneNumber.setter
    def setPhoneNumber(self, newPhoneNumber):
        self.PhoneNumber = newPhoneNumber

    @property
    def getAddress(self):
        return self.Address

    @getAddress.setter
    def setAddress(self, newAddress):
        self.Address = newAddress

    @property
    def getUsername(self):
        return self.Username

    @getUsername.setter
    def setUsername(self, newUsername):
        self.Username = newUsername

    @property
    def getRegistrationDate(self):
        return self.RegistrationDate

    @getRegistrationDate.setter
    def setUsername(self, newRegistrationDate):
        self.RegistrationDate= newRegistrationDate



    def Authenticate(self,password):
        if self.Password == password:
            return True


