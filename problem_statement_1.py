def bdjplan(totalbdj,expenses):
    totalExpens = sum(expenses)
    totalbdj = totalbdj
    if totalbdj > totalExpens:
        remainAmt = totalbdj-totalExpens
        print("total spent amount :",totalExpens)
        print("remaining budget :",remainAmt)
    else:
        print("your montly income is not sufficient for all expenses.")
    


totalbdj = int(input("please enter your total budget :"))
rent = int(input("please enter your rent : "))
food = int(input("please enter your food : "))
transportation = int(input("please enter your transportation : "))
entertainment = int(input("please enter your entertainment : "))

expenses = [rent,food,transportation,entertainment]
bdjplan(totalbdj,expenses)