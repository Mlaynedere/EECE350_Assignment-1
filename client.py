from socket import *
import time
from datetime import datetime
import getmac
server0 = '127.0.0.1'
web_IP= input("Enter the web page's IP: ")
port = 10550
receive_buffer_size = 4096
clientSocket= socket(AF_INET, SOCK_STREAM) 
clientSocket.connect((server0,port)) #the client connects to the proxy at the port specified
t = time.localtime()   #I used these two lines of code from (https://www.programiz.com/python-programming/datetime/current-time) to find the exact time of sending the message
current_time_client = time.strftime("%H:%M:%S", t)#to find the exact time of sending the message
clientSocket.send(web_IP.encode()) #the client's socket is sending the web ip desired to the proxy
print("I,as client, have sent: " + str(web_IP) + " to the proxy server, which is the IP address of the page I want, at " + str(current_time_client) + "\n")
j=clientSocket.recv(receive_buffer_size).decode() #here the client receives the response desired
g= time.localtime() #this is the time of receiving the response
time_current_client = time.strftime("%H:%M:%S", g)
print("I have received the response from the proxy server at " + str(time_current_client) + "\n")
print(j)
start_time= datetime.strptime(current_time_client,"%H:%M:%S") #I used the code from (https://www.geeksforgeeks.org/calculate-time-difference-in-python/)
end_time=datetime.strptime(time_current_client,"%H:%M:%S")  #and I combined the idea of both programs to find the differnece in time
total= end_time - start_time #this is the difference in time between sending the request and getting back the response
totalSeconds = total.total_seconds() #I utilized the code from (https://www.geeksforgeeks.org/extracting-mac-address-using-python/)
MAC_address = getmac.get_mac_address() #to get the MAC address
print("The total round trip time is: " + str(totalSeconds) + "seconds, with the address: " + str(MAC_address) + "\n")
clientSocket.close()
