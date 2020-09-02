f = open("breached_accounts.txt", 'r')

lines = f.read().split('\n') # Get all lines of files (pairs of `key: value`)
f.close()

result = [] # Result of "censoring", will be same format as input

for i in lines: # Loop each line
  data = i.split(':') # Split, data[0] is a key and data[1] is a value (what we need to censor)
  lenght = len(data[1])
  if lenght<3:
  	result.append(data[0] + ':' + data[1][0:lenght] + '***') # Censor, leaving only three first characters
  else: 
  	result.append(data[0] + ':' + data[1][0:3] + '***') # Censor from the last character and above  
final = '\n'.join(result); # Join lines together

x = open("breached_accounts_censored.txt", "w")
x.write(final)
x.close()