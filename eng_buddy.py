from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
import asyncio

# Токен от BotFather
TOKEN = '7765585073:AAE-fTowt5dIg3aXBhFdOPjQbyxqjtFiXVA'

# Создание бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработка команды /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привет! Я бот. Помогу тебе изучить английский. Чем могу помочь?\nЧтобы узнать, что я умею, напиши /help")

# Обработка команды /start
@dp.message(Command("grammar"))
async def cmd_start(message: Message):
    await message.answer("Привет! Начнем с грамматики. Какой аспект тебя интересует?\n1. /Past\n2./Present\n3./Future")

# Обработка команды /irregular
@dp.message(Command("irregular_verbs"))
async def cmd_start(message: Message):
    await message.answer("Вот список неправильных глаголов:\n1. be - was/were - been\n2. go - went - gone\n3. have - had - had\n4. do - did - done\n5. see - saw - seen\n6. take - took - taken\n7. become – became – become\n8. come - came - come\n9. get - got - got/gotten\n10. make - made - made\n11. say - said - said\n12. know - knew - known\n13. think - thought - thought\n14. give - gave - given\n15. find - found - found\n16. tell - told - told\n17. feel - felt - felt\n18. leave - left - left\n19. put - put - put\n20. bring – brought – brought")

# Обработка команды /Conditions.
@dp.message(Command("Conditions"))
async def cmd_start(message: Message):
    await message.answer("\n1. /ZeroConditional\n2. /FirstConditional\n3. /SecondConditional\n4. /ThirdConditional")

# Обработка команды /Past
@dp.message(Command("Past"))
async def cmd_start(message: Message):
    await message.answer("\n1. /PastSimple\n2. /PastContinuous\n3. /PastPerfect")

# Обработка команды /PastSimple
@dp.message(Command("PastSimple"))
async def cmd_start(message: Message):
    await message.answer("We use the past simple when we want to talk about action that happened before. \n Mostly the past simple ends in -ed ( regular verb ) \nShe visited her grandparents last weekend.\nThey watched a movie last night.\nHe finished his homework an hour ago.\nIn examples we can see that most of the verbs end with -ed. \nBut many verbs do not end with -ed, so we can use irregular verbs. \nGo → Went → Gone\nHave → Had → Had\nDo → Did → Done\nSay → Said → Said\nGet → Got → Got/Gotten\nMake → Made → Made\nTake → Took → Taken\nSee → Saw → Seen\nCome → Came → Come\nGive → Gave → Given\nYes/No Questions\nFormula:\n•	Did + subject + base verb + ?\nExamples:\n•	Did you go to school yesterday?\n•	Did she watch the movie?\nWh- Questions (with question words)\nFormula:\n•	Wh-word + did + subject + base verb + ?\nExamples:\n•	What did you eat for dinner?\n•	Where did he travel last summer?")

# Обработка команды /PastContinuous
@dp.message(Command("PastContinuous"))
async def cmd_start(message: Message):
    await message.answer("We use the past continuous when we wanna talk about specific moments that were happening at a specific moment in the past.\nAt 6 p.m I was walking around the city.\nmy friends, when it was raining.\nAlso we use it at two actions that were happening at the same time in the past. \nWhile I was sleeping, she was doing her homework. \nWhile he was working out, his girlfriend was baking for him. \nFor interacting actions in the past.\nI was playing video games, when my friends called me. \nI was doing my homework, when my sister interrupted me. \nEx: \nDuring Eurovision 2024, people were watching the performances on TV. The singers were performing their songs with great energy. While the audience was cheering, the judges were giving their scores.\nWas/were + ing is the past continuous \nHe/she/it ( was ) cheering \nWe/you/they ( were) performing")

# Обработка команды /PastPerfect
@dp.message(Command("PastPerfect"))
async def cmd_start(message: Message):
    await message.answer("Formula: Subject + had + past participle (V3)\nYou use the Past Perfect tense to show that one action happened before another action or time in the past.\nShe had already left when I arrived.\nWe had finished dinner before the movie started.\nYes/no questions \nFormula: Had + subject + past participle (V3)?\nExamples:\nHad you eaten before the movie started?\nHad she finished her homework when you called?\nWh- questions \nWh-word + had + subject + past participle?\nExamples: \nWhat had he done before he got fired?\nWhere had you been before the party?")


# Обработка команды /Present
@dp.message(Command("Present"))
async def cmd_start(message: Message):
    await message.answer("\n1. /PresentSimple\n2. /PresentContinuous\n3. /PresentPerfect")

# Обработка команды /PresentSimple
@dp.message(Command("PresentSimple"))
async def cmd_start(message: Message):
    await message.answer("We use Present Simple ,when we wanna talk about basic facts.\nThe sun rises in the east.\nWe also use it  for habits and routines. (with adverbs like always, usually, often, sometimes, never)    \nI drink coffee every day. ( It’s not happening right now, this sentence shows that the action happens every day. Not right now ) \nFor scheduled events (like timetables, programs, or schedules)\nThe movie starts at 8 o’clock.\nFor instructions or directions\nFirst, you mix the flour and sugar.\nFor feelings, thoughts, and states (non-action verbs like love, know, need, believe ) \nI like this song \nFormula for Wh- Questions (with question words):\nWh-word + be (am/is/are) + subject + verb-ing + ?\nExamples:\n•	What are you doing?\n•	Where is she going?")

# Обработка команды /PresentContinuous
@dp.message(Command("PresentContinuous"))
async def cmd_start(message: Message):
    await message.answer("We use Present continuous, when we wanna say that something is happening right now.\nEx: \n1.	She is reading a book right now.\n2.	They are playing soccer in the park.\n3.	I am cooking dinner at the moment\nHe’s swimming in the pool. (He is swimming…..) \nThat means, the action is happening right now. \nThe action is not finished. \nI am ( =I’m ) verb + ing \nHe/she/it ( =he’s ) verb + ing \nWe/you/they ( =they’re ) verb + ing \nFormula for Yes/No Questions:\nBe (am/is/are) + subject + verb-ing + ?\nExamples:\n•	Are you studying English?\n•	Is she watching TV?")

# Обработка команды /PresentPerfect
@dp.message(Command("PresentPerfect"))
async def cmd_start(message: Message):
    await message.answer("Structure:\nSubject + have/has + past particle\nI/we/they/you have (= I’ve etc.) \nhe/she/it has (= he’s etc.)\nWe use the present perfect tense when talking about an action that happened in the past, but we don’t know when it happened.\nI have visited Paris.\nShe has seen that movie.\nAlso we use it for action that happened in the past, and continues into the present.  \nHe has lived here for five years.\nWe have known each other since childhood")

# Обработка команды /Future
@dp.message(Command("Future"))
async def cmd_start(message: Message):
    await message.answer("\n1. /FutureSimple\n2. /FutureContinuous\n3. /FuturePerfect")

# Обработка команды /FutureSimple
@dp.message(Command("FutureSimple"))
async def cmd_start(message: Message):
    await message.answer("Formula: Subject + will + base form of the verb \nWe use future simple to describe an action, that will happen in future. In future simple we use verbs like “will” and “be going to”. \nYes/No Question\nFormula: Will + subject + base form of the verb?\nExamples:\n•	Will you travel to Paris?\n•	Will she start a new job?\nWh- questions \nFormula: \nWh- word (e.g., What, When, Where) + will + subject + base form of the verb?\nExamples:\n	•	What will you do tomorrow?\n	•	When will she start her new job?")

# Обработка команды /FutureContinuous
@dp.message(Command("FutureContinuous"))
async def cmd_start(message: Message):
    await message.answer("Future continuous talks about something that will be happening at a certain time in the future.\nFormula: \nSubject + will be + verb+ing\nExamples:\n	we•	I will be sleeping at 10 PM.\n	•	She will be studying tomorrow.\nQuestions yes/no:\nFormula: Will + subject + be + verb-ing + ?\nExamples:\n	•	Will you be working tomorrow?\n	•	Will she be watching the movie?\nWh- questions \nFormula: Wh- Questions (with question words):\nWh-word + will + subject + be + verb-ing + ?\nExample:\n•	 What will you be doing at 6 PM?\n•	Where will she be going tomorrow?")

# Обработка команды /FuturePerfect
@dp.message(Command("FuturePerfect"))
async def cmd_start(message: Message):
    await message.answer("The future perfect tense describes actions that will be completed before a specific time in the future. It’s like setting a deadline for an action to finish. \nStcuture: Subject + will have + past participle + [rest of the sentence]\nExamples:\nI will have completed the report by Friday.\nShe will have left before you arrive.\nThey will have built the house by next year.\nYes/No Questions\nStructure:Will + subject + have + past participle + [rest of the sentence]?\nExamples:\n•	Will you have eaten by 8 PM?\n•	Will she have arrived before the meeting starts?\nWh- Questions\nStructure:Wh-word + will + subject + have + past participle + [rest of the sentence]?\nExamples:\n•	What will you have done by then?\n•	Where will they have gone by tomorrow? ")

# Обработка команды /ZeroConditional
@dp.message(Command("ZeroConditional"))
async def cmd_start(message: Message):
    await message.answer("We use zero when we’re talking about facts. \nStructure: if + present simple + present simple \nEx: \nIf you put water in a freezer, it freezes.\nIf you heat water to 100°C, it boils. \nWhen the sun sets, it gets dark.\nIn these examples we can see the basic facts. And that’s zero condition about. ")

# Обработка команды /FirstConditional
@dp.message(Command("FirstConditional"))
async def cmd_start(message: Message):
    await message.answer("We’re using the first condition, when we give a stipulation. \nStructure: if + present simple + future simple \nEx: \nIf you study hard, you will pass the exam.\nIf she arrives early, we will start the meeting.\nIf we leave now, we might catch the early train. \nSo by these examples we can understand that the first construction is about stipulation. And all of them say things like “ if it happens, we will do it”. ")

# Обработка команды /SecondConditional
@dp.message(Command("SecondConditional"))
async def cmd_start(message: Message):
    await message.answer("We use the second conditional when we are talking about an action that non- possible or unlikely to happen. \nStructure: If + past simple + would/could/might + verb \nEx: \nIf I won the lottery, I would travel the world.\nIf he were taller, he would be a basketball player.\nIf I were a citizen of the U.A.E, I could travel around the world without a visa. \nIn these examples we can see that the action is unlikely to happen")

# Обработка команды /ThirdConditional
@dp.message(Command("ThirdConditional"))
async def cmd_start(message: Message):
    await message.answer("We use the third condition, when we talk about regrets.\nStructure: If + past perfect, would have + past participle\nEx: \nIf I had studied harder, I would have passed the exam.\nIf she had left earlier, she would have caught the train.\nIf they had invited us, we would have attended the party.\nIn this examples we can see that, mostly they are about regrets.")


# Обработка команды /help
@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Вот что я умею:\n/start — начать работу\n/help — помощь\n/grammar - правила грамматики\n/irregular_verbs - неправильные глаголы\n/Conditions - условия")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())