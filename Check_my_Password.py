import requests  # to make http requests
import hashlib
from maskpass import askpass


def request_api_data(query_char):  # to request data from pwnedpasswords API.
    url = 'https://api.pwnedpasswords.com/range/' + query_char  # using the API
    res = requests.get(url)  # getting the response
    if res.status_code != 200:  # checking for the status code.
        raise RuntimeError(f'Error Fetching : {res.status_code} Check the API and try again')
    return res.text

def password_leaks_count(response_data , tail_hash_to_check):   # count password leaks.
    
    response_data=response_data.splitlines(False) # organize data line wise in a list
    response_data=[line.split(':') for line in response_data] # split hash and count.
    
    for hash,count in response_data:    # list unpacking 
        if hash == tail_hash_to_check:
            return count
    return 0
        
   
def Check_password(password):  
      
    hashpassword = hashlib.sha1(password.encode('utf-8')).hexdigest().upper() # Convert plain password into hashed  hexadecimal format
    
    first5_char , tail =hashpassword[:5], hashpassword[5:]
    
    data=request_api_data(first5_char)
    return password_leaks_count(data , tail)
    
    
    
def main():
    password =askpass(prompt="Enter Your Password: ", mask="*")
    count=Check_password(password)
    if count :
        print(f'This Password has been breached {count} times. \nBetter Choose another One !')
    else :
        print('Good News ! No breaches found. You are good to go. \n \n :)')
        
    return None


if __name__=='__main__':
    main()
