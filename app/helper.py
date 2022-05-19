import os
import json
from languages import lang_ext

path = 'submissions'
def save(path, filename, content):
    with open(os.path.join(path, filename), 'w+') as file:
        file.write(content)


def dumb_visited_problems():
    with open('history.json', 'w+') as file:
        json.dump(visited_problems, file)

def load_visited_problems():
    try:
        with open('history.json', 'r+') as file:
            new_dict = json.load(file)
    except ValueError:
        new_dict = {} 
    return new_dict

def process_data(data):
    for submission in data.get('submissions_dump'):
        problem_name = submission.get('title_slug')
        filename = problem_name + '.' + lang_ext.get(submission.get('lang'), submission.get('lang'))
        code = submission.get('code')
        if submission.get('status_display') != 'Accepted' or visited_problems.get(problem_name, False) == True:
            continue
        save(path, filename, code)
        visited_problems[problem_name] = True


visited_problems = load_visited_problems()