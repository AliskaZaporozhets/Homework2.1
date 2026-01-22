price = int (input ("Enter the price, please: "))
discount = (int (input ("Enter the discount (%), please: "))) / 100

price_after_discount = price - (price * discount)

print ("The price with discount is: ", float (price_after_discount))