pocketMoney=int(input("Please enter your Pocket Money/month."))

if(pocketMoney > 1000):
	print("You are a rich kid.")
elif(pocketMoney > 500 and pocketMoney < 1000):
	print("You have a satisfactory life.")
else:
	print("You are a poor.")