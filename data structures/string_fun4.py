name= input("What is your name=>")

print(name)
print(f"lemgth: {len(name)}")

cl_name= name.strip()

print(cl_name)
print(f"lemgth: {len(cl_name)}")

secret_msg= '00000000000000OLA00000000000'
print(secret_msg.strip('0'))
print(secret_msg.lstrip('0'))
print(secret_msg.rstrip('0'))

crap_msg= '''

    Hey brother
    
'''
clean_msg = crap_msg.strip()
print(crap_msg)
print(clean_msg) 
print(f'{len(crap_msg)} --> {len(clean_msg)}')

