class Admin:
    def __init__(self, AdminID, FirstName, LastName, Email, PhoneNumber, Username, Password, Role, JoinDate):
        self.AdminID = AdminID
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.PhoneNumber = PhoneNumber
        self.Username = Username
        self.Password = Password
        self.Role = Role
        self.JoinDate = JoinDate

    @property
    def getAdminID(self):
        return self.AdminID
    @getAdminID.setter
    def setAdminID(self,newAdminID):
        self.AdminID = newAdminID

    @property
    def getFirstName(self):
        return self.FirstName

    @getFirstName.setter
    def setFirstName(self, newFirstName):
        self.FirstName = newFirstName

    @property
    def getLastName(self):
        return self.LastName

    @getLastName.setter
    def setLastName(self, newLastName):
        self.LastName = newLastName

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
    def getUsername(self):
        return self.Username

    @getUsername.setter
    def setUsername(self, newUsername):
        self.Username = newUsername

    @property
    def getRole(self):
        return self.Role

    @getRole.setter
    def setRole(self, newRole):
        self.Role = newRole

    @property
    def getJoinDate(self):
        return self.Role

    @getJoinDate.setter
    def setJoinDate(self, newJoinDate):
        self.JoinDate = newJoinDate

    def Authenticate(self,password):
        if self.password == password:
            return True