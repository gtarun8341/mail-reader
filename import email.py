import email
import imaplib
print("started")
mail = imaplib.IMAP4_SSL('imap.gmail.com')
print(mail)
(retcode, capabilities) = mail.login('gmail','password')
print("connected mail")
mail.list()
print("connected mail")
mail.select('inbox')
n=0
(retcode, messages) = mail.search(None, '(UNSEEN)')
if retcode == 'OK':
    for num in messages[0].split() :
        print ('Processing ')
        n=n+1
        typ, data = mail.fetch(num,'(RFC822)')
        for response_part in data:
            if isinstance(response_part, tuple):
                original = email.message_from_bytes(response_part[1])

                print(original['From'])
                print(original['Subject'])
                raw_email = data[0][1]
                raw_email_string = raw_email.decode('utf-8')
                email_message = email.message_from_string(raw_email_string)
                
                for part in email_message.walk():
                    
                    print('for')
                    if (part.get_content_type() == "text/html"): # ignore attachments/html
                        print('if')
                        body = part.get_payload(decode=True)
                        
                        #save_string = str(r"/home/tarunsparrot/tarun_" + str('body') + ".txt" )
                        myfile=open(r'/home/tarunsparrot/tarun_body.txt','a')
                        print('file')
                        #myfile = open(save_string, 'a')
                        #myfile.write(original['From']+'\n')
                        #myfile.write(original['Subject']+'\n')            
                        myfile.write(body.decode('utf-8'))
                        myfile.write('**********\n')
                        myfile.close()
                    else:
                        continue
        typ, data = mail.store(num,'+FLAGS','\\Seen')

print (n)