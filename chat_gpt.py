from langchain.chat_models import ChatOpenAI
import asset as ast
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate


class get_response:
    def __init__(self):
        self.chat = ChatOpenAI(openai_api_key=ast.openai_api_key)
        template="당신은 사용자의 코드를 참고하여 문제에 대한 풀이 글 작성을 도와주는 유용한 도우미입니다."
        system_message_prompt = SystemMessagePromptTemplate.from_template(template)
        human_template="알고리즘 문제 풀이 블로그 글을 쓸껀데 다음 주의사항을 지키며 문제풀이 글을 작성해줘.\n주의사항: 1. markdown형식으로 작성해줘. 2. 글에 내 코드를 참고해줘. 3. 코드는 전체를 한번만 작성하고 다음엔 작성하지 말아줘. 4. 문제해설을 자세하게 해 줘. 5. 코드를 제외하곤 ```를 사용하지 말아줘. \n문제:{question}\n코드:{code}"
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