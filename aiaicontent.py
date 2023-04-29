import openai
import os
import config
openai.api_key=config.OPENAI_API_KEY




def bookdesription(query):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="write a amazon book description for the chapter or paper on :{}".format(query),
        temperature=0.45,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)
    
    
    
    
        
    if 'choices' in response:
        if len(response['choices']) > 0:
            answer = response['choices'][0]['text']
        else:
            answer='u beat the AI'
    else:
            answer ='u beat the AI'   
    print(answer)


query = 'AI'
bookdesription(query)