# countingips


Created a program in Python that:
- Runs an http server on your local machine
- An HTTP path that responds to one URL path “/checkips” that takes JSON as input
- Receives a valid JSON input is an object with one key “ips” with a value that is a list of IP addresses as strings, e.g. {“ips”:[“1.2.3.4”, “192.168.1.1”]}
- The output is the number of IPs that are in this file at the time of the http request: https://raw.githubusercontent.com/stamparm/ipsum/master/levels/5.txt (which the contents change regularly)
- Has at least one runnable test case written with `unittest` 

Can start the server by running app.py 

Server responds to:
`curl --data '{"ips":["94.142.241.194", "192.168.1.1"]}' -H "Content-type: application/json" http://127.0.0.1:5000/checkips`
and prints:
1

Eric Tiancheng Gu 
copyright (c) 2021
