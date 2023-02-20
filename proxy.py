from socket import *
import time
port = 10550
receive_buffer_size = 4096
socket1 = socket(AF_INET,SOCK_STREAM) #socket binding with client
socket1.bind(('127.0.0.1',port)) #the socket binds locally to port 10550
socket1.listen(4) #the socket is listening for a connection
print("Proxy server waiting for connection...")
while True:
    clientSocket, address = socket1.accept() #this is the proxy socket that connected to the client's
    g = time.localtime() #the time of establishing a connection with the client
    time_current_proxy = time.strftime("%H:%M:%S", g)
    print("Connection from: " + str(address) + " at " + str(time_current_proxy))
    try: 
        web_IP = clientSocket.recv(4096).decode()
        socket2= socket(AF_INET,SOCK_STREAM) #socket binding with web source
        socket2.connect((web_IP,80)) #the socket of the proxy acted as a client to the web-server and tries to connect to it
        request_string = f"GET / HTTP/1.1\r\nHost: {web_IP}\r\n\r\n"
        socket2.send(request_string.encode()) #the proxy sent the get request to the web server
        k= time.localtime()
        timeWeb = time.strftime ("%H:%M:%S", k) #the time of sending the message to the web server
        print("The proxy server has sent the request to the web server at " + str(timeWeb))
        response=socket2.recv(receive_buffer_size).decode() #the proxy received the response from the web
        socket2.close() #the socket connected with the web server closesserver
        l=time.localtime() #the time of receiving a response from the web server
        timeResponse= time.strftime("%H:%M:%S", l) #the time of receiving the response
        print("The proxy server has received a response from the web server at" + str(timeResponse))
        clientSocket.send(response.encode()) #I am sending the response from the web server to the client
        w=time.localtime() #the time of sending the response to the client
        current_time_proxy = time.strftime("%H:%M:%S",w) #this is the time of sending the proxy
        print("The response was sent to the client at " + str(current_time_proxy))
    except:
        error_message= "[ERROR]...... There was an error establishing a connection....."
        clientSocket.send(error_message.encode()) 
        print("[ERROR]....The proxy has encountered an error!!")
    finally:
        clientSocket.close() #the connection with the client closes
