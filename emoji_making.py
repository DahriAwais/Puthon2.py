def social_media_post(good,bad,neutral):
  a=str(input("Enter your comment:"))

    
    
  if a in good:
      return "\U0001F600" 
  elif a in bad:
      return "\U0001F61F"
  elif a in neutral:
      return "\U0001F610"
  else:
      return "cant provide an emoji"

good=["good", "best", "better", "wow", "impressive", "wonderfull"]


bad=["bad", "worsty", "ugly", "not good", "frustrating", "unimpressive"]

neutral=["ordnary", "average", "neutral", "common", "standerd", "ok", ]
while True:
  print("welcome to the social media post generator")
  print("1. Enter your comment:")
  print("2. Exit:")
  choice=int(input("Enter your choice 1 or 2:"))
  if choice==1:
    print(social_media_post(good,bad,neutral))



d=social_media_post(good,bed,neutral)
print(d)





  



