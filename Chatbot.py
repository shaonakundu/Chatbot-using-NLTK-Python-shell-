from nltk.chat.util import Chat, reflections
pairs = [
            [r"my name is (.*)",["Hello %1. How are you"]],
            ["(what's your name?)", ["My name is Robo"]],
            ["(hey|hola|hi|hello)",[" Hi there.", "How can I help?", "hey, good to see you", "How may i assist you today"]],
            ["(how are you?|Hope you are safe)",["I am good, thanks","I am safe and sound"]],
            ["(Can we talk for sometime?|lets's talk|Let us know about each other)",["Yea sure, so what you wanna talk","Go ahead", "sure. let's talk"]],
            ["(where do you live?|where do you stay?|where are you from?|you belong from which place?)", ["I am from Kolkata, West Bengal and you are from which place?", "I stay in Kolkata, WB. So where do you stay?"]],
            ["(I am from Shaktinagar,UP)", ["Oh thats's great"]],
            ["(What's your favourite food?|what do you love to eat?|what's your fav dish?)", ["I love authentic Bengali food that is Mishti Pulao with Kosha Mangsho. what's your fav dish?"]],
            ["(I am a foodie so i eat everything|I love Buli Daal and Aloo posto)", ["That sounds cool"]],
            ["(What are your hobbies?|what do you do in your free time?)", ["Well I love interacting with people. But also love reading books and singing. what about you?"]],
            ["(I love playing guitar, dancing , painting)", ["Wow, you are really talented"]],
            ["(It was nice talking to you|Felt good chatting with you)", ["Same here.It was really fun to chat with you"]],
            ["(Goodbye|bye|bye,bye|Tata|Bye, see you soon)", ["Goodbye. See you soon"]]
        ]
def Chatbot():
    print("Hi, I am your chatbot built using nltk module")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

if __name__ == '__main__':
    Chatbot()
