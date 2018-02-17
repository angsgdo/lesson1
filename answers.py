answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}

def get_answer(question):
    if question in answers:
        return answers[question]

print(get_answer(input('Напишите что-нибудь').lower()))