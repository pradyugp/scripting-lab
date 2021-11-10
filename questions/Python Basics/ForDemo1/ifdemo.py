x = -3 # Have to give this line, else error : "NameError: name 'x' is not defined"
if x > 0.0 :
 print 'Positive'

elif x < 0.0 :
 print 'Negative'
 x = -1.0 * x
else :
 print 'Zero'

# Another way to write this code using "else - if" 

if x > 0.0 :
 print '+ve'

else: 
 if x < 0.0 :
  print '-ve'
  x = -1.0 * x
 else :
  print '0'

# --- OUTPUT ----
#Negative
#+ve

