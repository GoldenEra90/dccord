import discord
from discord.ext import commands

# 개발자 페이지에서 봇에 대한 토큰 텍스트를 가져온 뒤, TOKEN에 대입하자
TOKEN = "ODAyMDMxNzk1MTc1Njg2MTg0.YApUUQ.RvMMu9Itvf3h9hTS0xBlFMACVUg"

client = discord.Client()


# 봇이 접속하면 아래의 함수를 실행하게 된다
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="디시코드 생성중"))
print("이 창은 절대로 종료되어선 안됩니다. 반드시 최소화 시켜주세요")

client = commands.Bot(command_prefix='')

@client.command(name='우리핵퇴근')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%9A%B0%EB%A6%AC%ED%95%B5%ED%87%B4%EA%B7%BC.gif?raw=true')

@client.command(name='우리핵안녕')
async def hello(ctx):
    await ctx.send('https://raw.githubusercontent.com/GoldenEra90/GoldenDCcon/master/DCcon/images/%EC%9A%B0%EB%A6%AC%ED%95%B5%EC%95%88%EB%85%95.gif')

@client.command(name='펄럭')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B5%AD%EB%BD%95%ED%8E%84%EB%9F%AD2.gif?raw=true')

@client.command(name='한심')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%BD%94%EC%A3%BC%EB%B6%80%ED%95%9C%EC%8B%AC.png?raw=true')

@client.command(name='느그흥')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%8A%90%EA%B7%B8%ED%9D%A5.gif?raw=true')

@client.command(name='암드')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/AMD.png?raw=true')

@client.command(name='인텔')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/INTEL.png?raw=true')

@client.command(name='세가')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/sega.png?raw=true')

@client.command(name='우리형')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B0%84%EC%A7%80%EB%91%90.gif?raw=true')

@client.command(name='페페시무룩')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B0%9C%EA%B5%AC%EB%A6%AC%EA%B0%91%EB%B6%84%EC%8B%B8.gif?raw=true')

@client.command(name='페페빵야')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B0%9C%EA%B5%AC%EB%A6%AC%EB%B9%B5%EC%95%BC2.png?raw=true')

@client.command(name='페페화남')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B0%9C%EA%B5%AC%EB%A6%AC%ED%99%94%EB%82%A8.png?raw=true')

@client.command(name='개돼지')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B0%9C%EB%8F%BC%EC%A7%80.png?raw=true')

@client.command(name='마치')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B2%90%EA%B3%A0%EB%A1%9C%EB%A7%88%EC%B9%98.png?raw=true')

@client.command(name='아아')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B2%90%EA%B3%A0%EB%A1%9C%EC%95%84%EC%95%84.png?raw=true')

@client.command(name='계산중')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B3%84%EC%82%B0%EC%A4%91.png?raw=true')

@client.command(name='고흐흑')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B3%A0%ED%9D%90%ED%9D%91.png?raw=true')

@client.command(name='골뎅깜놀')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B3%A8%EB%8E%85%EA%B9%9C%EB%86%80.gif?raw=true')

@client.command(name='골뎅깜놀2')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B3%A8%EB%8E%85%EA%B9%9C%EB%86%802.gif?raw=true')

@client.command(name='골뎅딸딸')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B3%A8%EB%8E%85%EB%94%B8%EB%94%B8.png?raw=true')

@client.command(name='ㅗㅜㅑ')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B3%A8%EB%8E%85%EC%98%A4%EC%9A%B0%EC%95%BC.gif?raw=true')

@client.command(name='골뎅자본')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B3%A8%EB%8E%85%EC%9E%90%EB%B3%B8.png?raw=true')

@client.command(name='골뎅행복')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B3%A8%EB%8E%85%ED%96%89%EB%B3%B5.png?raw=true')

@client.command(name='골짝댄스')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B3%A8%EC%A7%9D%EB%8C%84%EC%8A%A4.gif?raw=true')

@client.command(name='골하')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B3%A8%ED%95%98.gif?raw=true')

@client.command(name='궁뎅이')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B6%81%EB%8E%85%EC%9D%B4.png?raw=true')

@client.command(name='모노레일')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B8%B0%EA%B5%AC%EB%AA%A8%EB%85%B8%EB%A0%88%EC%9D%BC.png?raw=true')

@client.command(name='댕댕이')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B8%B0%ED%83%80%EB%8C%95%EB%8C%95.gif?raw=true')

@client.command(name='두근두근')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B8%B0%ED%83%80%EB%91%90%EA%B7%BC%EB%91%90%EA%B7%BC.png?raw=true')

@client.command(name='매우정상')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B8%B0%ED%83%80%EB%A7%A4%EC%9A%B0%EC%A0%95%EC%83%81.png?raw=true')

@client.command(name='무지개펄럭')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B8%B0%ED%83%80%EB%AC%B4%EC%A7%80%EA%B0%9C%EA%B9%83%EB%B0%9C.gif?raw=true')

@client.command(name='불편')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B8%B0%ED%83%80%EB%B6%88%ED%8E%B8.png?raw=true')

@client.command(name='상담필요')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B8%B0%ED%83%80%EC%83%81%EB%8B%B4%ED%95%84%EC%9A%94.png?raw=true')

@client.command(name='어케했노')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B8%B0%ED%83%80%EC%96%B4%EC%BC%80.gif?raw=true')

@client.command(name='유다이')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B8%B0%ED%83%80%EC%9C%A0%EB%8B%A4%ED%9D%AC1.png?raw=true')

@client.command(name='파킨')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%8C%8C%ED%82%A82.gif?raw=true')

@client.command(name='편안')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B8%B0%ED%83%80%ED%8E%B8%EC%95%88.png?raw=true')

@client.command(name='형이왜')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B8%B0%ED%83%80%ED%98%95%EC%9D%B4%EC%99%9C.png?raw=true')

@client.command(name='끄덕')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%81%84%EB%8D%95.gif?raw=true')

@client.command(name='나가')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%82%98%EA%B0%80.png?raw=true')

@client.command(name='눈물맥크리')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%88%88%EB%AC%BC%EB%A7%A5%ED%81%AC%EB%A6%AC.png?raw=true')

@client.command(name='눈물소닉')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%88%88%EB%AC%BC%EC%86%8C%EB%8B%89.png?raw=true')

@client.command(name='눈물에이미')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%88%88%EB%AC%BC%EC%86%8C%EB%8B%89%EC%97%90%EC%9D%B4%EB%AF%B8.png?raw=true')

@client.command(name='눈물테일즈')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%88%88%EB%AC%BC%EC%86%8C%EB%8B%89%ED%85%8C%EC%9D%BC%EC%A6%88.png?raw=true')

@client.command(name='눈물한조')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%88%88%EB%AC%BC%ED%95%9C%EC%A1%B0.png?raw=true')

@client.command(name='두근두근2')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%91%90%EA%B7%BC%EB%91%90%EA%B7%BC2.gif?raw=true')

@client.command(name='디발라')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%94%94%EB%B0%9C%EB%9D%BC.gif?raw=true')

@client.command(name='따봉두')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%94%B0%EB%B4%89%EB%91%90.gif?raw=true')

@client.command(name='띠껍')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%9D%A0%EA%BB%8D.png?raw=true')

@client.command(name='탕탕')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%A0%88%EB%B0%94%ED%83%95%ED%83%95.gif?raw=true')

@client.command(name='팝콘')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%A0%88%EB%B0%94%ED%8C%9D%EC%BD%981.png?raw=true')

@client.command(name='팝콘2')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%A0%88%EB%B0%94%ED%8C%9D%EC%BD%982.png?raw=true')

@client.command(name='수직낙하')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%A1%A4%EC%BD%94%EC%88%98%EC%A7%81%EB%82%99%ED%95%98.png?raw=true')

@client.command(name='하트라인')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%A1%A4%EC%BD%94%ED%95%98%ED%8A%B8%EB%9D%BC%EC%9D%B8.gif?raw=true')

@client.command(name='황가드')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%A6%B0%EA%B0%80%EB%93%9C.gif?raw=true')

@client.command(name='마참내')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%A7%88%EC%B0%B8%EB%82%B4.png?raw=true')

@client.command(name='망테크')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%A7%9D%ED%85%8C%ED%81%AC.png?raw=true')

@client.command(name='맥놀람')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%A7%A5%EB%86%80%EB%9E%8C.gif?raw=true')

@client.command(name='맥절정')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%A7%A5%EC%A0%88%EC%A0%95.gif?raw=true')

@client.command(name='맥환호')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%A7%A5%ED%99%98%ED%98%B8.gif?raw=true')

@client.command(name='맨전드')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%A7%A8%EC%A0%84%EB%93%9C.gif?raw=true')

@client.command(name='맹구')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%A7%B9%EA%B5%AC.png?raw=true')

@client.command(name='맹시')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%A7%B9%EC%8B%9C.png?raw=true')

@client.command(name='메시')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%A9%94%EC%8B%9C.gif?raw=true')

@client.command(name='메좆')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%A9%94%EC%A2%86.png?raw=true')

@client.command(name='메좆두')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%A9%94%EC%A2%86%EB%91%90.gif?raw=true')

@client.command(name='문풍당당')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%AC%B8%ED%92%8D%EB%8B%B9%EB%8B%B91.gif?raw=true')

@client.command(name='문풍당당2')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%AC%B8%ED%92%8D%EB%8B%B9%EB%8B%B92.gif?raw=true')

@client.command(name='문풍당당3')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%AC%B8%ED%92%8D%EB%8B%B9%EB%8B%B93.gif?raw=true')

@client.command(name='민트초코')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%AF%BC%ED%8A%B8%EC%B4%88%EC%BD%94.gif?raw=true')

@client.command(name='민트초코2')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%AF%BC%ED%8A%B8%EC%B4%88%EC%BD%942.gif?raw=true')

@client.command(name='바흐흑')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B0%94%ED%9D%90%ED%9D%91.png?raw=true')

@client.command(name='박지성')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B0%95%EC%A7%80%EC%84%B1.gif?raw=true')

@client.command(name='버스딸딸')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B2%84%EC%8A%A4%EB%94%B8%EB%94%B8.gif?raw=true')

@client.command(name='꼬우면')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B2%A4%EB%B8%8C%EA%BC%AC%EC%9A%B0%EB%A9%B4.gif?raw=true')

@client.command(name='버그')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B2%A4%EB%B8%8C%EB%B2%84%EA%B7%B8.gif?raw=true')

@client.command(name='의도된')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B2%A4%EB%B8%8C%EC%9D%98%EB%8F%84.gif?raw=true')

@client.command(name='볼트공중')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B3%BC%ED%8A%B8%EA%B3%B5%EC%A4%91.png?raw=true')

@client.command(name='볼트구토')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B3%BC%ED%8A%B8%EA%B5%AC%ED%86%A0.png?raw=true')

@client.command(name='볼트군인')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B3%BC%ED%8A%B8%EA%B5%B0%EC%9D%B8.png?raw=true')

@client.command(name='볼트근육')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B3%BC%ED%8A%B8%EA%B7%BC%EC%9C%A1.png?raw=true')

@client.command(name='볼트나무')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B3%BC%ED%8A%B8%EB%82%98%EB%AC%B4.png?raw=true')

@client.command(name='볼트넷여친')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B3%BC%ED%8A%B8%EB%84%B7%EC%97%AC%EC%B9%9C.png?raw=true')

@client.command(name='볼트넷친구')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B3%BC%ED%8A%B8%EB%84%B7%EC%B9%9C%EA%B5%AC.png?raw=true')

@client.command(name='볼트닌자')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B3%BC%ED%8A%B8%EB%8B%8C%EC%9E%90.png?raw=true')

@client.command(name='볼트답답')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B3%BC%ED%8A%B8%EB%8B%B5%EB%8B%B5.png?raw=true')

@client.command(name='볼트딸딸')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B3%BC%ED%8A%B8%EB%94%B8%EB%94%B8.png?raw=true')

@client.command(name='ㅗ')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B3%BC%ED%8A%B8%EB%BB%90%ED%81%90.gif?raw=true')

@client.command(name='볼트수면')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B3%BC%ED%8A%B8%EC%88%98%EB%A9%B4.png?raw=true')

@client.command(name='볼트예수')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B3%BC%ED%8A%B8%EC%98%88%EC%88%98.png?raw=true')

@client.command(name='볼트자살')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B3%BC%ED%8A%B8%EC%9E%90%EC%82%B4.png?raw=true')

@client.command(name='볼트저격')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B3%BC%ED%8A%B8%EC%A0%80%EA%B2%A9.png?raw=true')

@client.command(name='볼트펄럭')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B3%BC%ED%8A%B8%ED%8E%84%EB%9F%AD.png?raw=true')

@client.command(name='불편2')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B6%88%ED%8E%B82.gif?raw=true')

@client.command(name='불편불')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B6%88%ED%8E%B8%EB%B6%88.gif?raw=true')

@client.command(name='불편해짐')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B6%88%ED%8E%B8%ED%95%B4%EC%A7%90.gif?raw=true')

@client.command(name='우리가남이가')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B6%93%EC%8B%BC%EB%82%A8%EC%9D%B4%EA%B0%801.png?raw=true')

@client.command(name='갸아악')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B6%93%EC%8B%BC%EA%B0%B8%EC%95%84%EC%95%851.png?raw=true')

@client.command(name='구와아악')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B6%93%EC%8B%BC%EA%B5%AC%EC%99%80%EC%95%84%EC%95%85.png?raw=true')

@client.command(name='대첼시')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B8%94%EB%A3%A8%EC%8A%A4.gif?raw=true')

@client.command(name='뻐큐')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%BB%90%ED%81%90.gif?raw=true')

@client.command(name='빠요엔')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%BF%8C%EC%9A%94%EB%B9%A0%EC%9A%94%EC%97%943.gif?raw=true')

@client.command(name='atm')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%83%81%EC%A0%90ATM.png?raw=true')

@client.command(name='병원')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%83%81%EC%A0%90%EB%B3%91%EC%9B%90.png?raw=true')

@client.command(name='치킨')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%83%81%EC%A0%90%EC%B9%98%ED%82%A8.png?raw=true')

@client.command(name='커피')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%83%81%EC%A0%90%EC%BB%A4%ED%94%BC.png?raw=true')

@client.command(name='피자')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%83%81%EC%A0%90%ED%94%BC%EC%9E%90.png?raw=true')

@client.command(name='화장실')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%83%81%EC%A0%90%ED%99%94%EC%9E%A5%EC%8B%A4.png?raw=true')

@client.command(name='훌륭')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%84%A0%EC%83%9D%ED%9B%8C%EB%A5%AD.png?raw=true')

@client.command(name='빨갱이')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%86%90%EB%8B%98%EB%B9%A8%EA%B0%B1%EC%9D%B4.gif?raw=true')

@client.command(name='피곤')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%86%90%EB%8B%98%ED%94%BC%EA%B3%A4.gif?raw=true')

@client.command(name='행복')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%86%90%EB%8B%98%ED%96%89%EB%B3%B52.gif?raw=true')

@client.command(name='손도깔끔')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%86%90%EB%8F%84%EA%B9%94%EB%81%94.png?raw=true')

@client.command(name='리듬스탈')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%8A%A4%ED%83%88%EB%A6%B0.gif?raw=true')

@client.command(name='싸닉')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%8B%B8%EB%8B%89.png?raw=true')

@client.command(name='오케이')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%95%BC%EC%9D%B8%EC%8B%9C%EB%8C%80%EC%98%A4%EC%BC%80%EC%9D%B4.png?raw=true')

@client.command(name='사딸라')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%95%BC%EC%9D%B8%EC%8B%9C%EB%8C%804%EB%94%B8%EB%9D%BC.png?raw=true')

@client.command(name='야한거')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%95%BC%ED%95%9C%EA%B1%B0.png?raw=true')

@client.command(name='어쩔')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%96%B4%EC%A9%94.gif?raw=true')

@client.command(name='어케함')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%96%B4%EC%BC%80%ED%95%A8.gif?raw=true')

@client.command(name='와우')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%97%90%EB%94%94%EC%99%80%EC%9A%B0.gif?raw=true')

@client.command(name='서순')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%97%AD%EA%B0%80%EC%84%9C%EC%88%9C.png?raw=true')

@client.command(name='순서')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%97%AD%EA%B0%80%EC%88%9C%EC%84%9C.png?raw=true')

@client.command(name='왜곡흠')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%99%9C%EA%B3%A1%ED%9D%A0.gif?raw=true')

@client.command(name='우리집')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%9A%B0%EB%A6%AC%EC%A7%91.png?raw=true')

@client.command(name='우리핵드럼')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%9A%B0%EB%A6%AC%ED%95%B5%EB%93%9C%EB%9F%BC.gif?raw=true')

@client.command(name='우리핵박수')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%9A%B0%EB%A6%AC%ED%95%B5%EB%B0%95%EC%88%981.gif?raw=true')

@client.command(name='우리핵박수2')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%9A%B0%EB%A6%AC%ED%95%B5%EB%B0%95%EC%88%982.gif?raw=true')

@client.command(name='우리핵박수3')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%9A%B0%EB%A6%AC%ED%95%B5%EB%B0%95%EC%88%983.gif?raw=true')

@client.command(name='우리핵쌍안경')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%9A%B0%EB%A6%AC%ED%95%B5%EB%B3%91%EC%8B%A0.gif?raw=true')

@client.command(name='우리핵쌍안경2')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%9A%B0%EB%A6%AC%ED%95%B5%EC%8C%8D%EC%95%88%EA%B2%BD.gif?raw=true')

@client.command(name='우리핵아닌데')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%9A%B0%EB%A6%AC%ED%95%B5%EC%95%84%EB%8B%8C%EB%8D%B0.gif?raw=true')

@client.command(name='우리핵시발')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%9A%B0%EB%A6%AC%ED%95%B5%EC%8B%9C%EB%B2%8C.gif?raw=true')

@client.command(name='우리핵빵야')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%9A%B0%EB%A6%AC%ED%95%B5%EB%B9%B5%EC%95%BC.gif?raw=true')

@client.command(name='우리핵안녕2')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%9A%B0%EB%A6%AC%ED%95%B5%EC%95%88%EB%85%952.gif?raw=true')

@client.command(name='우리핵투정')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%9A%B0%EB%A6%AC%ED%95%B5%ED%88%AC%EC%A0%95.gif?raw=true')

@client.command(name='우리핵확대')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%9A%B0%EB%A6%AC%ED%95%B5%ED%99%95%EB%8C%80.gif?raw=true')

@client.command(name='우리흥')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%9A%B0%EB%A6%AC%ED%9D%A5.gif?raw=true')

@client.command(name='이풍당당')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%9D%B4%ED%92%8D%EB%8B%B9%EB%8B%B9.gif?raw=true')

@client.command(name='이풍당당2')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%9D%B4%ED%92%8D%EB%8B%B9%EB%8B%B92.gif?raw=true')

@client.command(name='이풍당당3')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%9D%B4%ED%92%8D%EB%8B%B9%EB%8B%B93.gif?raw=true')

@client.command(name='일일맹')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%9D%BC%EC%9D%BC%EB%A7%B9.png?raw=true')

@client.command(name='자기과시')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%9E%90%EA%B8%B0%EA%B3%BC%EC%8B%9C.gif?raw=true')

@client.command(name='저쪽집')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%A0%80%EC%AA%BD%EC%A7%91.png?raw=true')

@client.command(name='잔짜잔')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%A0%9C%ED%94%84%EC%9E%94%EC%A7%9C%EC%9E%94.gif?raw=true')


@client.command(name='짜잔')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%A0%9C%ED%94%84%EC%A7%9C%EC%9E%94.gif?raw=true')

@client.command(name='졸개들')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%A1%B8%EA%B0%9C%EB%93%A4.gif?raw=true')

@client.command(name='맞아')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%A2%8B%EC%9D%80%EB%A7%90%EB%84%A4%EB%A7%90%EB%A7%9E.gif?raw=true')

@client.command(name='멋있다')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%A2%8B%EC%9D%80%EB%A7%90%EB%A9%8B%EC%9E%88%EB%8B%A4.gif?raw=true')

@client.command(name='좋겠다')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%A2%8B%EC%9D%80%EB%A7%90%EC%A2%8B%EA%B2%A0%EB%8B%A4.gif?raw=true')

@client.command(name='짱이야')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%A2%8B%EC%9D%80%EB%A7%90%EC%A7%B1%EC%9D%B4%EC%95%BC.gif?raw=true')

@client.command(name='ㅊㅋ')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%A2%8B%EC%9D%80%EB%A7%90%EC%B6%95%ED%95%98%ED%95%B4.gif?raw=true')

@client.command(name='주디노우')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%A3%BC%EB%94%94%EB%85%B8%EC%9A%B0.gif?raw=true')

@client.command(name='띠용')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%A3%BC%EB%94%94%EB%9D%A0%EC%9A%A9.gif?raw=true')

@client.command(name='호랑이')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%A3%BC%ED%86%B1%ED%98%B8%EB%9E%91%EC%9D%B41.gif?raw=true')

@client.command(name='호랑이2')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%A3%BC%ED%86%B1%ED%98%B8%EB%9E%91%EC%9D%B42.gif?raw=true')

@client.command(name='호랑이3')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%A3%BC%ED%86%B1%ED%98%B8%EB%9E%91%EC%9D%B43.gif?raw=true')

@client.command(name='호랑이4')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%A3%BC%ED%86%B1%ED%98%B8%EB%9E%91%EC%9D%B44.gif?raw=true')

@client.command(name='즐겁다')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%A6%90%EA%B2%81%EB%8B%A4.png?raw=true')

@client.command(name='지루')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%A7%80%EB%A3%A8%EC%A0%84%EA%B0%88.gif?raw=true')

@client.command(name='직관')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%A7%81%EA%B4%80.gif?raw=true')

@client.command(name='찐따')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%B0%90%EB%94%B0.gif?raw=true')

@client.command(name='초골')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%B4%88%EA%B3%A8.gif?raw=true')

@client.command(name='초크바')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%B4%88%ED%81%AC%EB%B0%94.gif?raw=true')

@client.command(name='추골하하')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%B6%94%EA%B3%A8%ED%95%98%ED%95%98.png?raw=true')

@client.command(name='추골헐')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%B6%94%EA%B3%A8%ED%97%90.png?raw=true')

@client.command(name='칠레감탄')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%B9%A0%EB%A0%88%EA%B0%90%ED%83%84.gif?raw=true')

@client.command(name='파산')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%BA%90%ED%94%BC%ED%83%88%ED%8D%84%EC%82%B0.png?raw=true')

@client.command(name='폴짝')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%BA%90%ED%94%BC%ED%83%88%ED%8F%B4%EC%A7%9D.png?raw=true')

@client.command(name='커뎅챤')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%BB%A4%EB%8E%85%EC%B1%A4.png?raw=true')

@client.command(name='트럼프끄덕')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%8A%B8%EB%9F%BC%ED%94%84%EB%81%84%EB%8D%95.gif?raw=true')

@client.command(name='트럼프따봉')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%8A%B8%EB%9F%BC%ED%94%84%EB%94%B0%EB%B4%89.png?raw=true')

@client.command(name='퍄')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%8D%84.gif?raw=true')

@client.command(name='페페끄덕')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%8E%98%ED%8E%98%EB%81%84%EB%8D%95.gif?raw=true')

@client.command(name='페페네온')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%8E%98%ED%8E%98%EB%84%A4%EC%98%A8.gif?raw=true')

@client.command(name='페페무한')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%8E%98%ED%8E%98%EB%AC%B4%ED%95%9C.gif?raw=true')

@client.command(name='페페싸닉')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%8E%98%ED%8E%98%EC%8B%B8%EB%8B%89.gif?raw=true')

@client.command(name='페페윙크')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%8E%98%ED%8E%98%EC%9C%99%ED%81%AC.gif?raw=true')

@client.command(name='페페착시')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%8E%98%ED%8E%98%EC%B0%A9%EC%8B%9C.gif?raw=true')

@client.command(name='페페초딩')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%8E%98%ED%8E%98%EC%B4%88%EB%94%A9.png?raw=true')

@client.command(name='페페활활')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%8E%98%ED%8E%98%ED%99%9C%ED%99%9C.gif?raw=true')

@client.command(name='핫산결심')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%95%AB%EC%82%B0%EA%B2%B0%EC%8B%AC.gif?raw=true')

@client.command(name='핫산눈물')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%95%AB%EC%82%B0%EB%88%88%EB%AC%BC.png?raw=true')

@client.command(name='핫산발상')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%95%AB%EC%82%B0%EB%B0%9C%EC%83%81.png?raw=true')

@client.command(name='핫산서라')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%95%AB%EC%82%B0%EC%84%9C%EB%9D%BC.png?raw=true')

@client.command(name='핫산쾅')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%95%AB%EC%82%B0%EC%BE%85.png?raw=true')

@client.command(name='핫산펑')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%95%AB%EC%82%B0%ED%8E%91.png?raw=true')

@client.command(name='핫산풍습')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%95%AB%EC%82%B0%ED%92%8D%EC%8A%B5.png?raw=true')

@client.command(name='호날도')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%98%B8%EB%82%A0%EB%8F%84.gif?raw=true')

@client.command(name='호우')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%98%B8%EC%9A%B0.gif?raw=true')

@client.command(name='호우2')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%98%B8%EC%9A%B02.gif?raw=true')

@client.command(name='호우3')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%98%B8%EC%9A%B03.gif?raw=true')

@client.command(name='호우4')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%98%B8%EC%9A%B04.gif?raw=true')

@client.command(name='혼란앵무')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%98%BC%EB%9E%80%EC%95%B5%EB%AC%B4.gif?raw=true')

@client.command(name='린가드')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%99%A9%EA%B0%80%EB%93%9C.gif?raw=true')

@client.command(name='린가드2')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%99%A9%EA%B0%80%EB%93%9C2.gif?raw=true')

@client.command(name='힘의차이')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%9E%98%EC%9D%98%EC%B0%A8%EC%9D%B4.png?raw=true')

@client.command(name='회전목마')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B8%B0%EA%B5%AC%ED%9A%8C%EC%A0%84%EB%AA%A9%EB%A7%88.png?raw=true')

@client.command(name='찡긋')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%8B%89%EC%B0%A1%EA%B8%8B.gif?raw=true')

@client.command(name='똥과오둠')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%98%A5%EA%B3%BC%EC%98%A4%EB%91%A0.png?raw=true')

@client.command(name='라푼젤')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%9D%BC%ED%91%BC%EC%A0%A4.gif?raw=true')

@client.command(name='붕쯔붕쯔')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%B0%B8%ED%94%BC%EB%B6%95%EC%AF%94.png?raw=true')

@client.command(name='리전락')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B8%B0%ED%83%80%EB%A6%AC%EC%A0%84%EB%9D%BD.gif?raw=true')

@client.command(name='노리치')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%85%B8%EB%A6%AC%EC%B9%98.gif?raw=true')

@client.command(name='닭집')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%8B%AD.png?raw=true')

@client.command(name='개집')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B0%9C%EC%A7%91.png?raw=true')

@client.command(name='꿀밤')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%9D%A0%EA%BB%8D%EA%BF%80%EB%B0%A4.png?raw=true')

@client.command(name='볼트꺼져')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B3%BC%ED%8A%B8%EA%BA%BC%EC%A0%B8.png?raw=true')

@client.command(name='볼트댕댕')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B3%BC%ED%8A%B8%EB%8C%95%EB%8C%95.png?raw=true')

@client.command(name='볼트떠남')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B3%BC%ED%8A%B8%EB%96%A0%EB%82%A8.png?raw=true')

@client.command(name='볼트띠용')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B3%BC%ED%8A%B8%EB%9D%A0%EC%9A%A9.png?raw=true')

@client.command(name='볼트라이플')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B3%BC%ED%8A%B8%EB%9D%BC%EC%9D%B4%ED%94%8C.png?raw=true')

@client.command(name='볼트루저')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B3%BC%ED%8A%B8%EB%A3%A8%EC%A0%80.png?raw=true')

@client.command(name='볼트마약')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B3%BC%ED%8A%B8%EB%A7%88%EC%95%BD.png?raw=true')

@client.command(name='볼트부활')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B3%BC%ED%8A%B8%EB%B6%80%ED%99%9C.png?raw=true')

@client.command(name='볼트처형')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B3%BC%ED%8A%B8%EC%B2%98%ED%98%95.png?raw=true')

@client.command(name='펨코')
async def hello(ctx):
    await ctx.send('https://www.fmkorea.com/')

@client.command(name='식사하거라')
async def hello(ctx):
    await ctx.send('https://media1.tenor.com/images/e0d994f2e71f6faf8136d253e453d9fb/tenor.gif')

@client.command(name='한입만')
async def hello(ctx):
    await ctx.send('https://media.tenor.com/images/8f72013666143dc33380989c716a5248/tenor.gif')

@client.command(name='cex')
async def hello(ctx):
    await ctx.send('https://www.sostokyo.com/searching/s_contents02/s_label/s_mb0406c.gif')

@client.command(name='라면')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%83%81%EC%A0%90%EA%B3%A0%EA%B8%B0%EA%B5%AD%EC%88%98.png?raw=true')

@client.command(name='감자튀김')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%83%81%EC%A0%90%EA%B0%90%EC%9E%90%ED%8A%80%EA%B9%80.png?raw=true')

@client.command(name='핫식스')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%83%81%EC%A0%90%EC%9D%8C%EB%A3%8C%EC%88%98.png?raw=true')

@client.command(name='제로콜라')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%A0%9C%EB%A1%9C%EC%BD%9C%EB%9D%BC.png?raw=true')

@client.command(name='콜라')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%83%81%EC%A0%90%EC%9D%8C%EB%A3%8C%EC%88%98.png?raw=true')

@client.command(name='핫도그')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%83%81%EC%A0%90%ED%95%AB%EB%8F%84%EA%B7%B8.png?raw=true')

@client.command(name=':hotdog~1:')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%83%81%EC%A0%90%ED%95%AB%EB%8F%84%EA%B7%B8.png?raw=true')

@client.command(name='햄버거')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%83%81%EC%A0%90%ED%96%84%EB%B2%84%EA%B1%B0.png?raw=true')

@client.command(name='탄식')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%83%84%EC%8B%9D.gif?raw=true')

@client.command(name='리사수')
async def hello(ctx):
    await ctx.send('https://raw.githubusercontent.com/blastsg/dccon/master/images/dccon/%EB%A6%AC%EC%82%AC%EC%88%98.png')

@client.command(name='제리쾅쾅')
async def hello(ctx):
    await ctx.send('https://raw.githubusercontent.com/blastsg/dccon/master/images/dccon/%EC%A0%9C%EB%A6%AC%EC%BE%85%EC%BE%85.gif')

@client.command(name='탄식2')
async def hello(ctx):
    await ctx.send('https://raw.githubusercontent.com/blastsg/dccon/master/images/dccon/%ED%83%84%EC%8B%9D2.gif')

@client.command(name='훔바')
async def hello(ctx):
    await ctx.send('https://raw.githubusercontent.com/blastsg/dccon/master/images/dccon/%ED%9B%94%EB%B0%94.gif')

@client.command(name='아이게뭔가요')
async def hello(ctx):
    await ctx.send('https://raw.githubusercontent.com/blastsg/dccon/master/images/dccon/%ED%9B%94%EB%B0%94.gif')

@client.command(name='전복')
async def hello(ctx):
    await ctx.send('https://tv.telk.kr/images/eurotruck/%EC%9C%A0%ED%8A%B8%EC%A0%84%EB%B3%B5.gif')

@client.command(name='역주행')
async def hello(ctx):
    await ctx.send('https://tv.telk.kr/images/eurotruck/%EC%9C%A0%ED%8A%B8%EC%97%AD%EC%A3%BC%ED%96%89.gif')

@client.command(name='박수')
async def hello(ctx):
    await ctx.send('https://quad2378-dccon.azurewebsites.net/images/dccon/%EC%8B%AC%EC%98%81%EB%B0%95%EC%88%98.gif')

@client.command(name='박수2')
async def hello(ctx):
    await ctx.send('https://quad2378-dccon.azurewebsites.net/images/dccon/%EC%8B%AC%EC%98%81%EB%B0%95%EC%88%982.gif')

@client.command(name='리스트')
async def hello(ctx):
    await ctx.send('그런거 없음ㅋ')

@client.command(name='예민하네')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%98%88%EB%AF%BC%ED%95%98%EB%84%A4.gif?raw=true')

@client.command(name='볼트파오후')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B3%BC%ED%8A%B8%ED%8C%8C%EC%98%A4%ED%9B%84.png?raw=true')

@client.command(name='볼트침대')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B3%BC%ED%8A%B8%EC%B9%A8%EB%8C%80.png?raw=true')

@client.command(name='볼트화염병')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B3%BC%ED%8A%B8%ED%99%94%EC%97%BC%EB%B3%91.png?raw=true')

@client.command(name='볼트활활')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B3%BC%ED%8A%B8%ED%99%9C%ED%99%9C.png?raw=true')


@client.command(name='H')
async def hello(ctx):
    await ctx.send('https://funzinnu.com/stream/cdn/dccon/H.gif')

@client.command(name='S')
async def hello(ctx):
    await ctx.send('https://funzinnu.com/stream/cdn/dccon/S.gif')

@client.command(name='R')
async def hello(ctx):
    await ctx.send('https://funzinnu.com/stream/cdn/dccon/R.gif')

@client.command(name='L')
async def hello(ctx):
    await ctx.send('https://funzinnu.com/stream/cdn/dccon/L.gif')


@client.command(name='페페운전')
async def hello(ctx):
    await ctx.send('https://funzinnu.com/stream/cdn/dccon/%ED%8E%98%ED%8E%98%EC%9A%B4%EC%A0%84.gif')

@client.command(name='페페페페')
async def hello(ctx):
    await ctx.send('https://funzinnu.com/stream/cdn/dccon/%ED%8E%98%ED%8E%98%ED%8E%98%ED%8E%98.gif')

@client.command(name='페페비트')
async def hello(ctx):
    await ctx.send('https://funzinnu.com/stream/cdn/dccon/%ED%8E%98%ED%8E%98%EB%B9%84%ED%8A%B8.gif')

@client.command(name='지갑')
async def hello(ctx):
    await ctx.send('https://funzinnu.com/stream/cdn/dccon/%EC%A7%80%EA%B0%91.gif')

@client.command(name='치직')
async def hello(ctx):
    await ctx.send('https://funzinnu.com/stream/cdn/dccon/%EC%B9%98%EC%A7%81.gif')


@client.command(name='페페마법')
async def hello(ctx):
    await ctx.send('https://funzinnu.com/stream/cdn/dccon/%ED%8E%98%ED%8E%98%EB%A7%88%EB%B2%95.gif')

@client.command(name='우리핵생각')
async def hello(ctx):
    await ctx.send('https://funzinnu.com/stream/cdn/dccon/%EC%9A%B0%EB%A6%AC%ED%95%B5%EC%83%9D%EA%B0%81.gif')

@client.command(name='개간지')
async def hello(ctx):
    await ctx.send('http://funzinnu.com/stream/cdn/dccon/%EA%B0%9C%EA%B0%84%EC%A7%80.gif')

@client.command(name='그건니가')
async def hello(ctx):
    await ctx.send('http://funzinnu.com/stream/cdn/dccon/%EA%B7%B8%EA%B1%B4%EB%8B%88%EA%B0%80.jpg')

@client.command(name='F')
async def hello(ctx):
    await ctx.send('http://funzinnu.com/stream/cdn/dccon/F.gif')

@client.command(name='대피하라')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%8C%80%ED%94%BC%ED%95%98%EB%9D%BC.png?raw=true')

@client.command(name='상환가')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%83%81%ED%99%98%EA%B0%80.png?raw=true')

@client.command(name='장투중')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%9E%A5%ED%88%AC%EC%A4%91.png?raw=true')

@client.command(name='개잡주')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B0%9C%EC%9E%A1%EC%A3%BC.png?raw=true')

@client.command(name='님주식')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%8B%98%EC%A3%BC%EC%8B%9D.png?raw=true')

@client.command(name='하환가')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%95%98%ED%99%98%EA%B0%80.png?raw=true')

@client.command(name='꺼억')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%BA%BC%EC%96%B5.png?raw=true')

@client.command(name='작전주')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%9E%91%EC%A0%84%EC%A3%BC.png?raw=true')


@client.command(name='엿')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%B3%BC%ED%8A%B8%EA%B8%B0%EC%83%81.png?raw=true')

@client.command(name='guro')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/guro.png?raw=true')

@client.command(name='펩시')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%8E%A9%EC%8B%9C%EC%A0%9C%EB%A1%9C.png?raw=true')

@client.command(name='한잔해')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%95%9C%EC%9E%94%ED%95%B4.gif?raw=true')

@client.command(name='스타벅스')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%8A%A4%ED%83%80%EB%B2%85%EC%8A%A4.gif?raw=true')

@client.command(name='스벅')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%8A%A4%ED%83%80%EB%B2%85%EC%8A%A4.gif?raw=true')

@client.command(name='네다철')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B8%B0%EA%B5%AC%EB%AA%A8%ED%98%95%EA%B8%B0%EC%B0%A8.png?raw=true')

@client.command(name='감튀')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%83%81%EC%A0%90%EA%B0%90%EC%9E%90%ED%8A%80%EA%B9%80.png?raw=true')

@client.command(name='제리폭소')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%A0%9C%EB%A6%AC%EA%B9%94%EA%B9%94.gif?raw=true')

@client.command(name='lg')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/LG.png?raw=true')

@client.command(name='영화관')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EA%B8%B0%EA%B5%AC%EC%98%81%ED%99%94%EA%B4%80.png?raw=true')

@client.command(name='yo')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/yo.gif?raw=true')

@client.command(name='와쿠와쿠')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/wakuwaku.gif?raw=true')

@client.command(name='미소')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/miso.gif?raw=true')

@client.command(name='일어나')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/wakeup.gif?raw=true')

@client.command(name='풉')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%ED%92%89.png?raw=true')

@client.command(name='버스뻐큐')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/busfuckyou.gif?raw=true')

@client.command(name='떡아')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EB%96%A1%EC%95%84.png?raw=true')

@client.command(name='출근')
async def hello(ctx):
    await ctx.send('https://github.com/GoldenEra90/GoldenDCcon/blob/master/DCcon/images/%EC%B6%9C%EA%B7%BC.gif?raw=true')



# 봇을 실행하자
client.run(TOKEN)
