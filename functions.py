def calculate_discount(original_price,discount_percentage):
    if discount_percentage >= 20:
     discount_amount = original_price * (discount_percentage/100)
     final_price = original_price - discount_amount
     return final_price
    else:
     return original_price
    
original_price = float(input("Enter the original price of the item:"))
discount_percentage = float(input("Enter the discount percentage:"))

final_price = calculate_discount (original_price,discount_percentage)

if final_price!= original_price:
  print ( "The final price is after applying a {}% discount is : KSH{}" .format(discount_percentage , final_price))
else:
  print ("No discount applied. The original price remains : KSH {}".format(final_price))



