# Keylogger:

A keylogger is a type of surveillance technology used to monitor and record each keystroke 
typed on a specific computer's keyboard. Keyloggers are often used as a spyware tool by 
cybercriminals to steal personally identifiable information (PII), login credentials and
sensitive enterprise data.

## pynput:

pynput is the library of Python that allows us to control mouse and keyboard. The package
'pynput.keyboard' contains classes for controlling and monitoring the keyboard. This allows
us to capture keyboard inputs which makes it useful for making keyloggers.

To install pynput type the below command in the terminal:

		pip install pynput 
	
## Threading:		
Threading module is used for creating, controlling and managing threads in python. 
Following is the syntax for the Timer class constructor:

		threading.Timer(interval, function, args=[], kwargs={})
		
- Methods of Timer class:

In the Timer class we have two methods used for starting and cancelling the execution of the timer object.
- start() method: This method is used to start the execution of the timer object. When we call this method, then the timer object starts its timer.
- cancel() method: This method is used to stop the timer and cancel the execution of the timer object's action. This will only work if the timer has not performed its action yet.

## smtplib:

Simple Mail Transfer Protocol (SMTP) is a protocol, which handles sending e-mail and 
routing e-mail between mail servers. Python provides smtplib module, which defines an
SMTP object that can be used to send mail to any Internet machine.

An SMTP object has an instance method called sendmail, which is typically used to do the
work of mailing a message. It takes three parameters −

- The sender − A string with the address of the sender.
- The receivers − A list of strings, one for each recipient.
- The message − Information which is to be mailed.
		
		server.login(sender_email_id, sender_email_password)
		server.sendmail(sender_email_id, receiver_email_id, message)


- starttls() is a command that tells email server that email client wants to turn existing
insecure connection into a secure one.

On the receiver account make sure to give permission for receiving mails from less secure 
apps also.

### Note:
- The program has been tested on windows and linux with python2.7 and python3.8.
- Dont misuse the program.