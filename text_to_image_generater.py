import webbrowser

import requests
from monsterapi import client

api_key='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Ijg0NjAzMjkwMTEyZjA3YWNhYjRlNWQyOTU1NjM1OGVjIiwiY3JlYXRlZF9hdCI6IjIwMjUtMDctMTBUMTc6MTc6MTIuOTI0OTU0In0.cpZNmSyuBWOr2viHoixN6lWFplE6dTpAoLfdQbBYpPw'

monster_client=client(api_key)

prompt=input("write a prompt to generate the image:")

model='txt2img'

input_data={
    'prompt':f'{prompt}',
    'negprompt':'bad anatomy',
    'sample':1,
    'steps':50,
    'aspect_ratio':'square',
    'guidance_scale':7.5,
    'seed':'2414'
}

result=monster_client.generate(model, input_data)

img_url=result['output'][0]

file_name='generated_image.jpg'

response=requests.get(img_url)

if response.status_code==200:
    with open(file_name,'wb')as file:
        file.write(response.content)
    print("image downloaded")
    
    webbrowser.open(file_name)
else:
    print('failed to download')