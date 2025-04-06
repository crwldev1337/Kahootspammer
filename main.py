import asyncio, random, string
from kahoot import KahootClient
from kahoot.packets.server.question_start import QuestionStartPacket
from pystyle import Colors, Colorate

def randomstring_gen(lenght=7):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(lenght))

async def question_start(packet: QuestionStartPacket):
     print(f"Question started: {packet}")
     
async def joiner():
    gradient = Colors.red_to_yellow
    gradient2 = Colors.yellow_to_green
    print(Colorate.Horizontal(gradient2, "Made by github.com/crwldev1337"))
    print("")
    print(Colorate.Horizontal(gradient, "[>]"), end=" ")
    gamepin = input(f"GamePin : ")
    print(Colorate.Horizontal(gradient, "[>]"), end=" ")
    numbots = int(input("Bots (ex: 100) : "))
    print(Colorate.Horizontal(gradient, "[>]"), end=" ")
    botname = input("Bots Name : ")
    usernames = [f"{botname} {randomstring_gen(7)}" for _ in range(numbots)]
    tasks = []
    for username in usernames:
        client = KahootClient()
        client.on("question_start", question_start)
        task = client.join_game(game_pin=gamepin, username=username)
        tasks.append(task)
    await asyncio.gather(*tasks)
    
asyncio.run(joiner())
