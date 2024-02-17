from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from chatterbot.logic import BestMatch
import json

# Load the JSON data
with open('responses.json', 'r') as file:
    data = json.load(file)

# # Create a ChatBot instance with a custom logic adapter
# chatbot = ChatBot('MyBot', logic_adapters=[
#     {
#         'import_path': 'chatterbot.logic.BestMatch',
#         'default_response': 'I am sorry, but I do not understand.',
#         'maximum_similarity_threshold': 0.90
#     }
# ])

# Create a ListTrainer and train the bot with the patterns and responses from the JSON data
# corpus_trainer = ChatterBotCorpusTrainer(chatbot)
# trainer = ListTrainer(chatbot)
for intent in data['intents']:
    patterns = intent['patterns']
    responses = intent['responses']
    for pattern in patterns:
        print([pattern] + responses)

# Now you can use the chatbot to get responses
# while True:
#     user_input = input("You: ")
#     if user_input.lower() == 'exit':
#         break
#     response = chatbot.get_response(user_input)
#     print("Bot:", response)
