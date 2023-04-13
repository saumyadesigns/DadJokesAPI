import requests,json
import ctypes

def callMyAPI():
    url = "https://dad-jokes.p.rapidapi.com/random/joke"
    needed={'x-rapidapi-host': "dad-jokes.p.rapidapi.com",'x-rapidapi-key': "ff6d99cd57msh95f1e85427b96dap18e3cbjsn58736e56c0d6"}
    response=requests.request("GET",url,headers=needed)

    if response.status_code==200:     
        out=response.text
        f=json.loads(out)
        temp=f['body'][0]['setup']
        temp=temp+"\n\n"+f['body'][0]['punchline']
        ctypes.windll.user32.MessageBoxW(0, temp, 'Dad Joke!', 0x00001000) #pop-up window for dad joke
        # ctypes.windll.user32.MessageBoxW(0,"Dad Joke Punchline", "Dad Joke Setup", 0x00001000 )
        # print(f['body'][0]['setup'])
        # print(f['body'][0]['punchline'])
        
        # print('XD so funnayy')
    else:
        print('Request failed :',response.status_code)
# callMyAPI()