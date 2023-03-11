import re
regex = re.compile(r'<[^>]+>')
with open('/home/tarunsparrot/tarun_url.txt') as file:
    for link in file:
        url = regex.sub('', link)
        myfile=open(r'/home/tarunsparrot/tarun_urlnohtml.txt','a')
        myfile.write(url)
        print(url)