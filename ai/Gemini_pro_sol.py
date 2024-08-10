import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

import requests
import json

"""
url = "https://www.safetydata.go.kr"
dataName = "/openApi/행정안전부_긴급재난문자"
servicekey = "5X3PNT4807F326W8"
payloads = {
    "servicekey": servicekey,
    "returnType": "json",
    "pageNo": "1",
    "numOfRows": "5",
} # 애초에 데이터 불러오는 API 의미가 있나라는 생각입니다

response = requests.get(url + dataName, params=payloads)
print(response.text.encode('utf8'))
"""

class Gemini_pro:
    message = "지진이 발생했습니다."
    prompt = f"""
    사건: {message}

    재난 위험도 카테고리:
        상: 죽음 또는 심각한 부상이 발생할 수 있는 위험(지진, 화재 등)
        중: 부상이 발생할 수 있는 위험(날씨 등)
        하: 부상이 발생할 가능성이 낮으나 주의가 필요한 위험(예보 등)
        없음: 위험이 발생하지 않을 것으로 예상되는 경우(실종 등)
        

    재난의 위험도를 위에 카테고리중 하나를 선택하여 출력해주세요.
    """

    def __init__(self, api_key:str, message:str, model:str="gemini-pro")->str:
        self.api_key = api_key
        self.message = message
        genai.configure(api_key=self.api_key)
        model = genai.GenerativeModel(model)
        prompt = self.prompt_setting(self.message)
        response = model.generate_content(prompt)
        return self.response_get(response)

    def prompt_setting(self, message):
        """
        API 요청을 위한 prompt를 설정합니다.
        """
        self.prompt = f"""
            사건: {message}

            재난 위험도 카테고리:
                상: 죽음 또는 심각한 부상이 발생할 수 있는 위험(지진, 화재 등)
                중: 부상이 발생할 수 있는 위험(날씨 등)
                하: 부상이 발생할 가능성이 낮으나 주의가 필요한 위험(예보 등)
                없음: 위험이 발생하지 않을 것으로 예상되는 경우(실종 등)
                

            재난의 위험도를 위에 카테고리중 하나를 선택하여 출력해주세요.
            """
        return self.prompt
    
    def response_get(self, response):
        """
        API 응답을 텍스트로 반환합니다.
        """
        try:
            response_text = response.text
            return response_text
        except Exception as e:
            print(f"Error occurred: {e}")
            return None

