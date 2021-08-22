# message = 'วัชราวลี'
# result = len(message)
# print(result)

# message = 'วัชราวลี'
# result = 'วัช' in message
# print(result)

# message = '0982612325'
# result = message.isdigit()
# print(result)

# message = 'Just Python'
# result = message.replace('Python', 'Rabbit')
# print(result)

message = 'กระต่าย, กระรอก, หมี'
animals = message.split(', ')
new_message = '+'.join(animals)
print(new_message)
print(animals)
