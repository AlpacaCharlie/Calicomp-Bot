# Calicomp-Bot
This is a discord bot that is inspired in the CALICOMP from the wonderful game that is VA-11 Hall-a

It only has one file with all the code because it's the first time I use python and I have basically no idea about it.

You must addyou own token for the bot to work. You get this from the Discord website. This bot also uses two roles. "Bartender" is for the users that will be able to add drinks. "Drink Admin" is for the users that will be able to reset the drink list.

The drink list is an excel file so you can add or edit any drink you want but be sure it follows the same formating.

To execeute all this I used IDLE from python. Needed libraries should be here but it's the first time I use github so please tell me if not

This project was powered mainly by the power of beer and love for Va-11 Hall-a so I'm sorry for all the grammar mistakes.

You can also invite this bot to your server with: https://discordapp.com/api/oauth2/authorize?client_id=502904311429201935&permissions=0&scope=bot
Be warned that like this the drink list is shared btween all the servers until I find how to fix this
Also it's hosted on AWS and in a couple of months I'll run out of the free tier, so if you are lazy to host and want me to keep 
hosting it you can donato to alpacacharlieoficial@gmail.com via paypal
(but believe me right now it's much better if you host it yourselves but I ilike money)

# Mutiple Servers update

 Good news! After a bit more of programming I figgured out how to make a single instance of a bot support multiple servers. The bot 
 will now create one file for each server taking as a base "drinklist.xls".
 Also a bug with the serve command that would end in a empty string was fixed
