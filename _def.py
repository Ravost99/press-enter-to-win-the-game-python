import colors, time
def main_menu():
  pass

def intro():
  print(f"Welcome to press enter to win in {colors.bold}python!{colors.reset}\n")
  time.sleep(0.5)
  print("Press enter to get enters!")
  time.sleep(0.5)
  print(f"Your {colors.bold}PPE{colors.reset} is how many points you get per enter.\nYour {colors.bold}PPS{colors.reset} is how many points you get per second.\n")
  time.sleep(0.5)
  print(f"Pressing enter has a {colors.green}5%{colors.reset} chance to increase your {colors.bold}PPE{colors.reset} or your {colors.bold}PPS{colors.reset} by 1!")
  time.sleep(0.5)
  # too many colors. !!!
  print(f"{colors.bg_dark_red}But...{colors.reset} Pressing enter has a {colors.dark_red}1%{colors.reset} chance to decrease your {colors.bold}PPE{colors.reset} or your {colors.bold}PPS{colors.reset} by 1!\nAnd even if you have {colors.dark_red}0{colors.reset} or {colors.dark_red}-1{colors.reset} {colors.bold}PPE or PPS{colors.reset} just keep pressing enter to get more {colors.bold}PPE or PPS{colors.reset}")
  time.sleep(0.5)
  print(f"And also even tho the {colors.bg_green}run button{colors.reset} is green and doesn't say {colors.bg_gray}stop{colors.reset}, it will still be running")
  time.sleep(0.5)
  help()
  time.sleep(0.5)

def help():
  print(f"Press {colors.bold}enter{colors.reset} to get points.")
  print(f"Press {colors.bold}h{colors.reset} to get some help with the commands.")
  print(f"Press {colors.bold}b{colors.reset} to view your balance.")
  print(f"Press {colors.bold}s{colors.reset} to go to the shop.")
  print(f"Press {colors.bold}c{colors.reset} to clear the console.")
  print(f"Press {colors.bold}{colors.dark_red}r{colors.reset} to hard reset your progress.")