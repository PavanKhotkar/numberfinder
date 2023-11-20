import phonenumbers
from phonenumbers import geocoder

# Replace 'your_phone_number' with the actual phone number you want to parse
number = "+919876458545"  # Example phone number with the country code for India

# Specify the default country region (e.g., "IN" for India)
default_region = "IN"

parsed_number = phonenumbers.parse(number, default_region)
location = geocoder.description_for_number(parsed_number, "en")
print(location)
