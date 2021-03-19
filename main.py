import datetime
import os
import csv
import json
import ast

print("Welcome to Mini Cooking Recipe Generator and Calorie Tracking System")
fileSize = os.path.getsize("userinformation.txt")
if fileSize != 0:
    with open("userInformation.txt", "r") as file:
        usrDB = file.read()
    allUsers = ast.literal_eval(usrDB)
    file.close()


def option2(Name):
    print("please select your operation number")
    print("1. Edit profile")
    print("2. Delete profile")
    menu2 = input()
    if menu2 == "1":
        print("which value do you wish to edit")
        print("1. Name")
        print("2. date of birth")
        print("3. gender")
        print("4. height(m)")
        print("5. weight(kg)")
        print("6. activity level")
        print("7. allergies")
        menu3 = input()
        if menu3 == "1":
            print("enter New name")
            new_name = input()
            Profile.update({"Name": new_name})
            Profile.update({"Edit date": str(datetime.datetime.today())})
            allUsers[new_name] = allUsers.pop(Name)
            save = allUsers
            with open('userinformation.txt', 'w') as writeFile:
                writeFile.write(json.dumps(save))
                writeFile.close()
        elif menu3 == "2":
            print("enter New date of birth")
            DOM = input()
            DOM = datetime.datetime.strptime(DOM, "%d/%m/%Y").date()
            currentDate = datetime.datetime.today().date()
            age = currentDate.year - DOM.year
            if (currentDate.month - DOM.month) < 0:
                age -= 1
            elif (currentDate.month - DOM.month) == 0 and (currentDate.day - DOM.day) < 0:
                age -= 1
            gender = Profile.get("gender")
            weight = Profile.get("weight")
            height = Profile.get("height")
            AL = Profile.get("activity")
            if gender == "f" or gender == "F":
                BMR = 655.1 + (9.563 * float(weight)) + (1.85 * float(height) * 100) - (4.676 * age)
            elif gender == "m" or gender == "M":
                BMR = 66.47 + (13.75 * float(weight)) + (5.003 * float(height) * 100) - (6.755 * age)
            TEE = BMR * AL
            BMR = format(BMR, '.2f')
            TEE = format(TEE, '.2f')
            Profile.update({"date of birth": str(DOM)})
            Profile.update({"age": age})
            Profile.update({"BMR": BMR})
            Profile.update({"TEE": TEE})
            Profile.update({"Edit date": str(datetime.datetime.today())})
            save = allUsers
            with open('userinformation.txt', 'w') as writeFile:
                writeFile.write(json.dumps(save))
                writeFile.close()
        elif menu3 == "3":
            print("enter New gender (M/F)")
            genderN = input()
            weight = Profile.get("weight")
            height = Profile.get("height")
            AL = Profile.get("activity")
            age = Profile.get("age")
            if genderN == "m" or genderN == "M" or genderN == "F" or genderN == "f":
                if genderN == "f" or genderN == "F":
                    BMR = 655.1 + (9.563 * float(weight)) + (1.85 * float(height) * 100) - (4.676 * age)
                elif genderN == "m" or genderN == "M":
                    BMR = 66.47 + (13.75 * float(weight)) + (5.003 * float(height) * 100) - (6.755 * age)
                TEE = BMR * AL
                BMR = format(BMR, '.2f')
                TEE = format(TEE, '.2f')
                Profile.update({"gender": genderN})
                Profile.update({"BMR": BMR})
                Profile.update({"TEE": TEE})
                Profile.update({"Edit date": str(datetime.datetime.today())})
                write = allUsers
                with open('userinformation.txt', 'w') as writeFile:
                    writeFile.write(json.dumps(write))
                    writeFile.close()
        elif menu3 == "4":
            print("enter New Height in meters")
            heightN = input()
            weight = Profile.get("weight")
            AL = Profile.get("activity")
            gender = Profile.get("gender")
            age = Profile.get("age")
            BMI = float(weight) / (float(heightN) ** 2)
            BMIrange = ""
            if BMI < 18.5:
                BMIrange = "underweight"
            elif 24.9 > BMI >= 18.5:
                BMIrange = "normal"
            elif 29.9 >= BMI >= 25:
                BMIrange = "overweight"
            elif BMI >= 30.0:
                BMIrange = "obese"
            if gender == "m" or gender == "M" or gender == "F" or gender == "f":
                if gender == "f" or gender == "F":
                    BMR = 655.1 + (9.563 * float(weight)) + (1.85 * float(heightN) * 100) - (4.676 * age)
                elif gender == "m" or gender == "M":
                    BMR = 66.47 + (13.75 * float(weight)) + (5.003 * float(heightN) * 100) - (6.755 * age)
            TEE = BMR * AL
            BMR = format(BMR, '.2f')
            BMI = format(BMI, '.2f')
            TEE = format(TEE, '.2f')
            Profile.update({"BMI": BMI})
            Profile.update({"BMI range": BMIrange})
            Profile.update({"BMR": BMR})
            Profile.update({"TEE": TEE})
            Profile.update({"height": heightN})
            Profile.update({"Edit date": str(datetime.datetime.today())})
            save = allUsers
            with open('userinformation.txt', 'w') as writeFile:
                writeFile.write(json.dumps(save))
                writeFile.close()
        elif menu3 == "5":
            print("enter New weight in KG")
            weightN = input()
            AL = Profile.get("activity")
            gender = Profile.get("gender")
            age = Profile.get("age")
            height = Profile.get("height")
            BMI = float(weightN) / (float(height) ** 2)
            BMIrange = ""
            if BMI < 18.5:
                BMIrange = "underweight"
            elif 24.9 > BMI >= 18.5:
                BMIrange = "normal"
            elif 29.9 >= BMI >= 25:
                BMIrange = "overweight"
            elif BMI >= 30.0:
                BMIrange = "obese"
            if gender == "m" or gender == "M" or gender == "F" or gender == "f":
                if gender == "f" or gender == "F":
                    BMR = 655.1 + (9.563 * float(weightN)) + (1.85 * float(height) * 100) - (4.676 * age)
                elif gender == "m" or gender == "M":
                    BMR = 66.47 + (13.75 * float(weightN)) + (5.003 * float(height) * 100) - (6.755 * age)
            TEE = BMR * AL
            BMR = format(BMR, '.2f')
            BMI = format(BMI, '.2f')
            TEE = format(TEE, '.2f')
            Profile.update({"BMI": BMI})
            Profile.update({"BMI range": BMIrange})
            Profile.update({"BMR": BMR})
            Profile.update({"TEE": TEE})
            Profile.update({"weight": weightN})
            Profile.update({"Edit date": str(datetime.datetime.today())})
            save = allUsers
            with open('userinformation.txt', 'w') as writeFile:
                writeFile.write(json.dumps(save))
                writeFile.close()
        elif menu3 == "6":
            print("enter you New desired activity level")
            ALS = {"1": 1.2, "2": 1.375, "3": 1.55, "4": 1.725, "5": 1.9}
            print("Please choose your preferred activity level (Enter a Number)")
            print("1. Little/No exercise")
            print("2. Light exercise")
            print("3. Moderate exercise (2-3 days a week)")
            print("4. very active (6-7 days a week)")
            print("5. Extra active (very active and physical job)")
            activity = input()
            AL = float(ALS.get(activity))
            print(type(AL))
            BMR = float(Profile.get("BMR"))
            print(type(BMR))
            TEE = BMR * AL
            Profile.update({"activity": AL})
            Profile.update({"TEE": TEE})
            Profile.update({"Edit date": str(datetime.datetime.today())})
            save = allUsers
            with open('userinformation.txt', 'w') as writeFile:
                writeFile.write(json.dumps(save))
                writeFile.close()
        elif menu3 == "7":
            allergies = Profile.get("allergies")
            print("do you want to add (1) or delete (2) an allergy")
            allergychoice = input()
            if allergychoice == "1":
                print("enter the number of the allergy or -1 if you want to exit")
                with open('ingredients.csv') as csvfile:
                    ingredientsList = csv.reader(csvfile, delimiter=';')
                    for row in ingredientsList:
                        print(((16 - int(len(row[0]))) * '-').join(row))
                csvfile.close()
                allergyNo = input()
                if allergyNo != "-1":
                    while True:
                        with open('ingredients.csv') as csvfile:
                            ingredientsList = csv.reader(csvfile, delimiter=';')
                            for row in ingredientsList:
                                for field in row:
                                    if field == allergyNo:
                                        allergy = row[0]
                                        allergies.append(allergy)
                        csvfile.close()
                        print("enter the ingredient number")
                        allergyNo = input()
                        if allergyNo == "-1":
                            break
                print(allergies)
                Profile.update({"allergies": allergies})
                Profile.update({"Edit date": str(datetime.datetime.today())})
                save = allUsers
                with open('userinformation.txt', 'w') as writeFile:
                    writeFile.write(json.dumps(save))
                    writeFile.close()
            if allergychoice == "2":
                while True:
                    print("Please choose the allergy you want to delete (Name of ingredient) or -1 to finalize edits")
                    print(allergies)
                    delete_allergy = input()
                    if delete_allergy == "-1":
                        break
                    for i in allergies:
                        if delete_allergy == i:
                            allergies.remove(i)
                    print(allergies)
                Profile.update({"allergies": allergies})
                Profile.update({"Edit date": str(datetime.datetime.today())})
                save = allUsers
                with open('userinformation.txt', 'w') as writeFile:
                    writeFile.write(json.dumps(save))
                    writeFile.close()

    if menu2 == "2":
        del allUsers[Name]
        save = allUsers
        with open('userinformation.txt', 'w') as writeFile:
            writeFile.write(json.dumps(save))
            writeFile.close()

    pass


def userValidation():
    print("enter the name of your user")
    Name = input()
    if allUsers.get(Name) == None:
        print("user does not exist")
        userValidation()
    print("is this your user? (y/n)")
    print_view = allUsers.get(Name)
    PV_name = print_view.get("Name")
    PV_gender = print_view.get("gender")
    PV_height = print_view.get("height")
    PV_weight = print_view.get("weight")
    PV_DOM = print_view.get("date of birth")
    PV_age = print_view.get("age")
    PV_BMI = print_view.get("BMI")
    PV_BMIR = print_view.get("BMI range")
    PV_BMR = print_view.get("BMR")
    PV_activity = print_view.get("activity")
    PV_TEE = print_view.get("TEE")
    PV_JD = print_view.get("join Date")
    PV_ED = print_view.get("Edit date")
    PV_allergies = print_view.get("allergies")
    print(f"Name : {PV_name}")
    if PV_gender == "m" or PV_gender == "M":
        print("gender : Male")
    elif PV_gender == "f" or PV_gender == "F":
        print(f"gender : Female")
    print(f"height : {PV_height} meter(s)")
    print(f"weight : {PV_weight} KG")
    print(f"Date of birth : {PV_DOM}")
    print(f"age : {PV_age}")
    print(f"BMI : {PV_BMI}")
    print(f"BMI range : {PV_BMIR}")
    print(f"BMR : {PV_BMR}")
    print(f"activity level : {PV_activity}")
    print(f"TEE : {PV_TEE}")
    print(f"join date : {PV_JD}")
    print(f"allergies: {PV_allergies}")
    if PV_ED != None:
        print(f"edit date : {PV_ED}")
    valid = input()
    if valid == "y" or valid == "Y":
        Profile = allUsers.get(Name)
        return Profile, Name
        pass
    elif valid == "n" or valid == "N":
        userValidation()
    pass


def option1():
    ALS = {"1": 1.2, "2": 1.375, "3": 1.55, "4": 1.725, "5": 1.9}  # activity level selector
    print("Enter your desired user name")
    Name = input()
    print("Enter your body weight in Kilograms")
    weight = input()
    print("Enter your height in meters")
    height = input()
    print("Enter your birth date (dd/mm/yyyy)")
    DOM = input()
    print("Enter you gender (M/F)")
    gender = input()
    DOM = datetime.datetime.strptime(DOM, "%d/%m/%Y").date()
    currentDate = datetime.datetime.today().date()
    age = currentDate.year - DOM.year
    if (currentDate.month - DOM.month) < 0:
        age -= 1
    elif (currentDate.month - DOM.month) == 0 and (currentDate.day - DOM.day) < 0:
        age -= 1
    BMI = float(weight) / (float(height) ** 2)
    if BMI < 18.5:
        BMIrange = "underweight"
    elif 24.9 > BMI >= 18.5:
        BMIrange = "normal"
    elif 29.9 >= BMI >= 25:
        BMIrange = "overweight"
    elif BMI >= 30.0:
        BMIrange = "obese"
    if gender == "f" or gender == "F":
        BMR = 655.1 + (9.563 * float(weight)) + (1.85 * float(height) * 100) - (4.676 * age)
    elif gender == "m" or gender == "M":
        BMR = 66.47 + (13.75 * float(weight)) + (5.003 * float(height) * 100) - (6.755 * age)
    print("Please choose your preferred activity level (Enter a Number)")
    print("1. Little/No exercise")
    print("2. Light exercise")
    print("3. Moderate exercise (2-3 days a week)")
    print("4. very active (6-7 days a week)")
    print("5. Extra active (very active and physical job)")
    AL = ALS.get(input())
    TEE = BMR * AL
    print("please enter the number of ingredients in case of allergies OR enter -1 if you have none/stop entering")
    allergies = []
    with open('ingredients.csv') as csvfile:
        ingredientsList = csv.reader(csvfile, delimiter=';')  # assigning the csv file to a LIST view
        for row in ingredientsList:
            print(((16 - int(len(row[0]))) * '-').join(row))  # row[0]
    csvfile.close()
    allergyNo = input()
    if allergyNo != "-1":
        while True:
            with open('ingredients.csv') as csvfile:
                ingredientsList = csv.reader(csvfile, delimiter=';')
                for row in ingredientsList:
                    for number in row:
                        if number == allergyNo:
                            allergy = row[0]  # creates a variable of type string that contains ingredient name
                            allergies.append(allergy)
            csvfile.close()
            print("enter the ingredient number")
            allergyNo = input()
            if allergyNo == "-1":
                break
    joinDate = currentDate
    with open("userInformation.txt", "r") as userFile:
        usrDB = userFile.read()
        userFile.close()
    BMR = format(BMR, '.2f')  # force float point
    BMI = format(BMI, '.2f')
    TEE = format(TEE, '.2f')
    if fileSize != 0:
        ProfileDetails = ast.literal_eval(usrDB)
        ProfileDetails[Name] = {"join Date": str(joinDate), "Name": Name, "gender": gender, "height": height,
                                "weight": weight,
                                "date of birth": str(DOM), "age": age, "BMI": BMI, "BMI range": BMIrange,
                                "BMR": BMR,
                                "activity": AL, "TEE": TEE, "allergies": allergies}
    elif fileSize == 0:
        ProfileDetails = {}
        ProfileDetails[Name] = {"join Date": str(joinDate), "Name": Name, "gender": gender, "height": height,
                                "weight": weight,
                                "date of birth": str(DOM), "age": age, "BMI": BMI, "BMI range": BMIrange,
                                "BMR": BMR,
                                "activity": AL, "TEE": TEE, "allergies": allergies}
    write = ProfileDetails
    Profile = ProfileDetails.get(Name)
    with open('userinformation.txt', 'w') as appendF:
        appendF.write(json.dumps(write))
        appendF.close()
    return Profile
    pass


while True:
    print("Select the number of your desired task")
    print("1. create or load a new user profile")
    print("2. edit or delete existing user profile")
    print("3. view user profile")
    print("4. Generate recipe recommendations for the session")
    print("5. View user meals and generate health information")
    print("6. Exit the program")
    choice = input()
    if choice == "1":
        print("do you have an existing user? (y/n)")
        exists = input()
        if exists == "y" or exists == "Y":
            Profile, Name = userValidation()  # validates user existance
        elif exists == "n" or exists == "N":
            Profile = option1()  # creates user

    if choice == "2":
        Profile, Name = userValidation()
        option2(Name)
    if choice == "3":
        userValidation()
    if choice == "6":
        break
