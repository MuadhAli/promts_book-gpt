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
        presence_penalty=0
        
    print(response)
    
query = 'AI'  
bookdesription(query):
            