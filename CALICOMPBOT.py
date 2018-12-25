import random
import asyncio
import aiohttp
import json
import xlrd
import os.path
from xlutils.copy import copy
import xlwt
from discord import Game
from discord.ext import commands
from discord.ext.commands import Bot
from random import randint


def open_file(id :int = None):
    global wb
    global sheet
    wb = 'drinklist'+ str(id) +'.xls'
    if os.path.isfile(wb):
        wb = xlrd.open_workbook(wb)
        sheet = wb.sheet_by_index(0)
    else:
        wb = xlrd.open_workbook('drinklist.xls')
        w = copy(wb)
        w.save('drinklist'+ str(id) +'.xls')
        open_file()
        

def close_file():
    wb.release_resources()

def get_rows():
    x : int = 1
    while str(sheet.cell_value(x, 0)) != "NO":
        x += 1
    print(x)
    return x

BOT_PREFIX = "cali_"
TOKEN = '' 

client =  Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="to serve drinks"))
    print("CALICOMP 1.1 starting up")

@client.command(pass_context=True)
async def name(ctx, name):
    open_file(ctx.message.server.id)
    rows = get_rows()
    rocks = 0
    aged = 0
    mixblend = 0
    outuput = "null"
    for x in range (1,rows+1):
        if name.lower() == sheet.cell_value(x, 0).lower():
            break
    if x != rows:
        name = sheet.cell_value(x, 0).lower()
        price = int(sheet.cell_value(x, 1))
        output = str(name) + " has a price of " + str(price) + "$" + '\n' + "Drink flavour: " + sheet.cell_value(x, 2)+ '\n' + "Drink type:"
        for y in range (3,16):
            if sheet.cell_value(x, y) == 1:
                output += " " + str(sheet.cell_value(0, y))
        output += '\n' + "Ingredients:" + '\n'
        for y in range (16,21):
            if sheet.cell_value(x,y) !=0:
                output += str(sheet.cell_value(0, y)) + ": " + str(sheet.cell_value(x,y)) + '\n'
        rocks = int(sheet.cell_value(x,21))
        aged = int(sheet.cell_value(x,22))
        mixblend = int(sheet.cell_value(x,23))
        if rocks == 0 and aged == 0 and mixblend == 0:
            output += "All mixed" + '\n'
        if rocks == 1 and aged == 0 and mixblend == 0:
            output += "All on the rocks and mixed" +'\n'
        if rocks == 0 and aged == 1 and mixblend == 0:
            output += "All aged and mixed" +'\n'
        if rocks == 1 and aged == 1 and mixblend == 0:
            output += "All on the rocks, aged and mixed" +'\n'
        if rocks == 0 and aged == 0 and mixblend == 1:
            output += "All blended" + '\n'
        if rocks == 1 and aged == 0 and mixblend == 1:
            output += "All on the rocks and blended" + '\n'
        if rocks == 0 and aged == 1 and mixblend == 1:
            output += "All aged and blended" + '\n'
        if rocks == 1 and aged == 1 and mixblend == 1:
            output += "All on the rocks, aged and blended" + '\n'
        output +=sheet.cell_value(x, 24)
        await client.say(output)
    close_file()
    if x == rows:
        await client.say("The drink you want to seach doesn't figure in the B.T.C. files")

@client.command(pass_context=True)
async def flavour(ctx,flavour):
    open_file(ctx.message.server.id)
    flavour = flavour.lower()
    rows = get_rows()
    trigered = int(1)
    output = "hey"
    if flavour == "List" or flavour == "list":
        trigered = int(0)
        await client.say("Aviable flavours are: N/A, Sour, Bubbly, Spicy, Sweet, Bitter")
    if flavour == "N/A":
        trigered = int(0)
        output = "N/A drinks are:" + '\n'
        for x in range (1,rows+1):
            if flavour == sheet.cell_value(x, 2):
                output += str(sheet.cell_value(x,0))+ '\n'
    if flavour == "Sour" or flavour == "sour":
        trigered = int(0)
        output ="Sour drinks are:" + '\n'
        for x in range (1,rows+1):
            if "Sour" == sheet.cell_value(x, 2):
                output += str(sheet.cell_value(x,0))+ '\n'
    if flavour == "Bubbly" or flavour == "bubbly":
        trigered = int(0)
        output = "Bubbly drinks are:" + '\n'
        for x in range (1,rows+1):
            if "Bubbly" == sheet.cell_value(x, 2):
                output += str(sheet.cell_value(x,0))+ '\n'
    if flavour == "Spicy" or flavour == "spicy":
        trigered = int(0)
        output ="Spicy drinks are:" + '\n'
        for x in range (1,rows+1):
            if "Spicy" == sheet.cell_value(x, 2):
                output += str(sheet.cell_value(x,0))+ '\n'
    if flavour == "Sweet" or flavour == "sweet":
        trigered = int(0)
        aoutput = "Sweet drinks are:"+ '\n'
        for x in range (1,rows+1):
            if "Sweet" == sheet.cell_value(x, 2):
                output += str(sheet.cell_value(x,0))+ '\n'
    if flavour == "Bitter" or flavour == "bitter":
        trigered = int(0)
        output = "Bitter drinks are:"+ '\n'
        for x in range (1,rows+1):
            if "Bitter" == sheet.cell_value(x, 2):
                output += sheet.cell_value(x,0)+ '\n'
    if trigered:
        output = "The flavour you are searching for doesn't figure in the B.T.C. files"
    await client.say(output)
    close_file
        

@client.command(pass_context=True)
async def type(ctx, tipe):
    open_file(ctx.message.server.id)
    rows = get_rows()
    trigered = int(1)
    output = "hey"
    if tipe.lower() == "list":
        trigered = int(0)
        output = "Aviable types are: Classy, Promo, Classic, Girly, Manly, Bottled, Vintage, Sobering, Bland, Soft, Happy, Burning and Strong"
    if trigered:
        for y in range (3,16):
            if tipe == sheet.cell_value(0, y).lower():
                trigered = int(0)
                output= sheet.cell_value(0, y) + " drinks:" + '\n'
                break
        for x in range (0,rows+1) :
            if 1 == sheet.cell_value(x, y):
                output += sheet.cell_value(x, 0)+ '\n'
    if trigered:
        output = "The type you are searching for doesn't figure in the B.T.C. files. You can use cali_type list to see aviable types."
    await client.say(output)
    close_file()

@client.command(pass_context=True)
async def serve(ctx):
    open_file(ctx.message.server.id)
    rows = get_rows()
    x = randint(1,rows)
    output = "You get a "
    output += sheet.cell_value(x, 0)
    output += ". You drink it and "
    if sheet.cell_value(x, 20) == 0:
        y = randint(1,5)
    else:
        y = randint(1,10)
    if y == 1:
        output += "feel perfectly fine."
    if y == 2:
        output += "still want another drink."
    if y == 3:
        output += "notice you can't take the glass because you are a shiba."
    if y == 4:
        output += "think if the money was worth it."
    if y == 5:
        output += "think that the bartender over there has a John face."
    if y == 6:
        output += "start to feel dizzy."
    if y == 7:
        output += "karmotrine starts hitting you fast."
    if y == 8:
        output += "think about how horrible the flavour was."
    if y == 9:
        output += "the drinks makes you want to pat the shiba."
    if y == 10:
        output += "you don't expect the spanish inquisiton."
    await client.say(output)
    close_file()

@client.command(pass_context=True)
async def money(ctx, price : str = None):
    open_file(ctx.message.server.id)
    aviableDrinks = 0
    x = 1
    output = "hey"
    if price == None:
        await client.say("Please enter a the money you want to pay for a drink and the system will make a list of the drink you can buy")
    else:
        priceINT = int(price)
        output = "With " + price + "$ you can buy:" + '\n'
        while str(sheet.cell_value(x, 1)) != "NO":
            if priceINT > int(sheet.cell_value(x, 1)):
                aviableDrinks = 1
                output += sheet.cell_value(x, 0) + "    "
            x += 1
    if aviableDrinks == 0:
        await client.say("You cant buy any drink with "+ price + "$")
    else:
        await client.say(output)
    close_file()
            
@client.command(pass_context=True)
async def add_drink(ctx,name : str=None,price:int=None,flav:int=None,clasy:int=None,prom:int=None,clasc:int=None,girl:int=None,man:int=None,bot:int=None,vin:int=None,sob:int=None,blan:int=None,sof:int=None,hap:int=None,burn:int=None,stro:int=None,adel:int=None,brons:int=None,pwd:int=None,flan:int=None,karm:int=None,rock:int=None,aged:int=None,mix:int=None,desc:str=None):
    if "bartender" in [y.name.lower() for y in ctx.message.author.roles]:
        open_file(ctx.message.server.id)
        if name==None:
            output = "This command needs a very specific input because I don't know how to program and must follow this formating:" + '\n'
            output += "name,price,flavour,classy,promo,classic,girly,manly,bottled,vintage,sobering,bland,soft,happy,burning,strong,Adelhyde,Bronson Ext,Pwd Delta,Flanergide,Karmotrine,Rocks,Aged,Miixed/Blended,Description"+'\n'
            output += "The name can't have any spaces for now" + '\n' + "Price can be any integer number you want"
            output += "Flavour goes from 1 to 6. 1=N/A 2=Bitter 3=Bubbly 4=Sour 5=Spicy 6=Sweet" + '\n'
            output += "From classy to strong youcan choose between 0 and 1. 0=NO 1=YES" + '\n'
            output += "Next five are the ingredients. YOu can mix them as you want but total can't be more than 20"+ '\n'
            output += "If its aged mixed or blended put a one on the dessired position"+ '\n' + "Finally add a short description or fun fact betwen" +'"'
            await client.say(output)
        elif price == None:
            await client.say("Add a price to the drink")
        elif  flav == None or flav < 1 or flav > 6 :
            await client.say("No input or bad input int flavour")
        elif clasy == None or clasy > 1 or clasy < 0:
            await client.say("No input or bad input in classy")
        elif prom == None or prom > 1 or prom < 0:
            await client.say("No input or bad input in promo")
        elif clasc == None or clasc > 1 or clasc < 0:
            await client.say("No input or bad input in classic")
        elif girl == None or girl > 1 or girl < 0:
            await client.say("No input or bad input in girly")
        elif man == None or man > 1 or man < 0:
            await client.say("No input or bad input in manly")
        elif bot == None or bot > 1 or bot < 0:
            await client.say("No input or bad input in bottled")
        elif vin == None or vin > 1 or vin < 0:
            await client.say("No input or bad input vintage")
        elif sob == None or sob > 1 or sob < 0:
            await client.say("No input or bad input sobering")
        elif blan == None or blan > 1 or blan < 0:
            await client.say("No input or bad input bland")
        elif sof == None or sof > 1 or sof < 0:
            await client.say("No input or bad input soft")
        elif hap == None or hap > 1 or hap < 0:
            await client.say("No input or bad input happy")
        elif burn == None or burn > 1 or burn < 0:
            await client.say("No input or bad input burning")
        elif adel == None:
            await client.say("No input of Adelhyde")
        elif brons == None:
            await client.say("No input of Bronson Ext")
        elif pwd == None:
            await client.say("No input of Pwd Delta")
        elif flan == None:
            await client.say("No input of Flanergide")
        elif karm == None:
            await client.say("No input of Karmotrine")
        elif adel+brons+pwd+flan+karm > 20:
            await client.say("More than 20 ingredients")
        elif rock == None or rock > 1 or rock < 0:
            await client.say("No input or bad input Rocks")
        elif aged == None or aged > 1 or rock < 0:
            await client.say("No input or bad input aged")
        elif mix == None or mix > 1 or mix < 0:
            await client.say("No input or bad input mixed/blended")
        elif  desc == None:
            await client.say("No input or bad input description")
        else:
            realflav :str = None
            if flav == 1:
                realflav = "N/A"
            if flav == 2:
                realflav = "Bitter"
            if flav == 3:
                realflav = "Bubbly"
            if flav == 4:
                realflav = "Sour"
            if flav == 5:
                realflav = "Spicy"
            if flav == 6:
                realflav = "Sweet"
            w = copy(wb)
            sheet2 = w.get_sheet(0)
            x = 1
            while str(sheet.cell_value(x, 0)) != "NO":
                x += 1
            sheet2.write(x, 0, name)
            sheet2.write(x, 1,price)
            sheet2.write(x, 2,realflav)
            sheet2.write(x, 3,clasy)
            sheet2.write(x, 4,prom)
            sheet2.write(x, 5,clasc)
            sheet2.write(x, 6,girl)
            sheet2.write(x, 7,man)
            sheet2.write(x, 8,bot)
            sheet2.write(x, 9,vin)
            sheet2.write(x, 10,sob)
            sheet2.write(x, 11,blan)
            sheet2.write(x,12,sof)
            sheet2.write(x, 13,hap)
            sheet2.write(x, 14,burn)
            sheet2.write(x, 15,stro)
            sheet2.write(x, 16,adel)
            sheet2.write(x, 17,brons)
            sheet2.write(x, 18,pwd)
            sheet2.write(x, 19,flan)
            sheet2.write(x, 20,karm)
            sheet2.write(x, 21,rock)
            sheet2.write(x, 22,aged)
            sheet2.write(x, 23,mix)
            sheet2.write(x, 24,desc)
            x+=1
            for y in range (0,25):
                sheet2.write(x,y,"NO")
            close_file()
            w.save('drinklist'+ str(ctx.message.server.id) +'.xls')
            open_file()
            await client.say("Done")
    else:
        await client.say("Only B.T.C. bartenders can do that")
       
@client.command(pass_context=True)
async def reset_drink(ctx):
    if "drink admin" in [y.name.lower() for y in ctx.message.author.roles]:
        w = copy(wb)
        sheet2 = w.get_sheet(0)
        for y in range (0,25):
            sheet2.write(30,y,"NO")
        close_file()
        w.save('drinklist'+ str(ctx.message.server.id) +'.xls')
        open_file(ctx.message.server.id)
        await client.say("Done")
    else:
        await client.say("You don't have the necesary role to do that. (Drink Admin)")

@client.command(pass_context=True)
async def id_test(ctx):
    wb = 'drinklist'+ ctx.message.server.id +'.xls'
    await client.say(wb)
    
client.run(TOKEN)

