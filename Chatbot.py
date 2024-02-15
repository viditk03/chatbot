from difflib import get_close_matches


def get_best_match(user_question: str, questions: dict) -> str | None:
    """Compares the user message similarity to the ones in the dictionary"""

    questions: list[str] = [q for q in questions]
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)

    # Return the first best match, else return None
    if matches:
        return matches[0]


def chatbot(knowledge: dict):
    """Chatbot"""

    while True:
        user_input: str = input('You: ')

        # Finds the best match, otherwise returns None
        best_match: str | None = get_best_match(user_input, knowledge)

        # Gets the best match from the knowledge base
        if answer := knowledge.get(best_match):
            print(f'Bot: {answer}')
        else:
            print('Bot: I don\'t understand... Could you try rephrasing that?')


if __name__ == "__main__":
    brain: dict = {'hello': 'Hey there!',
                   'how are you?': 'I am good, thanks!',
                   'who is the hod of department?': 'Dr.Hemant Tulkar',
                   'what can you do?': 'I can answer questions!',
                   'which department is this ': 'Department of Emerging Technology',
                   'how many branches are there in this department':'There are 2 branches that comes under Emerging Technology that are the first one is "Aiml" and second is "Aids" ',
                   'how many faculties are they in department' : 'There are total 14 faculties available in deaprtment like:-'
                   '1. HOD sir Dr.Hemant tulkar'
                   '2. Ravi .s.r.t sir'
                   '3. Mayuri mam'
                   '4. Ashish nanotkar sir'
                   '5. Vivek sir'
                   '6. Alok sir'
                   '7. Ashish golghate sir'
                   '8. Neha mam'
                   '9. Vijaya mam'
                   '10. Ashwini mam'
                   '11. Hrushikesh sir'
                   '12. Akash dhok sir'
                   '13. Kalyani mam'
                   '14. Yogesh narekar sir',
                   'which faculty teaches which/what subjects' : 'For examples like: Mayuri mam teaches "oops" and kalyani mam teaches "Python" likewise vivek sir teaches "Toc" and etc', 
                   'what is the roll no/ registration no of vidit khairkar' : 'vidit khairkar roll no/ registraton no is "AM22D006"',
                   'who is the president and vice president of department ' : 'Our president is mrs.Hemani and vice president is mr.Himanshu ',
                   'ok': 'Great.' }

    chatbot(knowledge=brain)