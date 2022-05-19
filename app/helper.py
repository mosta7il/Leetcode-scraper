import os
from languages import lang_ext
visited_problems = {}

path = 'submissions'

def process_data(data):
    for submission in data.get('submissions_dump'):
        problem_name = submission.get('title_slug')
        filename = problem_name + '.' + lang_ext.get(submission.get('lang'), submission.get('lang'))
        code = submission.get('code')
        if submission.get('status_display') != 'Accepted' or visited_problems.get(problem_name, False) == True:
            continue
        save(path, filename, code)
        visited_problems[problem_name] = True

def save(path, filename, content):
    with open(os.path.join(path, filename), 'w+') as file:
        file.write(content)
        