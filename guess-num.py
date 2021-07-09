import random
start = input('請輸入你想猜數字的起始值：')
start = int(start)
end= input('請輸入你想猜數字的終點值：')
end = int(end)
r = random.randint(start,end)
guess_time = 1
while True:
	guess = input('請猜一個整數:')
	guess = int(guess)
	if guess == r:
		print('你猜對了，真棒!')
		print('你總共猜',guess_time,'次')
		break
	elif guess > r:
		print('太大了!')
		guess_time = guess_time +1
	else:
		print('太小了!')
		guess_time = guess_time +1

	