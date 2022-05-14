total = 0
bookingrpt = 0
ticketinput = 0
ticket_type = ["0. Adult","1. Child","2. Senior","3. Family","4. Group>=6"]
type_counts = [0,0,0,0,0]
oneday_price = [20, 12, 16, 60, 15]
twoday_price = [30, 18, 24, 90, 22.5]

ext_attraction = ["0. Lion Feeding", "1. Penguin Feeding", "2. Evening BBQ (Only 2 Day Ticket Holders)"]
att_price = [2.5, 2, 5]
status = 1


print()
print("   Ticket Type\t\t\t\tCost for one day\t\tCost for two days")
for i in range(5):
    print(f"{ticket_type[i]}\t\t\t\t${oneday_price[i]}\t\t\t\t${twoday_price[i]}")

print()
print("Extra attraction""\t\t\t\t"" Cost per person")
for i in range(3):
    print(ext_attraction[i],"\t\t\t\t",att_price[i])

day = input("Enter today's date (1-31): ")
day = int(day)
while(day < 1 and day > 31):
    print("INVALID DATE ENTERED!!!!")
for i in range(7):
    print(day)
    if(day == 31):
        day = 0
    day = day + 1

ticketinput = int(input("Select options from 0 - 4 to book ticket(s) or -1 to end booking: "))
while(ticketinput != -1):
    if(ticket_type == 0):
        adultcount = int(input("Adult count: "))
        type_counts[0] = type_counts[0] + adultcount
    elif(ticket_type == 1):
        childcount = int(input("Child count: "))
        type_counts[1] = type_counts[1] + childcount
    elif(ticket_type == 2):
        seniorcount = int(input("Senior count:"))
        type_counts[2] = type_counts[2] + seniorcount
    
