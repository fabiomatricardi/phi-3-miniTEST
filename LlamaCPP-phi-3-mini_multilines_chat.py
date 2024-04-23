"""


### THIS GGUF has already the CHAT TOKENIZER IMPlEMENTED!
### MISSING: to add multi line support and chat history limiter - it has only 32K tokens context window THOUGH...
"""
from llama_cpp import Llama
import random
import string
import sys

modpath = "model/Phi-3-mini-4k-instruct-q4.gguf"
client = Llama(
        model_path=modpath,
        n_gpu_layers=0,
        n_ctx=4096, #but it has also a 128K variant!
        verbose=False
        )

def writehistory(filename,text):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
        f.write('\n')
    f.close()
# example from https://www.geeksforgeeks.org/python-generate-random-string-of-given-length/
# initializing size of string
N = 7
# using random.choices() # generating random strings
res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=N))
#Write in the history the first 2 sessions
logfile=f'Phi-3-mini-4k-Chat-{res}.txt'

writehistory(logfile,f'Your Chat with ✅✅✅✅ {modpath} and LLAMA.CPP\n---\n')   
welcomestring = '''You are Qwen1.5 AI, an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful.
Hello, introduce yourself to someone opening this program for the first time. Be concise.\n---\n'''
writehistory(logfile, welcomestring)
history = [
    {"role": "system", "content": "You are Microsoft phi-3-mini AI, an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful."},
    {"role": "user", "content": "Hello, introduce yourself to someone opening this program for the first time. Be concise."},
]
print("\033[92;1m")
while True:
    completion = client.create_chat_completion(
                    messages=history,
                    max_tokens=450,
                    stop=["</s>","[/INST]","/INST",'<|eot_id|>','<|end|>'],
                    temperature = 0.1,
                    repeat_penalty = 1.2,
                    stream=True)

    new_message = {"role": "assistant", "content": ""}
    for chunk in completion:
        try:
            print(chunk['choices'][0]['delta']['content'], end="", flush=True) #['content']
            new_message["content"] += chunk['choices'][0]['delta']['content']  
        except:
            pass          

    history.append(new_message)
    writehistory(logfile, f'🤖: {new_message}')

    print("\033[1;30m")  #dark grey
    print("Enter your text (end input with Ctrl+D on Unix or Ctrl+Z on Windows):")
    print("\033[91;1m")  #red
    lines = sys.stdin.readlines()
    userinput = ''
    for line in lines:
        userinput += line + "\n"

    if "quit!" in lines[0].lower():
            print("\033[0mBYE BYE!")
            break
    history.append({"role": "user", "content": userinput})
    writehistory(logfile, f'👤: {userinput}')
    print("\033[92;1m")
