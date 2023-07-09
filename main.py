import json
import get_info
import chat_gpt
import requests
import create_blog
# init

def main():
    try :
        with open("prob_id.json", "r") as data:
            prob_ids = json.load(data)
        print("데이터를 불러옵니다.")
    except:
        from first import create_data
        tmp = create_data()
        tmp.make_json()
        prob_ids = tmp.data
        print("데이터를 새로 생성합니다.")
        
    print("생성해야 할 문제 번호를 파악 완료했습니다.")
    mode = get_info.preprocess()
    mode.get_ids(prob_ids['data'])
    
    url = "https://solved.ac/api/v3/problem/show"
    querystring = {"problemId": mode.n}
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers, params=querystring)
    response = response.json()

    print("chat_gpt를 활용해서 글을 만들고 있습니다.")
    gpt = chat_gpt.get_response()
    answer = gpt.make_response(mode.trs, mode.code_string)
    title = f"백준 {response['problemId']} {response['titleKo']} (Python / 파이썬)"
    print(answer.content)
    contents = "\n**이 글은 Chat-GPT 3.5에 의해 자동으로 생성된 블로그 글 입니다. 완벽한 정보가 아닐 수 있음을 알려드립니다.**\n"+answer.content +f"###전체코드\n```\n{mode.code_string}\n```"
    
    print("글을 포스팅 중입니다...!")
    create_blog.posting(title, contents)
    
    # prob_ids['data'].append(mode.n)
    # with open("./prob_id.json", "w") as make_file:
    #     json.dump(prob_ids, make_file)
        

if __name__=='__main__':
    ## ex) python3 train.py 
    main()