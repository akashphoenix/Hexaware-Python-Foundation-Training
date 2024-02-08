from exception.CustomExceptions import DatabaseConnectionException
from dao.CustomerService import CustomerService
from dao.VehicleService import VehicleService
from dao.ReservationService import ReservationService

def MainMenuCustomer():
    print("1. Get customer by customerID")
    print("2. Register Customer")
    print("3. update customer")
    print("4. Delete Customer")
    print("0. Exit from Customer")
def MainMenuVehicle():
    print("1. Get vehicle by VehicleID")
    print("2. Get available Vehicle ")
    print("3. Add Vehicle")
    print("4. Update Vehicle")
    print("5. Remove Vehicle")
    print("0. Exit from Vehicle")
def MainMenuReservation():
    print("1. Get Reservation by ReservationID ")
    print("2. create Registration ")
    print("3. update Registration ")
    print("4. Cancel Registration")
    print("0. Exit from Registration ")

def main():
    while True:
        print("---Welcome to CarConnect---")
        print("Choose Categories")
        print("1. Customer")
        print("2. Vehicle")
        print("3. Registration")
        print("9. to exit")
        option =int(input("Enter Category "))
        if option == 1:
            cus = CustomerService("localhost","root","shree420","carconnect")
            try:
                cus.connect()
            except DatabaseConnectionException:
                print("error")
            while True:
                print("choose the functionality")
                MainMenuCustomer()
                option = int(input("Enter the option number which are given above "))
                if option == 1:
                    cus.GetCustomerById()
                elif option == 2:
                    cus.RegisterCustomer()
                elif option == 3:
                    cus.UpdateCustomer()
                elif option == 4:
                    cus.DeleteCustomer()
                elif option == 0:
                    cus.disconnect()
                    break

        if option == 2:
            veh = VehicleService("localhost","root","shree420","carconnect")
            veh.connect()
            while True:
                print("choose the functionality")
                MainMenuVehicle()
                option = int(input("Enter the option number which are given above "))
                if option == 1:
                    veh.GetVehicleById()
                elif option == 2:
                    veh.GetAvailableVehicles()
                elif option == 3:
                    veh.AddVehicle()
                elif option == 4:
                    veh.UpdateVehicle()
                elif option == 5:
                    veh.RemoveVehicle()
                elif option == 0:
                    break


        if option == 3:
            res = ReservationService("localhost","root","shree420","carconnect")
            res.connect()
            while True:
                print("choose the functionality")
                MainMenuReservation()
                option = int(input("Enter the option number which are given above "))
                if option == 1:
                    res.GetReservationById()
                elif option == 2:
                    res.CreateReservation()
                elif option == 3:
                    res.UpdateReservation()
                elif option == 4:
                    res.CancelReservation()
                elif option == 0:
                    break
        if option == 9:
            print("Logging Out......")
            break

if __name__ == "__main__":
    main()




