import time
import os
print ("...loading")
time.sleep(.5)
os.system('clear')
print ("webradio")
print ("")
print ("9 - musik beenden")
print ("")
print ("1.  antenne_b |  4. kindradio1 ")
print ("2.  sleaze    |  5. bob        ")
print ("3.  delta     |  6. kindradio2 ")
print ("33. b3        |  7. weihn.radio")
print ("")

print ("8 - Herunterfahren")
print ("")
time.sleep(3)
track = input("what to do ? ")
print(track)


os.system('clear')

if track == "1":
    os.system('exec killall mpg123')
    os.system('exec mpg123 -@ http://mp3channels.webradio.antenne.de:80/antenne | grep ICY &')
    os.system('clear')
    os.system('python webradio.py')
elif track == "2":
    os.system('exec killall mpg123')
    os.system('exec mpg123 -@ http://stream.laut.fm/sleaze-rock-radio.m3u | grep ICY &')
    os.system('clear')
    os.system('python webradio.py')
elif track == "3":
    os.system('killall mpg123')
    os.system('exec mpg123 -@ http://streams.deltaradio.de/delta-live/mp3-192/mediaplayer | grep ICY &')
    os.system('clear')
    os.system('python webradio.py')
elif track == "33":
    os.system('killall mpg123')
    os.system('exec mpg123 -@ http://streams.br.de/bayern3_2.m3u | grep ICY &')
    os.system('clear')
    os.system('python webradio.py')
elif track == "4":
    os.system('killall mpg123')
    os.system('exec mpg123 -@ http://stream.laut.fm/kinderradio.m3u | grep ICY &')
    os.system('clear')
    os.system('python webradio.py')
elif track == "5":
    os.system('killall mpg123')
    os.system('exec mpg123 -@ http://streams.radiobob.de/bob-live/mp3-128/streams.radiobob.de/ | grep ICY &')
    os.system('clear')
    os.system('python webradio.py')
elif track == "6":
    os.system('killall mpg123')
    os.system('exec mpg123 -@ http://stream.laut.fm/kinderlieder.m3u | grep ICY &')
    os.system('clear')
    os.system('python webradio.py')
elif track == "7":
    os.system('killall mpg123')
    os.system('exec mpg123 -@ http://stream.laut.fm/kinderweihnachtsradio.m3u | grep ICY &')
    os.system('clear')
    os.system('python webradio.py')

elif track == "8":
    os.system('sudo poweroff')

elif track == "9":
    os.system('killall mpg123')
    os.system('clear')
    os.system('python webradio.py')    

else:
    print ("Finish")
