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
	monitor = 0;
	while True:
		newValue = digitalRead(0);
		print("Detection", newValue);
		if (newValue>=1):
			customWrite(1, '1');
			digitalWrite(2, HIGH);
			customWrite(3,"FIRE");
			customWrite(4, '1');
			if (newValue!=monitor):
				EmailClient.send(user, "Fire", "Fire alarm");
			print ("FIRE");
			monitor = newValue;
			delay(1000);
		else:
			customWrite(1, '0');
			digitalWrite(2, LOW);
			customWrite(3,"STATUS: OK");
			customWrite(4, '0');
			print ("STATUS OK");
			monitor = newValue;
			delay(1000)

if __name__ == "__main__":
	main()
