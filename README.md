# phi-3-miniTEST

Repo of the code from the Medium article

### Requirements
Create a virtual envirnment and activate it
```
python -m venv venv
venv\Scripts\activate  #to activate the virtual environment
```

Install llama-cpp-python
```
# for CPU
pip install llama-cpp-python[server]==0.2.62

# with CUDA support
$env:CMAKE_ARGS="-DLLAMA_CUBLAS=on"
pip install llama-cpp-python[server]==0.2.62
```


## Run the model
```
python LlamaCPP-phi-3-mini_multilines_chat.py
```

There is multi line input support
to end generation, on a blank line end input with Ctrl+D on Unix or Ctrl+Z on Windows
