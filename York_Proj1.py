# INF 120-004
# Project 1
# Casey York
# September 5, 2016

def calculator():
  tax = .08
  showInformation("This program will help you calculate your restaurant tab.")

  # Gathering info to calculate restaurant tab
  giftCertificate = requestNumber("How much is your gift certificate?")
  appetizerPerson1 = requestNumber("How much was the first person\'s appetizer?")
  entreePerson1 = requestNumber("How much was the first person\'s entree?")
  drinkPerson1 = requestNumber("How much was the first person\'s drink?")
  totalPerson1 = appetizerPerson1 + entreePerson1 + drinkPerson1
  appetizerPerson2 = requestNumber("How much was the second person\'s appetizer?")
  entreePerson2 = requestNumber("How much was the second person\'s entree?")
  drinkPerson2 = requestNumber("How much was the second person\'s drink?")
  totalPerson2 = appetizerPerson2 + entreePerson2 + drinkPerson2

  # Calculating the final amount due
  total = round(totalPerson1 + totalPerson2, 2)
  tabTax = round(total * tax, 2)
  tab = round(total + tabTax, 2)
  amountDue = round(tab - giftCertificate, 2)
  
  # Printing the customer's bill
  printNow("Your order total is $" + str(total) + ".")
  printNow("Your tax is $" + str(tabTax) + ".")
  printNow("The total of your tab is $" + str(tab) + ".")
  printNow("Your amount due is $" + str(amountDue) + ".")
  