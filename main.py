from car import Car
from driver import Driver
from user import User
from account import Account

if __name__ == "__main__":
    print ("Hola mundo")
    
    car = Car()
    car.id = 123
    car.license = "AAG456"
    car.driver  = "Alonso"
    pasengenger = 5
    
    print(vars(car))
    
    car2 = Car()
    car2.id      = 7
    car2.license = "TDV345"
    car2.driver  = "Julian"
    pasengenger  = "2"
    
    print(vars(car2))
    
    driver = Driver()
    driver.name      = "Jeapiere"
    driver.apellido  = "Lopez"
    driver.direccion = "Av.Maldonado"
    
    print(vars(driver))
    
    user = User()
    user.id         = 8
    user.name       = "Luismi"
    user.email      = "luim.@gamil.com"
    
    print(vars(user))
    
    account = Account()
    account.id          = 1
    account.name        = "Panchito"
    account.document    = 17549846
    account.mail        = "pancho@gma"