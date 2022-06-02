import urllib, json, interactions, re, requests, helpers

def get_data():
    r =requests.get(helpers.FIRSTS_LOCG_URL)
    firsts = str(json.loads(r.text))
    match_firsts = re.findall("\/comic\/.*?-1", firsts)
    return  match_firsts

bot = interactions.Client(token=helpers.BOT_TOKEN())

@bot.command(
    name="cotw",
    description="Replies with this week's #1 comic books on LOCG",
    scope=869530640788373564,
)

async def only_firsts(ctx: interactions.CommandContext):
    data = get_data()
    body = ""
    for match in data:
        body=body+"\n https://leagueofcomicgeeks.com"+match
    await ctx.send(body)

bot.start()
