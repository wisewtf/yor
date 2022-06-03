import json, interactions, re, requests, helpers

def cotw():
    r =requests.get(helpers.FIRSTS_LOCG_URL)
    firsts = str(json.loads(r.text))
    match_firsts = re.findall("\/comic\/.*?-1", firsts)
    body = ""
    for match in match_firsts:
        body=body+"\n https://leagueofcomicgeeks.com"+match
    return  body

bot = interactions.Client(token=helpers.BOT_TOKEN())

@bot.command(
    name="cotw",
    description="Replies with this week's #1 comic books on LOCG",
    # scope is optional. So you can use it or not, in case you do remember to set the env variable
    scope=helpers.GUILD_SCOPE,
)

async def only_firsts(ctx: interactions.CommandContext):
    await ctx.send(cotw())

bot.start()