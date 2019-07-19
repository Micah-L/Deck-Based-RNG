#You can change the modulus 2**128 to something else. Just be sure to change it in both functions below. Since 2**225 < 52! < 2**226, it is recommended to keep it below 2**225.

def factmod(n): #returns n! mod
	if n <= 1:
		return 1
	f = 1
	for i in xrange(1,n+1):
		f = f*i % 2**128
	return f
#The seed defines a particular total order of S_52 (the seed being the smallest in that order), and the function returns the position of deck in that ordering modulo 2**128. Thus the function is clearly surjective (onto 128 bit ints). 
#You may change the seed to any deck of cards, so long as it is complete and valid.
def deck_to_number(deck):
	seed = ("5h","4s", "5s","7s", "9s", "Qc", "Kc","Ah", "2h", "3h",  "Ks", "3c", "Ad", "2d", "3d", "7c","10s", "Qs",  "6d", "8d", "9d", "8c",  "10d", "8s","5d", "Jd", "As", "Qd", "Kd","Ac", "2c","4c","3s",  "5c",  "2s",  "Kh", "6c", "6s",  "Js", "7d", "9c", "10c", "Jc", "4d","4h","6h", "7h", "8h", "9h", "10h", "Jh", "Qh") #can be any deck
	order = dict(zip(seed,range(1,53)))
	d = [order[deck[i]] for i in range(len(deck))]
	n=0
	for i in range(len(d)):
		n = n + (d[i]-1-len(filter(lambda x: x < d[i], d[0:i])))*factmod(len(d)-1-i) % 2**128
	return n
