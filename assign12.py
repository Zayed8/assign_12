from Car_Package import hellcat
from Car_Package import zonda
from Car_Package import aventador
from Car_Package import tesla
from Car_Package import gtr
from Car_Package import rollsroyce
from Car_Package import supra
class CarMenu():
    try:
        username = str(input("Enter your name : "))
        print("Welcome to Cars menu ",username)
    except ValueError:
        print("Entered Value is Invalid")
    except Exception:
        print("Error Occured! An Exception was raised")
    print()
    print("⫷----MENU----⫸")
    print(" Enter 1 For Hellcat ⪼ \n Enter 2 For Zonda ⪼ \n Enter 3 For Aventador ⪼ \n Enter 4 For Tesla ⪼ \n Enter 5 For Gtr ⪼ \n Enter 6 For Rollsroyce ⪼ \n Enter 7 For Supra ⪼ \n ")
    UserSelectCar = int(input("◥ Enter The Car Number You are Interested In ◤ : "))
    if UserSelectCar == 1:
        print("【 HELLCAT 】")
        print(hellcat.Hellcat.model())
        print(hellcat.Hellcat.price())
        print(hellcat.Hellcat.horsepower())
        print(hellcat.Hellcat.mileage())
        print(hellcat.Hellcat.image())
    elif UserSelectCar == 2:
        print("【 ZONDA 】")
        print(zonda.Zonda.model())
        print(zonda.Zonda.price())
        print(zonda.Zonda.horsepower())
        print(zonda.Zonda.mileage())
        print(zonda.Zonda.image())
    elif UserSelectCar == 3:
        print("【 AVENTADOR 】")
        print(aventador.Aventador.model())
        print(aventador.Aventador.price())
        print(aventador.Aventador.horsepower())
        print(aventador.Aventador.mileage())
        print(aventador.Aventador.image())
    elif UserSelectCar == 4:
        print("【 TESLA 】")
        print(tesla.Tesla.model())
        print(tesla.Tesla.price())
        print(tesla.Tesla.horsepower())
        print(tesla.Tesla.mileage())
        print(tesla.Tesla.image())
    elif UserSelectCar == 5:
        print("【 GTR 】")
        print(gtr.Gtr.model())
        print(gtr.Gtr.price())
        print(gtr.Gtr.horsepower())
        print(gtr.Gtr.mileage())
        print(gtr.Gtr.image())
    elif UserSelectCar == 6:
        print("【 ROLLS ROYCE 】")
        print(rollsroyce.Rollsroyce.model())
        print(rollsroyce.Rollsroyceprice())
        print(rollsroyce.Rollsroyce.horsepower())
        print(rollsroyce.Rollsroyce.mileage())
        print(rollsroyce.Rollsroyce.image())
    elif UserSelectCar == 7:
        print("【 SUPRA 】")
        print(supra.Supra.model())
        print(supra.Supra.price())
        print(supra.Supra.horsepower())
        print(supra.Supra.mileage())
        print(supra.Supra.image())
    else:
        print("Exit☒")
        print("To Exit Press any other number!")
        print("Thanks For Visiting To Our Menu ByeBye....👋")
    try:
        f=open("CarHistory.txt","+at")
    except FileExistsError:
        print("The File dose Not Exits")
    except FileNotFoundError:
        print("Invalid File Entered Check Again!")
    except Exception:
        print("Error Occured! An Exception was raised")
    finally:
        print("Data Entered in CarHistory.txt Successfully!")
    f.write(f"Username : {username} \nCar Selected : {UserSelectCar}")
    