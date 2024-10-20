#write a python program to convert KM to Meter.

# Function to convert KM to M
def km_to_meter(km):
    result = km * 1000
    return result
#taking input from user
km = int(input("Enter KM to find meter:"))
meter = km_to_meter(km)
print(km,"KM is equal to",meter,"meters")

print("programmed by Arshad khan roll no.85")