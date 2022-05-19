import requests
import time
from cookies import cookieHelper
from helper import process_data, dumb_visited_problems

def app():
    cookies = cookieHelper()
    if cookies == None:
        print("No cookies found!!")
        return

    with requests.Session() as s:
        url = 'https://leetcode.com/api/submissions/'
        params = {
            'offset' : 0,
            'limit'  : 20,
            'lastkey': ''
        }
        response = s.get(url, cookies=cookies, params=params)
        print('...Processing...')
        while response.ok:
            data = response.json()
            process_data(data)  
            if data.get('has_next'):
                params['offset'] += 20
                params['lastkey'] = data.get('last_key')
                time.sleep(2.5)
                response = s.get(url, cookies=cookies, params=params)
            else:
                print('...Done...')
                break
        else:
            print('Request Problem...\nstatus_code: ', response.status_code, sep='', end='\n')
        dumb_visited_problems()



if __name__ == '__main__':
    app()


    




