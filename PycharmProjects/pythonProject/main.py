import telebot
import random

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
bot = telebot.TeleBot('6507633562:AAGCCpLunfI-0saYn7gXXi9pka7bHMeTC4w')

def generateQuestions(num):
    q = []
    for n1 in range(1, num):
        n1=random.randint
        n1=random.randint(1,120)
        n2 = random.randint(1, 120)
        for op in range(4):
            if op == 0:
                L = [random.randint(n1 + n2 - 25, n1 + n2 + 25), n1 + n2,
                random.randint(n1 + n2 - 25, n1 + n2 + 25)]
                random.shuffle(L)
                q.append({"question": str(n1) + "+" + str(n2),
                              "options": L,
                              "correct_option": str(n1 + n2)})
            elif op == 1:
                L = [random.randint(n1 - n2 - 25, n1 - n2 + 25), n1 - n2,
                     random.randint(n1 - n2 - 25, n1 - n2 + 25)]
                random.shuffle(L)
                q.append({"question": str(n1) + "-" + str(n2),
                              "options": L,
                              "correct_option": str(n1 - n2)})
                # elif op == 0:
                # L = [random.randint(n1 + n2 - 25, n1 + n2 + 25), n1 + n2,
                #     random.randint(n1 + n2 - 25, n1 + n2 + 25)]
                # random.shuffle(L)
                # q.append({"question": str(n1) + "+" + str(n2),
                #          "options": L,
                #          "correct_option": str(n1 + n2)})
                # elif op == 0:
                #    L = [random.randint(n1 + n2 - 25, n1 + n2 + 25), n1 + n2,
                #         random.randint(n1 + n2 - 25, n1 + n2 + 25)]
                #    random.shuffle(L)
                #    q.append({"question": str(n1) + "+" + str(n2),
                #              "options": L,
                #              "correct_option": str(n1 + n2)})
    return q
questions=generateQuestions(20)
# Список вопросов для викторины
userquestions = [
    {
        'question': 'Сколько планет в Солнечной системе?',
        'options': ['7', '8', '9', '10'],
        'correct_option': '8'
    },
    {
        'question': 'Какой год основания Рима?',
        'options': ['753 до н. э.', '476 г. н. э.', '1492 г.', '1945 г.'],
        'correct_option': '753 до н. э.'
    },
    {
        'question': 'Кто автор произведения "Война и мир"?',
        'options': ['Лев Толстой', 'Федор Достоевский', 'Иван Тургенев', 'Александр Пушкин'],
        'correct_option': 'Лев Толстой'
    },
    {
        'question': 'Сколько континентов на Земле?',
        'options': ['5', '6', '7', '8'],
        'correct_option': '7'
    },
    {
        'question': 'Какое химическое обозначение углекислого газа?',
        'options': ['CO', 'CO2', 'O2', 'CH4'],
        'correct_option': 'CO2'
    },
    {
        'question': 'Кто написал "Рomeo and Juliet"?',
        'options': ['Charles Dickens', 'Jane Austen', 'William Shakespeare', 'Mark Twain'],
        'correct_option': 'William Shakespeare'
    },
    {
        'question': 'В каком году произошло Октябрьское восстание в России?',
        'options': ['1905', '1917', '1921', '1933'],
        'correct_option': '1917'
    },
    {
        'question': 'Какой химический элемент обозначается как Fe?',
        'options': ['Железо', 'Свинец', 'Золото', 'Серебро'],
        'correct_option': 'Железо'
    },
    {
        'question': 'Сколько миллисекунд в одной секунде?',
        'options': ['10', '100', '1000', '10000'],
        'correct_option': '1000'
    },
    {
        'question': 'Кто изображен на американской купюре в 100 долларов?',
        'options': ['Авраам Линкольн', 'Джордж Вашингтон', 'Бенджамин Франклин', 'Томас Джефферсон'],
        'correct_option': 'Бенджамин Франклин'
    }
]
for q in userquestions:
    questions.append(q)
# Словарь для хранения ответов пользователя
user_answers = {}

# Текущий номер вопроса
current_question = 0
random.shuffle(questions)
# Обработчик сообщений от пользователя
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    global current_question

    # Если еще есть вопросы в викторине
    if current_question < len(questions):
        # Отправляем текущий вопрос с вариантами ответов
        question_data = questions[current_question]
        options = question_data['options']
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        random.shuffle(options)
        for option in options:
            markup.add(telebot.types.KeyboardButton(option))
        bot.send_message(message.chat.id, question_data['question'], reply_markup=markup)
        # Регистрируем обработчик для следующего шага (ввода ответа)
        bot.register_next_step_handler(message, handle_answer)
    else:
        # Викторина завершена, отправляем результат
        correct_answers = sum([1 for user_answer in user_answers.values() if user_answer])
        bot.send_message(message.chat.id, f'Игра завершена. Правильных ответов: {correct_answers}/{len(questions)}')
        # Перезапускаем викторину
        #restart_quiz(message)

# Обработчик ввода ответа от пользователя
def handle_answer(message):
    global current_question

    # Если еще есть вопросы в викторине
    if current_question < len(questions):
        # Проверяем ответ пользователя
        question_data = questions[current_question]
        correct_option = question_data['correct_option']
        user_answer = message.text

        if user_answer == correct_option:
            user_answers[current_question] = True
            bot.send_message(message.chat.id, 'Правильно!')
        else:
            user_answers[current_question] = False
            bot.send_message(message.chat.id, f'Неправильно. Правильный ответ: {correct_option}')

        current_question += 1
        handle_message(message)
def restart_quiz(message):
    global current_question,user_answers,questions
    current_question=0
    user_answers={}
    random.shuffle(questions)
    bot.send_message(message.chat.id,"игра перезапущенна,начнем заново")
    questions=generateQuestions(20)
# Запуск бота
if __name__ == "__main__":
    bot.polling(none_stop=True)