import random

answers = ["The outcome is good", "It seems so", "I am not sure","Yes", "No", "Dont count on it","Try asking someone else","I would assume so","I must have misplaced your answer'","The answer is not what you want to hear","Ask again later","Not very likely","You have nothing to worry about","Very doubtful","Most likely"]
question = 'What is your question? '

def prompt_question(question):
    response = raw_input(question)
    print random.choice(answers)

prompt_question(question)
