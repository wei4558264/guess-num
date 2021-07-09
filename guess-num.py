import random
r = random.randint(1,100)
while True:
	guess = input('請猜一個整數:')
	guess = int(guess)
	if guess == r:
		print('你猜對了，真棒!')
		break
	elif guess > r:
		print('太大了!')
	else:
		print('太小了!')

	