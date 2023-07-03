option=float(input('para hypotenuse aplasta 1 para pi circumference aplasta 2 para encontrar los length de cada lado  de un hexagon aplasta 3'))
if option==1:
  side1= float(input('width'))
  side2= float(input('length'))
  hyp=(side1*side1+side2*side2)**0.5
  print(hyp)
if option==2:
  Pi=3.14
  r=float(input("radius"))
  c=3.14*r*2
  print("\nCircumference = ", c)
if option==3:
  area=float(input('area del hexagon'))
  L=area/6
  print("/nthe length = ",c)
