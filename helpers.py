import os

def BOT_TOKEN():
    return os.environ['BOT_TOKEN']


# This one is only needed if you use the scope option in the main script
def GUILD_SCOPE():
    return os.environ['GUILD_SCOPE']

FIRSTS_LOCG_URL = "https://leagueofcomicgeeks.com/comic/get_comics?addons=1&list=releases&publisher[]=2&publisher[]=7&publisher[]=1&publisher[]=5&publisher[]=13&list_refinement=firsts&format%5B%5D=1&date_type=week&date="
