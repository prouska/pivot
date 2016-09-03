import math
import googlefinance

h = float(raw_input("Price High:"))
l = float(raw_input("Price Low:"))
c = float(raw_input("Close Price:"))
	


def pivot():

	
	
	numbers=[h,l,c]							
	
	p = sum(numbers)/len(numbers)
	
	print "Pivot: " + format(p,'.2f')
	
	r = p * 2 - l
	
	print "R1: " + format(r,'.2f')	

	rr = p + (h - l)
	
	print "R2: " + format(rr,'.2f')
	
	rrr = r + (h - l)
	
	print "R3: " + format(rrr,'.2f')
	
	s = p * 2 - h
	
	print "S1: " + format(s,'.2f')
	
	ss = p - (h - l)
	
	print "S2: " + format(ss,'.2f')
	
	sss = s - (h - l)
	
	print "S3: " + format(sss,'.2f')






pivot()	

