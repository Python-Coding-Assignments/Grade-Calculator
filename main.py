import Constants.constant as constant

#declarations and initializations of variables
assignptsmade = 0
midtermptsmade = 0
revelptsmade = 0
attendptsmade = 0
finalptsmade = 0
courseGrade = 0
extraCredit = letterGrade = "null"
extraptsmade = 0
A = B = C = D = E = 0

#getting user input for number of points earned for each assignment
assignptsmade = float(input("Assignment Points Made: "))
midtermptsmade = float(input("Midterm Points Made: "))
revelptsmade = float(input("Revel Points Made: "))
attendptsmade = float(input("Attendance Points Made: "))
finalptsmade = float(input("Score on the Final Assignment: "))
extraCredit = input("Did you earn extra credit? (y/n): ")

#conditional statement if the user selected that he/she earned extra credit
if extraCredit == "Y" or extraCredit == "y":
    #getting user input for number of extra credit points earned
    extraptsmade = float(input("Extra Credit points Made: "))
    #adding extra credit points to total assignment points
    assignptsmade += extraptsmade

#conditional statement if user did not enter Y, y, N, or n
if extraCredit != "Y" and extraCredit != "y" and extraCredit != "N" and extraCredit != "n":
    print("\nInvalid option, exiting program.")
#conditional statement if user either entered Y, y, N, or n    
else:
    #calculating percentage grade for each attribute
    A = ((assignptsmade / constant.ASSIGNPTSPOSS) * 0.4)
    B = ((midtermptsmade / constant.MIDTERMPTSPOSS) * 0.25)
    C = ((revelptsmade / constant.REVELPTSPOSS) * 0.1)
    D = ((attendptsmade / constant.ATTENDPTSPOSS) * 0.1)
    E = ((finalptsmade / constant.FINALPTSPOSS) * 0.15)
    #calculating the final course grade
    courseGrade = (A + B + C + D + E) * 100

    #conditional statement if course grade is greater than or equal to 90
    if courseGrade >= 90:
        letterGrade = "A"
    #conditional statement if course grade is greater than or equal to 80 and less than 90    
    elif courseGrade >= 80 and courseGrade < 90:
        letterGrade = "B"
    #conditional statement if course grade is greater than or equal to 70 and less than 80
    elif courseGrade >= 70 and courseGrade < 80:
        letterGrade = "C"
    #conditional statement if course grade is greater than or equal to 60 and less than 70    
    elif courseGrade >= 60 and courseGrade < 70:
        letterGrade = "D"
    #conditional statement if course grade is less than 60    
    else:
        letterGrade = "F"

    #printing final course grade to user
    print("\nFinal Course Average: " + str("{:.1f}".format(courseGrade)) + "%")
    print("Final Course Letter Grade: " + letterGrade)