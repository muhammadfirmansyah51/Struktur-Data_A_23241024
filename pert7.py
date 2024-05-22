#tabel kebenaran (logika boolean)
# and or not xor

# NOT
print ("*******Logika NOT********")
x = False
y = True
print ("nilai dari x =", x)
print ("nilai dari y =", y)

# and
print ("*********Logika And*********")
x = False
y = False
z = x and y

x = True
y = False
z = (x, "and", y, "=", z)
print (x, "and", y, "=", z )

x = False
y = True
z = (x, "and", y, "=", z)
print (x, "and", y, "=", z )

x = True
y = True
z = (x, "and", y, "=", z)
print (x, "and", y, "=", z )

# OR (akan bernilai true, selama ada satu aja yang true, )
# bernilai salah, ketika keduanya salah
print ("*********Logika OR*********")
x = False
y = False
z = x or y
print (x, "or", y, "=", z)

x = True
y = False
z = (x, "or", y, "=", z)
print (x, "or", y, "=", z )

x = False
y = True
z = (x, "or", y, "=", z)
print (x, "or", y, "=", z )

x = True
y = True
z = (x, "or", y, "=", z)
print (x, "or", y, "=", z )

# xor
print ("*********Logika XOR*********")
x = False
y = False
z = x ^ y
print (x, "xor", y, "=", z)

x = True
y = False
z = x ^ y
print (x, "xor", y, "=", z)

x = False
y = True
z = x ^ y
print (x, "xor", y, "=", z)

x = True
y = True
z = x ^ y
print (x, "xor", y, "=", z)
