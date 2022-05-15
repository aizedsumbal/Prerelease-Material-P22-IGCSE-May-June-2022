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
famadults = 0
famchildren = 0
grpadults = 0
grpchildren = 0


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


while(ticketinput != -1):
    ticketinput = int(input("Select options from 0 - 4 to book ticket(s) or -1 to end booking: "))
    if(ticketinput == 0):
        adultcount = int(input("Adult count: "))
        type_counts[0] = type_counts[0] + adultcount
    elif(ticketinput == 1):
        childcount = int(input("Child count: "))
        type_counts[1] = type_counts[1] + childcount
    elif(ticketinput == 2):
        seniorcount = int(input("Senior count:"))
        type_counts[2] = type_counts[2] + seniorcount
    elif(ticketinput == 3):
        familycount = int(input("Family count: "))
        print(f"Maximum adults/senior allowed are {familycount*2}")
        print(f"Maximum children allowed are {familycount*3}")
        adultcount = int(input("Adult or senior count: "))
        childcount = int(input("Child count: "))
        while(familycount < adultcount/2) or (familycount < childcount/3):
            print("You have exceeded the adult/senior count or the child count for the tickets. Please type in details again:")
            familycount = int(input("Family count: "))
            print(f"Maximum adults/senior allowed are {familycount*2}")
            print(f"Maximum children allowed are {familycount*3}")
            adultcount = int(input("Adult or senior count: "))
            childcount = int(input("Child count: "))
        type_counts[3] = type_counts[3] + familycount
        adultcount = famadults
        childcount = famchildren
        print("")
    elif(ticketinput == 4):
        print("Enter tickets more more than or equal to 6.")
        groupcount = int(input("Group count: "))
        while(groupcount < 6):
            print("Group count is less than 6. Adult count and child count numbers add up to less than 6.")
            groupcount = int(input("Group count: "))

        adultcount = int(input("Adult or senior number in the group: "))
        childcount = int(input("Child number in the group: "))
        while(adultcount+childcount != groupcount):
            print("Adults/seniors and children do not add up to the total group size.")
            adultcount = int(input("Adult or senior number in the group: "))
            childcount = int(input("Child number in the group: "))
        grpadults = adultcount
        grpchildren = childcount
        type_counts[4] = type_counts[4] + groupcount
        print("")
