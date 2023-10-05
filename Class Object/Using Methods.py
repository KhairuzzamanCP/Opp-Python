def call():
    print('calling someone i dont know')
    return 'call done'

class Phone:
    price = 20000;
    model = 'mi 10 pro'
    color = 'blue'
    features =['cammera','speaker','watetproved']
    
    def call(self):
        print('calling one persion')

    def send_sms(self,phone, sms):
        text =f'Sending Sms to:{phone} and message:{sms}'
        return text
my_phone = Phone()
print(my_phone.features)
my_phone.call()
result = my_phone.send_sms(41524,'I forgot to miss you')
print(result)