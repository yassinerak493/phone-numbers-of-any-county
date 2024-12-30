import phonenumbers
from phonenumbers import PhoneNumber
from phonenumbers.phonenumberutil import region_code_for_country_code
import random

# Mapping of country codes to their respective phone number lengths
country_phone_lengths = {
    1: 10,    # US, Canada
    7: 11,    # Russia
    20: 10,   # Egypt
    27: 10,   # South Africa
    30: 10,   # Greece
    31: 9,    # Netherlands
    32: 9,    # Belgium
    33: 9,    # France
    34: 9,    # Spain
    36: 9,    # Hungary
    39: 10,   # Italy
    40: 10,   # Romania
    41: 9,    # Switzerland
    43: 10,   # Austria
    44: 10,   # United Kingdom
    45: 8,    # Denmark
    46: 10,   # Sweden
    47: 8,    # Norway
    48: 9,    # Poland
    49: 11,   # Germany
    51: 9,    # Peru
    52: 10,   # Mexico
    53: 8,    # Cuba
    54: 10,   # Argentina
    55: 11,   # Brazil
    56: 9,    # Chile
    57: 10,   # Colombia
    58: 11,   # Venezuela
    60: 10,   # Malaysia
    61: 9,    # Australia
    62: 10,   # Indonesia
    63: 10,   # Philippines
    64: 9,    # New Zealand
    65: 8,    # Singapore
    66: 9,    # Thailand
    81: 10,   # Japan
    82: 9,    # South Korea
    84: 11,   # Vietnam
    86: 11,   # China
    90: 10,   # Turkey
    91: 10,   # India
    92: 11,   # Pakistan
    93: 9,    # Afghanistan
    94: 10,   # Sri Lanka
    95: 9,    # Myanmar
    98: 11,   # Iran
    212: 9,   # Morocco
    213: 9,   # Algeria
    216: 8,   # Tunisia
    218: 9,   # Libya
    220: 8,   # Gambia
    221: 9,   # Senegal
    222: 9,   # Mauritania
    223: 8,   # Mali
    224: 9,   # Guinea
    225: 10,  # Côte d'Ivoire
    226: 8,   # Burkina Faso
    227: 8,   # Niger
    228: 8,   # Togo
    229: 8,   # Benin
    230: 8,   # Mauritius
    231: 8,   # Liberia
    232: 8,   # Sierra Leone
    233: 9,   # Ghana
    234: 10,  # Nigeria
    235: 8,   # Chad
    236: 8,   # Central African Republic
    237: 8,   # Cameroon
    238: 7,   # Cape Verde
    239: 7,   # São Tomé and Príncipe
    240: 9,   # Equatorial Guinea
    241: 7,   # Gabon
    242: 7,   # Congo-Brazzaville
    243: 9,   # Congo-Kinshasa
    244: 9,   # Angola
    245: 9,   # Guinea-Bissau
    246: 7,   # Diego Garcia (British Indian Ocean Territory)
    247: 7,   # Ascension Island
    248: 7,   # Seychelles
    249: 8,   # Sudan
    250: 9,   # Rwanda
    251: 9,   # Ethiopia
    252: 7,   # Somalia
    253: 7,   # Djibouti
    254: 10,  # Kenya
    255: 10,  # Tanzania
    256: 9,   # Uganda
    257: 7,   # Burundi
    258: 9,   # Mozambique
    260: 10,  # Zambia
    261: 8,   # Madagascar
    262: 9,   # Réunion
    263: 9,   # Zimbabwe
    264: 9,   # Namibia
    265: 9,   # Malawi
    266: 8,   # Lesotho
    267: 7,   # Botswana
    268: 6,   # Eswatini
    269: 7,   # Comoros
    290: 7,   # Saint Helena
    291: 7,   # Eritrea
    297: 7,   # Aruba
    298: 6,   # Faroe Islands
    299: 6,   # Greenland
    350: 9,   # Gibraltar
    351: 9,   # Portugal
    352: 9,   # Luxembourg
    353: 9,   # Ireland
    354: 7,   # Iceland
    355: 8,   # Albania
    356: 8,   # Malta
    357: 8,   # Cyprus
    358: 10,  # Finland
    359: 9,   # Bulgaria
    370: 8,   # Lithuania
    371: 8,   # Latvia
    372: 8,   # Estonia
    373: 8,   # Moldova
    374: 8,   # Armenia
    375: 9,   # Belarus
    376: 6,   # Andorra
    377: 9,   # Monaco
    378: 9,   # San Marino
    379: 10,  # Vatican City
    380: 9,   # Ukraine
    381: 10,  # Serbia
    382: 8,   # Montenegro
    383: 8,   # Kosovo
    385: 9,   # Croatia
    386: 8,   # Slovenia
    387: 8,   # Bosnia and Herzegovina
    389: 8,   # North Macedonia
    420: 9,   # Czech Republic
    421: 9,   # Slovakia
    423: 9,   # Liechtenstein
    500: 4,   # Falkland Islands
    501: 7,   # Belize
    502: 8,   # Guatemala
    503: 8,   # El Salvador
    504: 8,   # Honduras
    505: 8,   # Nicaragua
    506: 8,   # Costa Rica
    507: 7,   # Panama
    508: 7,   # Saint Pierre and Miquelon
    509: 8,   # Haiti
    590: 9,   # Guadeloupe
    591: 8,   # Bolivia
    592: 7,   # Guyana
    593: 9,   # Ecuador
    594: 9,   # French Guiana
    595: 9,   # Paraguay
    596: 9,   # Martinique
    597: 8,   # Suriname
    598: 8,   # Uruguay
    599: 9,   # Curaçao
}

def generate_random_phone_number(country_code):
    # Get the region code (e.g., 'US' for United States) for the given country code
    region_code = region_code_for_country_code(country_code)
    
    if not region_code:
        raise ValueError("Invalid country code")

    # Get the phone number length for the given country code
    phone_length = country_phone_lengths.get(country_code, 7)  # Default to 7 if not found

    # Generate a random subscriber number with the correct length
    subscriber_number = random.randint(10**(phone_length-1), 10**phone_length - 1)

    # Create a phone number object
    phone_number = PhoneNumber()
    phone_number.country_code = country_code
    phone_number.national_number = subscriber_number
    
    # Format the phone number in the international format
    formatted_number = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

    return formatted_number

def generate_unique_phone_numbers(country_code, num_numbers):
    unique_numbers = set()
    while len(unique_numbers) < num_numbers:
        new_number = generate_random_phone_number(country_code)
        unique_numbers.add(new_number)
    return unique_numbers

def save_numbers_to_file(country_code, phone_numbers):
    # Create a filename based on the country code
    filename = f"phone_numbers_{country_code}.txt"
    
    # Write phone numbers to the file
    with open(filename, 'w') as file:
        for number in phone_numbers:
            file.write(f"{number}\n")
    
    print(f"Phone numbers saved to {filename}")

def main():
    try:
        country_code = int(input("Enter the country code (e.g., 1 for US, 44 for UK): "))
        
        # Check if the country code is valid
        if region_code_for_country_code(country_code) is None:
            print("Invalid country code. Exiting.")
            return

        num_numbers = int(input("Enter the number of phone numbers to generate: "))

        if num_numbers <= 0:
            raise ValueError("Number of phone numbers must be greater than zero.")
        
        phone_numbers = generate_unique_phone_numbers(country_code, num_numbers)

        # Save numbers to a file
        save_numbers_to_file(country_code, phone_numbers)

        for i, number in enumerate(phone_numbers, start=1):
            print(f"{i}: {number}")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
