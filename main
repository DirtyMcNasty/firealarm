from email import *
from time import *
from gpio import *

def onEmailSend(status):
	print("send status: " + str(status))

def main():
	EmailClient.setup(
		"alarm@paytech.com",
		"172.16.8.5",
		"alarm",
		"pass123"
	)

	EmailClient.onSend(onEmailSend)
	user="vodstvo1@paytech.com";
	
	pinMode(0, INPUT)
	pinMode(1, OUT)
	pinMode(2, OUT)
	pinMode(3, OUT)
	print("Fire Detection")
	while True:
		monitor = digitalRead(0);
		print("Detection", monitor);
		if (monitor>=1):
			customWrite(1, '1');
			digitalWrite(2, HIGH);
			customWrite(3,"FIRE");
			customWrite(4, '1');
			EmailClient.send(user, "Fire", "Fire alarm");
			print ("FIRE");
			delay(1000);
		else:
			customWrite(1, '0');
			digitalWrite(2, LOW);
			customWrite(3,"STATUS: OK");
			customWrite(4, '0');
			print ("STATUS OK");
			delay(1000)
	
if __name__ == "__main__":
	main()
