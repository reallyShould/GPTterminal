import os, sys
import openai
import colorama

colorama.init()

openai.api_key = "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"


os.system('cls' if sys.platform == 'win32' else 'clear')

if not os.path.exists('gpt-history.txt'):
    open('gpt-history.txt', 'a+')
else:
    print(open('gpt-history.txt', 'r').read())
    fck = open('gpt-history.txt', 'r').read()

while 1:
    question = input(f"\n{colorama.Back.YELLOW}>>> ")
    if question == 'exit':
        print(colorama.Style.RESET_ALL)
        os.system('cls' if sys.platform == 'win32' else 'clear')
        break
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": question}])

    with open('gpt-history.txt', 'w') as f:
        f.write(f'{fck}\nYou: {question}\nGPT: {chat_completion["choices"][0]["message"]["content"]}')
        f.close()

    #open('gpt-history.txt', 'w').write(f'{fck}\nYou: {question}\nGPT: {chat_completion["choices"][0]["message"]["content"]}')
    print(f"{colorama.Back.GREEN}{chat_completion['choices'][0]['message']['content']}")