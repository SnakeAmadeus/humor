import os, platform
c = input("how many calculators would you like to open? :")
for i in range(int(c) if c.isnumeric() else sum([ord(ch) for ch in c])):
	os.system({"Windows" : "Calc", "Darwin" : "open -na Calculator &"}[platform.system()])
