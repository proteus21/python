import openai
openai.api_key ='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'

def get_response(message):
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages  = [
        { 'role':'user','content' : message}])
    return response.choices[0]["message"]["content"] #-> you can directly add the message variable as the users content property.