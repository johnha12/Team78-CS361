# Team78-CS361

This is a guide to use the fortuneMicroservice.py. This guide will cover how to send a request to the microservice as well as to recieve its response. fortuneMicroservice.py will generate a string fortune immediately after a request is recieved. fortuneMicroservice.py uses fortunePipe.txt as the communication pipe between the program and microservice.

# Sending a request
To send a request, the program must write a single integer in the fortunePipe.txt. There are two ways to send a request. The program may have its own call to write an integer onto the txt file, or import fortuneMicroservice and call fortuneMicroservice.request(). fortuneMicroservice.request() will return a string instance of the generated fortune. This means the user must either save it in a variable or use it right away (ex. print(fortuneMicroservice.request()). fortuneMicroservice.request() will send a request then return the response as soon as possible.


# Recieving a response
Recieving a response have similar steps as sending a request. Make sure you have sent the request before grabbing a response (not doing so may result in no string, an int, or an non-random fortune). There are two ways to recieve a response. The program can call a function to read the fortunePipe.txt file, or use the request() function provided. fortuneMicroservice.request() will send a request then return the response as soon as possible.

# Warnings
1. Write an int onto txt file to request. read txt file to recive response.
2. Make sure fortuneMicroservice.py is running in the background.
3. import time and use sleep(1) in between request and response. This is due to microservice needing to write fortune and return response.

![alt text](https://github.com/johnha12/Team78-CS361/blob/main/CS%20361%20A8_1.jpg?raw=true)
