import pywhatkit  # in order the library to work Flask should also be installed

# sending message instantly
def send_instant():
    destination_num = input('Enter the number where to send: ')
    message = input('enter the text: ')

    pywhatkit.sendwhatmsg_instantly(destination_num, message)

    
# programming to send the message
def send_later():
    destination_num = input('Enter the number where to send: ')
    message = input('enter the text: ')
    hour = int(input('enter hours'))
    minutes = int(input('enter minutes'))
    pywhatkit.sendwhatmsg(phone_no=destination_num, message=message, time_hour=hour, time_min=minutes)



 def main():
     send_instant()


 if __name__ == '__main__':
    main()
