import urllib

def update():
    stuff_to_update = ['main.py', '_def.py']
    for fl in stuff_to_update:
        dat = urllib.request.urlopen("https://raw.githubusercontent.com/Ravost99/press-enter-to-win-the-game-python/main/" + fl).read()
        with open(fl, 'wb') as file:
          file.write(dat)
    print('\n\t\tUpdated Successfull !!!!')
    print('\tRun The Script Again...')
    exit()