import random
import shutil
import numpy as np
import tweepy 
from PIL import Image
import os

os.chdir('/Users/lukaissciandra/Desktop/Python/Twitter')

def rgb2hex(r,g,b):
    return "0x{:02x}{:02x}{:02x}".format(r,g,b)

img = Image.new( 'RGB', (600,480), "black")
pixels = img.load()

R1 = random.randint(0,255)
G1 = random.randint(0,255)
B1 = random.randint(0,255)
color1 = (R1,G1,B1)

R2 = random.randint(0,255)
G2 = random.randint(0,255)
B2 = random.randint(0,255)
color2 = (R2,G2,B2)

hex1 = rgb2hex(color1[0],color1[1],color1[2])
hex2 = rgb2hex(color2[0],color2[1],color2[2])
combo = hex1+" | "+hex2

colors = {}

for i in range(0,120,1): # col
    for j in range(img.size[1]): #  row
        pixels[i,j] = color1
        colors[i] = color1
for i in range(480,600,1):    # col
    for j in range(img.size[1]):    #  row
        pixels[i,j] = color2
        colors[i] = color2

prop = {}
for i in range(120,480,1):
    prop[i] = (479-i)

for i in range(120,480,1):    # col
    for j in range(img.size[1]):
        mult = prop[i]/360  # row
        rblend = round((R1*mult)+(R2*(1-mult)))
        gblend = round((G1*mult)+(G2*(1-mult)))
        bblend = round((B1*mult)+(B2*(1-mult)))
        color_blend = (rblend,gblend,bblend)
        colors[i] = color_blend
        pixels[i,j] = color_blend
        if i == 120:
            colorend1 = (rblend,gblend,bblend)
        if i == 478:
            colorend2 = (rblend,gblend,bblend)


inext = 0
for i in range(0,599,1):    # col
    for j in range(img.size[1]): #row
        inext = i + 1
        if colors[i] != colors[inext]:
            for j in range(0,450,2):
                i = inext
        color_blend = colors[i]
        pixels[i,j] = color_blend

img.save('/Users/lukaissciandra/Desktop/Python/Twitter/temp.png')

#Removed access credentials

tweet_text=combo
image_path = '/Users/lukaissciandra/Desktop/Python/Twitter/temp.png'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret_key)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)

status = api.update_with_media(image_path, tweet_text)
