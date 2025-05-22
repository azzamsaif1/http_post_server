# import socket

# HOST = '127.0.0.1'
# PORT = 1234

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind((HOST, PORT))
# server_socket.listen(1)

# print(f"[Server Running] Visit: http://{HOST}:{PORT}")




# while True:
#     client_conn,client_add=server_socket.accept()
#     print(f"[accepted the connection {client_conn} from add{client_add}]")
#     #[accepted the connection <socket.socket fd=436, family=2, type=1, proto=0,
#     # laddr=('127.0.0.1', 1234),
#     # raddr=('127.0.0.1', 50492)> from add('127.0.0.1', 50492)]
#     request=client_conn.recv(1024).decode()
#     print(f"[Request Received]\n {request}")
#     #GET / HTTP/1.1
#                 # Host: 127.0.0.1:1234
#                 # Connection: keep-alive
#                 # Cache-Control: max-age=0
#                 # sec-ch-ua: "Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"
#                 # sec-ch-ua-mobile: ?0
#                 # sec-ch-ua-platform: "Windows"
#                 # Upgrade-Insecure-Requests: 1
#                 # User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36
#                 # Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
#                 # Sec-Fetch-Site: none
#                 # Sec-Fetch-Mode: navigate
#                 # Sec-Fetch-User: ?1
#                 # Sec-Fetch-Dest: document
#                 # Accept-Encoding: gzip, deflate, br, zstd
#                 # Accept-Language: de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7,ar;q=0.6

#     #anlysis the first line
#     request_line=request.splitlines()[0]
#     print("[this is the first line request]")
#     print(request_line)
#     method,path,_=request_line.split()
#     print(f"this is the method :{method} and this is the path : {path} and this is th _{_}")
#     username =""
#     #if the method of the request is POST
#     if method =="POST":
#         body=request.split("\r\n\r\n",1)[1]
#         print(f"[POST BODY]: {body}")
        
        
#         if body.startswith("name="):
#             username=body.replace("name=","").replace("+","")
            
#             #response 
#         if username:
#             message=f"<h2>Hello , {username} ! </h2>"
#         else:
#             message=""
            
#         html = f"""
#                     <html>
#                         <head><title>POST Example</title></head>
#                         <body>
#                             <h1>Welcome to Azzam's POST Server</h1>
#                             <form method="POST" action="/">
#                                 <input type="text" name="name" placeholder="Your name">
#                                 <button type="submit">Send</button>
#                             </form>
#                             {message}
#                         </body>
#                     </html>
#                     """
#         response=f""" 
#                     HTTP/1.1 200 OK
#                     content_type:text/html
#                     content-length:{len({html})}
                    
#                     {html}
#         """
#         client_conn.sendall(response.encode())
#         client_conn.close()
        
        
import socket

HOST = '127.0.0.1'
PORT = 8080

# create server 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"[Server Running] Visit: http://{HOST}:{PORT}")

while True:
    client_conn, client_addr = server_socket.accept()
    request = client_conn.recv(1024).decode()
    print("[Request Received]:\n", request)

    # analysis request
    request_line = request.splitlines()[0]
    method, path, _ = request_line.split()

    user_name = ""

    #    POST
    if method == "POST":
        body = request.split("\r\n\r\n", 1)[1]
        print("[POST Body]:", body)

        #    body
        if body.startswith("name="):
            user_name = body.replace("name=", "").replace("+", " ")

    #   
    if user_name:
        message = f"<h2>Hello, {user_name}!</h2>"
    else:
        message = ""

    html = f"""
    <html>
        <head><title>POST Example</title></head>
        <body>
            <h1>Welcome to Azzam's POST Server</h1>
            <form method="POST" action="/">
                <input type="text" name="name" placeholder="Your name">
                <button type="submit">Send</button>
            </form>
            {message}
        </body>
    </html>
    """

    response = f"""\
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: {len(html)}

{html}
"""
    client_conn.sendall(response.encode())
    client_conn.close()
