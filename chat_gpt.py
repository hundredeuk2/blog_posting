from langchain.chat_models import ChatOpenAI
import asset as ast
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate


class get_response:
    def __init__(self):
        self.chat = ChatOpenAI(openai_api_key=ast.openai_api_key)
        template="당신은 사용자의 코드를 참고하여 문제에 대한 풀이 글 작성을 도와주는 유용한 도우미입니다."
        system_message_prompt = SystemMessagePromptTemplate.from_template(template)
        human_template="""알고리즘 문제 풀이 블로그 글을 쓸껀데 다음 주의사항을 지키며 문제풀이 글을 작성해줘.
주의사항: 1. 글에 내 코드를 참고해줘. 2. 문제해설을 자세하게 해 줘. 3. 코드는 생성하지 말아줘.
문제: 세계적으로 유명한 엄지민 자동차 회사는 효율적인 킥다운 장치를 만들어달라는 의뢰를 받았다. 킥다운이란 자동차에서 낮은 기어로 바꾸는 장치를 의미한다. 연구 끝에 효율적인 킥다운 장치는 '이'와 '홈'이 불규칙하게 배열되어 있는 기어로 만들어져야 한다는 것을 알았다.
첫 번째 그림과 같이 두 기어 파트가 서로 마주 보고 있게 된다. 튀어나온 것이 기어의 이, 들어간 곳이 홈이다. 그리고 이들을 두 번째 그림과 같이 서로 맞물리게 끼우는 것으로 킥다운 장치를 만들 수 있다. 하지만 문제는 맞물리게 하였을 때 가로나비가 짧을수록 효율적인 킥다운 장치가 된다. 때문에 문제는 두 기어가 주어졌을 때 맞물리게 하는 가장 짧은 가로나비를 구하는 것이다. 
코드:a = str(input())
b = str(input())
줘
if len(a) < len(b):
    upper, under = b, a
else:
    upper, under = a, b
    
M, m = len(upper), len(under)   
if len(a) == 0 or len(b) == 0:
    print(M)
    exit(0)
    
def cal(curr_list,  bet, m):
    for i in range(m):
        curr = curr_list[i:]
        if len(curr) > m :
            l = m
        else:
            l = len(curr)
        for idx in range(l):
            if bet[idx] == curr[idx]:
                if bet[idx] == "2":
                    state =False
                    break
            state = True
        if state :
            break
    if not state :
        i+=1
    return i, state

right, state = cal(under, upper,m)

if state:
    right += M
else:
    right = M+m
left, state = cal(upper, under,m)

if not state:
    left = M+m
elif m + left <= M:
    left = M
else:
    left += M
    
print(min(right, left))
글: ##문제
세계적으로 유명한 엄지민 자동차 회사는 효율적인 킥다운 장치를 만들어달라는 의뢰를 받았다. 킥다운이란 자동차에서 낮은 기어로 바꾸는 장치를 의미한다. 연구 끝에 효율적인 킥다운 장치는 '이'와 '홈'이 불규칙하게 배열되어 있는 기어로 만들어져야 한다는 것을 알았다.

첫 번째 그림과 같이 두 기어 파트가 서로 마주 보고 있게 된다. 튀어나온 것이 기어의 이, 들어간 곳이 홈이다. 그리고 이들을 두 번째 그림과 같이 서로 맞물리게 끼우는 것으로 킥다운 장치를 만들 수 있다. 하지만 문제는 맞물리게 하였을 때 가로나비가 짧을수록 효율적인 킥다운 장치가 된다. 때문에 문제는 두 기어가 주어졌을 때 맞물리게 하는 가장 짧은 가로나비를 구하는 것이다.

## 입력

첫 줄에는 첫 번째 기어 파트를 나타내는 1과 2로 구성된 문자열이 주어진다. 두 번째 줄에는 마찬가지로 두 번째 기어 파트를 나타내는 1, 2로 구성된 문자열이 주어진다. 여기서 1은 홈을, 2는 이를 의미한다. 길이 <= 100

## 출력

첫 줄에 만들 수 있는 가장 짧은 가로 너비를 출력한다.
---
### Solve

문제에 조금 애매한 표현이 있는데, 맞물리는 것은 즉 이와 이끼리의 만남이 없는 상태라고 보면 된다. 즉, 2와 2가 만나면 안 된다는 뜻이다. 문제는 둘의 길이가 다르며 계속 밀면서 Fit 되는지 안되는지 확인을 해야 한다.

그러기 위해선 하나의 기어를 기준으로 좌 우로 밀면서 맞물리는지 확인을 해야 한다는 점이다. 문제 해결을 위한 로직은 다음과 같다.

1.  기어를 미는 대신 list를 순서대로 잘라서 본다.
2.  위아래 한 번씩 본다면 결국 좌 우 한번씩 확인하게 된다.
문제:{question}
코드:{code}
글:"""
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
        self.chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

    def make_response(self, trs, code_string):
        # 형식이 지정된 메시지에서 채팅 완료 가져오기
        answer = self.chat(
        self.chat_prompt.format_prompt(
            question = trs[0].text[1:-4],
            code = code_string,
        ).to_messages()
        )
        return answer