import pycurl
from io import BytesIO
from scapy.layers.inet import IP, TCP
from scapy.all import send

print("""
\033[38;5;27m██████╗ ██████╗ ██╗    ██╗ ██████╗ ███╗   ██╗████████╗
██╔══██╗██╔══██╗██║    ██║██╔═══██╗████╗  ██║╚══██╔══╝
██║  ██║██████╔╝██║ █╗ ██║██║   ██║██╔██╗ ██║   ██║   
██║  ██║██╔══██╗██║███╗██║██║   ██║██║╚██╗██║   ██║   
██████╔╝██████╔╝╚███╔███╔╝╚██████╔╝██║ ╚████║   ██║   
╚═════╝ ╚═════╝  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   
\033[0m
""")

print("\033[38;5;21mFlame44 & GTP 3.5 the goat\033[0m")

def send_http_request(url, method='GET', headers=None, data=None, file=None):
    buffer = BytesIO()
    curl = pycurl.Curl()
    try:
        curl.setopt(pycurl.URL, url)
        curl.setopt(pycurl.CUSTOMREQUEST, method)
        if headers:
            header_list = [f"{key}: {value}" for key, value in headers.items()]
            curl.setopt(pycurl.HTTPHEADER, header_list)
        if data:
            curl.setopt(pycurl.POSTFIELDS, data)
        if file:
            curl.setopt(pycurl.HTTPPOST, [("file", (curl.FORM_FILE, file))])
        curl.setopt(pycurl.WRITEFUNCTION, buffer.write)
        curl.setopt(pycurl.VERBOSE, 1)  # Enable verbose mode
        curl.perform()

        # Extract response information
        response_code = curl.getinfo(pycurl.RESPONSE_CODE)
        response_headers = buffer.getvalue().decode('iso-8859-1')
        response_body = buffer.getvalue().decode('utf-8')

        # Print response information
        print(f"HTTP Response Code: {response_code}")
        print("Response Headers:")
        print(response_headers)
        print("Response Body:")
        print(response_body)

        return response_body
    except pycurl.error as e:
        print("An error occurred during the HTTP request:")
        print(e)
    finally:
        buffer.close()
        curl.close()

def send_network_request(data):
    try:
        packet = IP(dst="127.0.0.1") / TCP() / bytes(data, 'utf-8')
        send(packet)
        print("Network request sent successfully.")
    except Exception as e:
        print("An error occurred while sending the network request:")
        print(e)

if __name__ == "__main__":
    url = input("Enter the URL or IP (e.g., www.site.com or 10.10.10.10): ")
    method = 'GET'
    headers = {'User-Agent': 'Mozilla/5.0'}
    data = None
    file = None

    response = send_http_request(url, method, headers, data, file)

    repeat = input("Do you want to repeat the request? (yes/no): ")
    while repeat.lower() == 'yes':
        modify = input("Do you want to modify the request? (yes/no): ")
        if modify.lower() == 'yes':
            print("Previous response:")
            print(response)
            new_url = input(f"URL ({url}): ") or url
            new_method = input(f"Method ({method}): ") or method
            new_headers = {}
            for key, value in headers.items():
                new_value = input(f"Header '{key}' ({value}): ")
                if new_value:
                    new_headers[key] = new_value
                else:
                    new_headers[key] = value
            new_data = input("Enter new data: ")
            file_path = input("Enter a file to attach: ")
            response = send_http_request(new_url, new_method, new_headers, new_data, file_path)
        else:
            send_network_request(response)
        repeat = input("Do you want to repeat the request? (yes/no): ")
