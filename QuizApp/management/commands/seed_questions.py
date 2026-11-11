from django.core.management.base import BaseCommand
from QuizApp.models import Question, Choice



data = [
    # easy(10)
    {
        "difficulty": "easy",
        "text": "Which keyword is used to define a function in Python?",
        "choices": ["function", "def", "define", "fun"],
        "correct": 1
    },
    {
        "difficulty": "easy",
        "text": "Which data type is used to store True or False?",
        "choices": ["int", "str", "bool", "float"],
        "correct": 2
    },
    {
        "difficulty": "easy",
        "text": "What is the output of print(2 ** 3)?",
        "choices": ["6", "8", "9", "5"],
        "correct": 1
    },
    {
        "difficulty": "easy",
        "text": "Which symbol is used for comments in Python?",
        "choices": ["//", "/*", "#", "--"],
        "correct": 2
    },
    {
        "difficulty": "easy",
        "text": "Which method adds an element to the end of a list?",
        "choices": ["add()", "insert()", "append()", "extend()"],
        "correct": 2
    },
    {
        "difficulty": "easy",
        "text": "What is the output of len('Python')?",
        "choices": ["5", "6", "7", "8"],
        "correct": 1
    },
    {
        "difficulty": "easy",
        "text": "Which function is used to display output in Python?",
        "choices": ["input()", "print()", "display()", "show()"],
        "correct": 1
    },
    {
        "difficulty": "easy",
        "text": "Which of these is a valid Python list?",
        "choices": ["(1, 2, 3)", "{1, 2, 3}", "[1, 2, 3]", "<1, 2, 3>"],
        "correct": 2
    },
    {
        "difficulty": "easy",
        "text": "What is the output of 10 // 3?",
        "choices": ["3.33", "3", "1", "4"],
        "correct": 1
    },
    {
        "difficulty": "easy",
        "text": "Which keyword is used to create a loop over a sequence?",
        "choices": ["repeat", "loop", "for", "iterate"],
        "correct": 2
    },

    # medium (10)
    {
        "difficulty": "medium",
        "text": "What is the output of [1, 2, 3][::-1]?",
        "choices": ["[1, 2, 3]", "[3, 2, 1]", "[2, 1, 3]", "[3, 1, 2]"],
        "correct": 1
    },
    {
        "difficulty": "medium",
        "text": "Which method returns all dictionary keys?",
        "choices": ["values()", "items()", "keys()", "get()"],
        "correct": 2
    },
    {
        "difficulty": "medium",
        "text": "What is the output of bool([])?",
        "choices": ["True", "False", "None", "Error"],
        "correct": 1
    },
    {
        "difficulty": "medium",
        "text": "What does the enumerate() function return?",
        "choices": [
            "Only values",
            "Only indexes",
            "Index-value pairs",
            "A sorted list"
        ],
        "correct": 2
    },
    {
        "difficulty": "medium",
        "text": "What is the output of list(set([1, 2, 2, 3])) in terms of elements?",
        "choices": [
            "[1, 2, 2, 3]",
            "[1, 2, 3]",
            "[1, 1, 2, 3]",
            "[2, 3]"
        ],
        "correct": 1
    },
    {
        "difficulty": "medium",
        "text": "Which operator checks whether two variables refer to the same object?",
        "choices": ["==", "is", "in", "! ="],
        "correct": 1
    },
    {
        "difficulty": "medium",
        "text": "What is the output of 'Python'.lower()?",
        "choices": ["PYTHON", "python", "Python", "pYTHON"],
        "correct": 1
    },
    {
        "difficulty": "medium",
        "text": "What does the zip() function do?",
        "choices": [
            "Sorts multiple lists",
            "Combines iterables element by element",
            "Removes duplicate values",
            "Reverses a sequence"
        ],
        "correct": 1
    },
    {
        "difficulty": "medium",
        "text": "What is the output of [x * 2 for x in range(3)]?",
        "choices": [
            "[0, 1, 2]",
            "[2, 4, 6]",
            "[0, 2, 4]",
            "[0, 2, 4, 6]"
        ],
        "correct": 2
    },
    {
        "difficulty": "medium",
        "text": "Which exception occurs when accessing a missing dictionary key using square brackets?",
        "choices": [
            "IndexError",
            "ValueError",
            "KeyError",
            "TypeError"
        ],
        "correct": 2
    },

    # hard(10)
    {
        "difficulty": "hard",
        "text": "What is the output of this code?\n\nx = [1, 2, 3]\ny = x\ny.append(4)\nprint(x)",
        "choices": [
            "[1, 2, 3]",
            "[1, 2, 3, 4]",
            "[4]",
            "Error"
        ],
        "correct": 1
    },
    {
        "difficulty": "hard",
        "text": "What is the output of print(2 ** 3 ** 2)?",
        "choices": ["64", "512", "256", "36"],
        "correct": 1
    },
    {
        "difficulty": "hard",
        "text": "What is the output of this code?\n\nx = [1, 2, 3]\nprint(x[-2])",
        "choices": ["1", "2", "3", "Error"],
        "correct": 1
    },
    {
        "difficulty": "hard",
        "text": "What is the output of this code?\n\ndef add(x, values=[]):\n    values.append(x)\n    return values\n\nprint(add(1))\nprint(add(2))",
        "choices": [
            "[1] then [2]",
            "[1] then [1, 2]",
            "[1, 2] then [1, 2]",
            "Error"
        ],
        "correct": 1
    },
    {
        "difficulty": "hard",
        "text": "What is the output of this code?\n\nprint([i for i in range(5) if i % 2 == 0])",
        "choices": [
            "[1, 3]",
            "[0, 2, 4]",
            "[2, 4]",
            "[0, 1, 2, 3, 4]"
        ],
        "correct": 1
    },
    {
        "difficulty": "hard",
        "text": "Which statement about Python generators is correct?",
        "choices": [
            "They always return a list",
            "They use yield to produce values lazily",
            "They cannot be used in loops",
            "They store all values in memory immediately"
        ],
        "correct": 1
    },
    {
        "difficulty": "hard",
        "text": "What is the output of print(type(lambda x: x))?",
        "choices": [
            "<class 'function'>",
            "<class 'lambda'>",
            "<class 'method'>",
            "<class 'object'>"
        ],
        "correct": 0
    },
    {
        "difficulty": "hard",
        "text": "What is the output of this code?\n\nx = {1, 2, 3}\ny = {2, 3, 4}\nprint(x & y)",
        "choices": [
            "{1, 2, 3, 4}",
            "{1, 4}",
            "{2, 3}",
            "{1, 2, 3}"
        ],
        "correct": 2
    },
    {
        "difficulty": "hard",
        "text": "What is the output of this code?\n\nclass A:\n    value = 10\n\na = A()\na.value = 20\nprint(A.value, a.value)",
        "choices": [
            "20 20",
            "10 20",
            "10 10",
            "20 10"
        ],
        "correct": 1
    },
    {
        "difficulty": "hard",
        "text": "What is the output of this code?\n\nx = [1, 2, 3, 4, 5]\nprint(x[1:4:2])",
        "choices": [
            "[1, 3]",
            "[2, 4]",
            "[2, 3, 4]",
            "[1, 2, 3, 4]"
        ],
        "correct": 1
    }
]

class Command(BaseCommand):
    help = 'Send the database with quiz questions.'

    def handle(self, *args, **kwargs):
        created_question = 0
        for item in data:
            q, created = Question.objects.get_or_create(
                text=item['text'],
                difficulty=item['difficulty']
            )
            if created:
                created_question += 1

            if q.choices.count() == 0:
                for idx, choice_text in enumerate(item["choices"]):
                    is_correct = (idx == item["correct"])
                    Choice.objects.create(
                        question=q, 
                        text=choice_text, 
                        is_correct=is_correct,
                    )
        self.stdout.write(self.style.SUCCESS(f'Seeding Completed. {created_question} questions added.'))
