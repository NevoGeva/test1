
FILE_PATH = 'people_data.json'

try:
    with open(FILE_PATH, "r") as file:
     content = file.read()
    print(content)
except: FileNotFoundError
print("that file was not found")


      
