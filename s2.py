import phonenumbers
from phonenumbers import NumberParseException, is_valid_number, format_number, PhoneNumberFormat

def validate_and_format_number(phone_number):
    try:
        # Parse the number without a specific region to allow all international formats
        parsed_number = phonenumbers.parse(phone_number, None)
        if is_valid_number(parsed_number):
            formatted_number = format_number(parsed_number, PhoneNumberFormat.INTERNATIONAL)
            return formatted_number
        else:
            return None
    except NumberParseException:
        return None

def process_phone_numbers(input_file, output_file):
    valid_numbers = []

    with open(input_file, 'r') as infile:
        numbers = infile.readlines()

    for number in numbers:
        number = number.strip()
        result = validate_and_format_number(number)
        if result:
            valid_numbers.append(result)

    with open(output_file, 'w') as outfile:
        for valid_number in valid_numbers:
            outfile.write(valid_number + '\n')

    print(f"Valid numbers have been written to {output_file}")

# Example usage
input_file = 'phone_numbers_216.txt'  # Replace with your input file
output_file = 'valid_numb_216.txt'  # Replace with your desired output file
process_phone_numbers(input_file, output_file)
