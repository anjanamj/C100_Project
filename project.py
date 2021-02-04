class ATM(object):
  """
    blueprint for ATM
  """

  def __init__(self, card_num, pin_num):
    self.card_num = card_num
    self.pin_num = pin_num
    

  def cashWithdraw(self):
    print("Enter the amout you want to withdraw")

  def balanceEnquiry(self):
    print("You are a millionaire")

  


my_details = ATM("1234567890", "1234")

print(my_details.card_num)
print(my_details.pin_num)
print(my_details.cashWithdraw())
print(my_details.balanceEnquiry())


