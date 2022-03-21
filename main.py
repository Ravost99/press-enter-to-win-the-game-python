from colors import colorMsg, rainBow, allBGCodes, allColorCodes
from clear import clear
from update import update
from _def import intro, help
import colors, time, random, os, sys, math, json

#varibles
ARROW = " "
score = 0
ppe = 1
pps = 0
#randomization seed
seed = random.randint(10000, 99999)

clear()
intro()
#update()
while True:
  enter = input(ARROW)

  if enter == "" or enter == " ":
    num = random.randint(1, 100)
    if num == 45:
      ppe += 1
      print(f"{colors.bg_yellow}{colors.black}Congratulations!{colors.reset}\nYour {colors.bold}PPE{colors.reset} has increased by 1!{colors.reset}")
    elif num == 50:
      pps += 1
      print(f"{colors.bg_yellow}{colors.black}Congratulations!{colors.reset}\nYour {colors.bold}PPS{colors.reset} has increased by 1!{colors.reset}")
    elif num == 69 and pps > 1 or ppe > 1:
      pps -= 1
      print(f"{colors.bg_dark_red}{colors.black}Uh Oh!{colors.reset}\nYour {colors.bold}PPS{colors.reset} has decreased by 1!{colors.reset}")
    elif num == 13 and pps > 1 or ppe > 1:
      ppe -= 1
      print(f"{colors.bg_dark_red}{colors.black}Uh Oh!{colors.reset}\nYour {colors.bold}PPE{colors.reset} has decreased by 1!{colors.reset}")
    score += ppe
  elif enter == "h":
    help()
  elif enter == "b":
    print(f"Your balance: {colors.bold}{score} Enters{colors.reset}.")
    print(f"Your PPE: {colors.bold}{ppe}{colors.reset}.")
    print(f"Your PPS: {colors.bold}{pps}{colors.reset}.")
  elif enter == "s":
    shopType = input(f"What shop type? ({colors.bold}Idle/Enter{colors.reset}) ")
    if shopType.lower() == "idle":
      pass
    elif shopType.lower() == "enter":
      enterItems = [
        ("Extra Keyboard", "Keys++", 64),
        ("More hands", "Nothing like 450 wpm", 721)
      ]
      #data = json.load(enterItems)

      for item in enterItems:
        name = item[0]
        desc = item[1]
        value = item[2]
        price = round(((value+22)**1.04)*(ppe**1.06))
        if score > price:
          color = colors.green
        else:
          color = colors.red
        #print(enterItems[item])
        print(f"( {colors.bold}{name}{colors.reset} )\n{desc}\nPPE: {value}\nCost: {color}{price}{colors.reset}\n")
      
      choseItem = input("What do you want to buy? ")
      

    else:
      print(f"{colors.red}Shop Types are Idle/Enter, not {shopType}!{colors.reset}")
      continue
          
  elif enter == "c":
    clear()
  elif enter == "r":
    reset = input("Are you sure you want to reset all your progress? (no undo) y/n ")
    if reset == "y":
      score = 0
      ppe = 1
      pps = 0
      print("Restarting  ...")
      time.sleep(0.3)
      clear()
      intro()
    else:
      continue
  #developer testing
  elif enter.startswith("ppe"):
    test = int(enter.split("ppe",1)[1])
    ppe += test
  elif enter.startswith("pps"):
    test = int(enter.split("pps",1)[1])
    pps += test
  else:
    print(f"{colors.red}Command '{colors.bold}{enter}{colors.reset}{colors.red}' not found!{colors.reset}")