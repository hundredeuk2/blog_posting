import requests
import asset as ast
import json
from collections import OrderedDict

class create_data:
    def __init__(self):
        self.data = OrderedDict()
        self.ids = []
    
    def make_id(self):
        for i in range(1,4):
            tmp = f"https://www.tistory.com/apis/post/list?access_token={ast.access_token}&output=json&blogName={ast.blog_name}&page={i}"
            response = requests.get(tmp)
            data = response.json()['tistory']['item']['posts']
            for j in range(len(data)):
                if data[j]['categoryId'] != ast.category_id:
                    continue
                elif "백준" not in data[j]['title']:
                    continue
                id = data[j]['title'].split(" ")[1]
                self.ids.append(id)
                
    def make_json(self):
        self.make_id()
        self.data['data'] = self.ids        
        with open("prob_id.json", "w") as json_file:
            json.dump(self.data, json_file)