# This code is made by Eric Tiancheng Gu (c) 2021
# First we imported the Flask class.
try:
    from flask import Flask, request
    import requests
except Exception as e:
    print("Some modules are missing, please check".format(e))

# Next we create an instance of this class. The first argument is the name of the application’s module or package. If
# you are using a single module (as in this example), you should use __name__ because depending on if it’s started as
# application or imported as module the name will be different ('__main__' versus the actual import name). This is
# needed so that Flask knows where to look for templates, static files, and so on. For more information have a look
# at the Flask documentation.
app = Flask(__name__)

# file url of ips
url = 'https://raw.githubusercontent.com/stamparm/ipsum/master/levels/5.txt'


# We then use the route() decorator to tell Flask what URL should trigger our function. The http server responds to
# one URL path “/checkips” that takes JSON as input, have a POST method as well The function is given a name which is
# also used to generate URLs for that particular function, and returns the message we want to display in the user’s
# browser.

@app.route('/checkips', methods=['POST'])
def checkips_controller() -> str:
    # have content as inputted data with curl
    content = request.get_json()

    return checkips_service(content)


def checkips_service(content: dict) -> str:
    # initialize a number to count ips
    number = 0

    # check if there is no input, if there is no input, automatic 0
    if content is None:
        return "1"

    # ips_given gets the dictionary element with key 'ips'
    ips_given = content['ips']

    # file gets the list of the code from the given url by line, and becomes
    # a set so we can check if something is in it quickly, with less runtime
    file = requests.get(url).text
    file = file.split('\n')
    file = set(file)

    # going through each ip in the input data
    for ip in ips_given:

        """
        This is some of the bonus stuff
        
        # check if the ip is actually an ip address
        if "." in ip:
            elements_array = ip.split(".")
            if len(elements_array) == 4:
                for i in elements_array:
                    if i.isnumeric() and 0 <= int(i) <= 255:
                        flag = True
                    else:
                        flag = False
                        break
            else:
                flag = False
        else:
            flag = False

        # remove data if it's not an ip address
        if flag is False:
            #ips_given.remove(ip)
            print("not an ip in the inputs")
            # OR return error
            return -1
        """

        # we check if that ip is in the file
        if ip in file:
            # add one if it is
            number += 1

    return str(number)


# main method here
if __name__ == '__main__':
    # run on local host
    app.run(host="0.0.0.0")

    # test terminal command
    # curl --data '{"ips":["94.142.241.194", "192.168.1.1"]}' -H "Content-type: application/json" http://127.0.0.1:5000/checkips
