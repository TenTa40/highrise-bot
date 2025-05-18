from highrise import BaseBot, Position
from highrise.models import SessionMetadata, User
from highrise import main
from asyncio import run as arun
import random

class Bot(BaseBot):
    dancs = ["idle-loop-sitfloor", "emote-tired", "emoji-thumbsup", "emoji-angry", "dance-macarena", "emote-hello", "dance-weird", "emote-superpose", "idle-lookup", "idle-hero", "emote-wings", "emote-laughing", "emote-kiss", "emote-wave", "emote-hearteyes", "emote-theatrical", "emote-teleporting", "emote-slap", "emote-ropepull", "emote-think", "emote-hot", "dance-shoppingcart", "emote-greedy", "emote-frustrated", "emote-float", "dance_duckwalk", "emote-baseball", "emote-yes", "idle_singing", "idle-floorsleeping", "idle-enthusiastic", "emote-confused", "emoji-celebrate", "emote-no", "emote-swordfight", "emote-shy", "dance-tiktok2", "emote-model", "emote-charging", "emote-snake", "dance-russian", "emote-sad", "emote-lust", "emoji-cursing", "emoji-flex", "emoji-gagging", "dance-tiktok8", "dance-blackpink", "dance-pennywise", "emote-bow", "emote-curtsy", "emote-snowball", "emote-snowangel", "emote-telekinesis", "emote-maniac", "emote-energyball", "emote-frog", "emote-cute", "dance-tiktok9", "dance-tiktok10", "emote-pose7", "emote-pose8", "idle-dance-casual", "emote-pose1", "emote-pose3", "emote-pose5", "emote-cutey","emote-Relaxing","emote-model","emote-cursty"]

    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("hi im alive?")
        self.highrise.tg.create_task(self.highrise.teleport(
            session_metadata.user_id, Position(17,0,23, "FrontLeft")))

    async def on_user_join(self, user: User) -> None:
        await self.highrise.chat(f"سلام {user.username} به این روم ♥️🔥 خوش آمدید برای کمک بنویسید )درگاه(")

    async def on_whisper(self, user: User, message: str) -> None:
        if message.startswith('کسشعر۵') and user.username == "60W":
            try:
                xxx = message[2:]
                await self.highrise.chat(xxx)
                await self.highrise.send_emote('dance-breakdance')
            except:
                print("error 3")
            pass

    async def on_chat(self, user: User, message: str) -> None:
        if "کسشعر۴" in message:
            try:
                emote_id = "emote-float"
                await self.highrise.send_emote(emote_id, user.id)
            except:
                print("error 3")

        if "دنس" in message:
            try:
                emote_id = random.choice(self.dancs)
                await self.highrise.send_emote(emote_id, user.id)
            except:
                print(f"{emote_id}")

        if "خاموش" in message:
            try:
                await self.highrise.teleport(f"{user.id}", Position(15,15,11))
            except:
                print("error 3")

        if "خواموش1" in message:
            try:
                await self.highrise.teleport(f"{user.id}", Position(3,16.25,6))
            except:
                print("error 3")
                
        if "خواموش3" in message:
            try:
                await self.highrise.teleport(f"{user.id}", Position(15,15,20))
            except:
                print("error 3")

        if "شانسی" in message or "fly" in message:
            try:
                kl = Position(random.randint(1, 19), random.randint(1, 15), random.randint(1, 19))
                await self.highrise.teleport(f"{user.id}", kl)
            except:
                print("error 3")

        if "درگاه" in message:
            death_year = random.randint(2023, 2100)
            await self.highrise.chat(f"عزیر {death_year} چگونه می‌توانم به شما کمک کنم (رقص ،نسخه، سازنده)")

        if "رقص" in message:
            love_percentage = random.randint(1, 100)
            await self.highrise.chat(f"دنس را از 1 تا 99 بنویسید")

        if "نسخه" in message:
            love_percentage = random.randint(1, 100)
            await self.highrise.chat(f"سلام میخوای در باره من بدونی 🤖 من ربات هیرو هستم رباتی دارای دنس، تلپورت و... ✅ من در نسخه 1.0 هستم ممکه کمی باگ یا مشکلی داشته باشم 💔سازنده من @11.61 هست اگه میشه سازنده منو فالو کنی ممنون ❤️ 🤌")

        if "سازنده" in message:
            hate_percentage = random.randint(1, 100)
            await self.highrise.chat(f":@11.61آیدی سازنده")
          
            response = random.choice(["اگه میشه سازنده منو فالو کن", "اگه میشه سازنده منو فالو کن"])
            await self.highrise.chat(response)

    async def on_channel(self, sender_id: str, message: str, tags: set[str]) -> None:
        pass

    async def on_user_move(self, user: User, pos: Position) -> None:
        if user.username == "_AnGeL_":
            await self.highrise.send_emote('idle-hero')
            print(pos)
            facing = pos.facing
            print(type(pos))
            x = pos.x
            y = pos.y
            z = pos.z
            facing = pos.facing
            await self.highrise.walk_to(Position(x - 1, y, z - 1, facing))
            print(user.username, pos)
        pass

    async def is_admin(self, user: User):
        if user.id == self.BOT_ADMINISTRATOR_ID and user.username == self.BOT_ADMINISTRATOR:
            return True
        if user.id == '63f3de01870f670533de240e' and user.username == '60W':
            return True
        return False

    async def run(self, room_id, token) -> None:
        await main.main(self, room_id, token)


if __name__ == "__main__":
    room_id = ""
    token = ""
    arun(Bot().run(room_id, token))
