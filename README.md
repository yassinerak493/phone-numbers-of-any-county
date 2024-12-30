# phone-numbers-of-any-county
generate real phone numbers of any country in the world 

Here's the corrected version of your explanation:
you need to install chromedriver in this path C:\path\to\chromedriver\chromedriver.exe
Numbers are generated with a script (likely s1.py).
The output file will be named phone_numbers_{country_code}.txt. 
After that, use the script s2.py to filter out the incorrect numbers, creating a second file named valid_numb_{country_code}.txt.
At the end of the script, you can change the input and output file names as needed. These generated numbers are then tested to check if they exist on WhatsApp using s3.py.
You can also change the input and output file names in s3.py like you did in s2.py. If a number exists on WhatsApp, it is considered valid or "real."
