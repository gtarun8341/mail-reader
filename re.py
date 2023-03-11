import re
import webbrowser
 
with open("/home/tarunsparrot/tarun_body.txt") as file:
        for line in file:
            urls = re.findall('https://clicksgenie.com/user/earn/surf.aspx.*', line)
            #urls = re.findall('https://volutic.com/user/earn/surf.aspx.*', line)
            save_string = (r"/home/tarunsparrot/tarun_" + str('url') + ".txt" )
            if len(urls)>0:
                myfile = open(save_string, 'a')
                myfile.write('\n'+str(*urls)+'\n')
                myfile.close()
                print(*urls)
                
