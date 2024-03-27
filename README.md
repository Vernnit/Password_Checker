# Password_Checker

## What it does ?
This is a Password Checker which tells whether the password you entered has ever been breached or is it safe to use.


## How it works ?

We are using pwnedpasswords API here to check for the password's security , if it has been breached or not.

we will use only first 5 characters of Hashed password so our password is not revealed to this API , then we will receive all breached password hashes matching with those five chars and then match the full hash with the list of all hashes we will be getting from the API.