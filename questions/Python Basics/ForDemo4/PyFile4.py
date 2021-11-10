try:
  f = open('HakunaMatata', "a")
  f.write('Lion King')
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()
