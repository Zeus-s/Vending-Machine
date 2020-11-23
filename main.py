import easygui

cola = 2.5
aqua = 0.75
sprite = 2.25 
pepsi = 1.75 
gf = 3.5

def main() :
    con = True
    while(con==True) :
        msg = "Hello, Welcome to our Vending Machine! \n Press 'Yes' to continue... "
        title = "Vending Machine"
        choices = ['Yes','No']
        myChoice = easygui.ynbox(msg,title,choices)
        
        if myChoice == 1 :
            msg = "Which drinks do you like to buy?\nPlease click on the button (not the image)..."
            title = "Vending Machine"
            choices = ['Coca-cola','Aqua','Sprite','Pepsi','Greenfield']
            img = ["1.png", "2.png", "3.png","4.png","5.png"]
            choice = easygui.buttonbox(msg,title,image=img,choices=choices)
            if (choice == "Coca-cola" or img == "1.png") :
                need = cola
            elif (choice == "Aqua") :
                need = aqua
            elif (choice == "Sprite") :
                need = sprite
            elif (choice == "Pepsi") :
                need = pepsi
            elif (choice == "Greenfield") :
                need = gf

            msg = "Enter the number of drinks you want to buy : (maximum 5 pieces)"
            title = "Vending Machine"
            sn = easygui.integerbox(msg,title)
            cost = sn*need
            msg = "Please deposit the money : \n Pricelist \n Coca-cola : $2.5 \n Aqua : $0.75 \n Sprite : $2.25 \n Pepsi : $1.75 \n Greenfield : $3.5 \n \n Please input less than $100 \n Cost : $" + str(cost) 
            title = "Vending Machine"
            money = easygui.integerbox(msg,title)

            change = float(money) - cost
            
            if (change>= 0) :
                if (1 > change >= 0) :
                    msg = "Thankyou. Your change is " + str(change) + " cents"
                    title = "Vending Machine"
                    easygui.msgbox(msg,title,ok_button="Exit")
                else :
                    msg = "Thankyou. Your change is $" + str(change) + " dollars."
                    title = "Vending Machine"
                    easygui.msgbox(msg,title,ok_button="Exit")

                    msg = "Would you like to buy again?"
                    title = "Vending Machine"
                    choices = ['Yes','No']
                    cont = easygui.ynbox(msg,title,choices)

                    if cont == 1 :
                        main()
                    else :
                        msg = "Have a good day!"
                        title = "Vending Machine"
                        con = False
                        easygui.msgbox(msg,title,ok_button='Exit')

            else :
                msg = "You didn't deposit enough money, please start again."
                title = "Soda Machine"
                easygui.msgbox(msg,title)
        else :
            msg = "Have a good day!"
            title = "Vending Machine"
            con = False
            easygui.msgbox(msg,title,ok_button='Exit')

if __name__ == "__main__":
    main()