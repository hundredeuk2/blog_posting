from bs4 import BeautifulSoup
import os
import asset as ast
import requests


class preprocess:
    def __init__(self):
        
        pass
    
    def get_ids(self, prob_id, path = ast.pth):
        py_list = os.listdir(path)
        
        for name in py_list:
            # Execpt Programmers coding test file
            if "boj" not in name:
                continue
            tmp = name.split("_")[1].split(".")[0]
            if tmp in prob_id:
                continue
            
            self.n = str(tmp)
            self.trs = self.get_infomation(tmp)
            with open(path+'/'+name, 'r') as file:
                code_string = file.read()
            self.code_string = code_string
            break
            
        # return git_id
    
    def get_infomation(self, prob_n):
        
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(f'https://www.acmicpc.net/problem/{prob_n}', headers=headers)
        soup = BeautifulSoup(data.text, 'html.parser')
        trs = soup.select('#problem_description')
        
        return trs

