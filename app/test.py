import sys

#print("hello world")

# print(sys.executable) 
# C:\Users\31557\AppData\Local\Programs\Python\Python310\python.exe

# print(sys.path)
# ['E:\\test\\copykitt-tutorial\\copykitt-tutorial\\app', '
# C:\\Users\\31557\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip', 
# 'C:\\Users\\31557\\AppData\\Local\\Programs\\Python\\Python310\\DLLs', 
# 'C:\\Users\\31557\\AppData\\Local\\Programs\\Python\\Python310\\lib', 
# 'C:\\Users\\31557\\AppData\\Local\\Programs\\Python\\Python310', 
# 'C:\\Users\\31557\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages']


# E:\test\copykitt-tutorial\copykitt-tutorial\app, C:\Users\31557\AppData\Local\Programs\Python\Python310\python310.zip, C:\Users\31557\AppData\Local\Programs\Python\Python310\DLLs, C:\Users\31557\AppData\Local\Programs\Python\Python310\lib, C:\Users\31557\AppData\Local\Programs\Python\Python310, C:\Users\31557\AppData\Local\Programs\Python\Python310\lib\site-packages




from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World -- zou"}







