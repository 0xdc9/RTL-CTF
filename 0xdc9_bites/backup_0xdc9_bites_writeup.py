def deci(cipher):
	key = 'w'
	a = cipher.split(' ')
	key_1 = ord(key)
	key_2 = int(key.encode('hex'))
	keyes = [key_1, key_2]
	cipher = ""
	for x in range(0, len(a)):
		if x % 2 == 1:
			cipher += chr(int(a[x]) ^ (128 - keyes[0]  + keyes[0]))

		elif x % 2 == 0:
			cipher += chr(int(a[x]) ^ (128 -  keyes[1] + keyes[1]))

	print(cipher)

deci('210 212 204 251 200 180 248 223 194 249 212 179 164 164 223 247 233 183 232 223 240 217 183 232 176 238 253')