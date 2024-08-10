

import google.generativeai as genai

import google.generativeai as genai
from datetime import datetime, timedelta



"""
import textwrap
from IPython.display import display
from IPython.display import Markdown

import requests
import json

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



class SmartAlarm:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.alarms = {}
        genai.configure(api_key=self.api_key)
        self.gemini_model = genai.GenerativeModel("gemini-pro")

    def set_alarm(self, bed_time: str, wake_up_time: str):
        prompt = f"Based on bedtime {bed_time} and wake up time {wake_up_time}, what's the optimal alarm time? Please respond with just the time in HH:MM format."
        response = self.gemini_model.generate_content(prompt)
        optimal_time = response.text.strip()
        self.store_alarm(optimal_time)
        return optimal_time

    def store_alarm(self, alarm_time: str):
        self.alarms[alarm_time] = {
            "original_time": alarm_time,
            "current_time": alarm_time,
            "snoozed": False
        }

    def snooze_alarm(self, current_time: str, situation: str):
        if not self.alarms:
            raise ValueError("No active alarm found")
        
        prompt = f"Given the current time is {current_time} and the situation is '{situation}', how many minutes should the alarm be snoozed for? Consider factors like urgency, time of day, and the described situation. Please respond with just a number (in minutes)."
        response = self.gemini_model.generate_content(prompt)
        snooze_duration = int(response.text.strip())

        current_time_obj = datetime.strptime(current_time, "%H:%M")
        closest_alarm = min(self.alarms.keys(), key=lambda x: abs(datetime.strptime(x, "%H:%M") - current_time_obj))
        
        new_alarm_time = (current_time_obj + timedelta(minutes=snooze_duration)).strftime("%H:%M")
        self.alarms[new_alarm_time] = {
            "original_time": self.alarms[closest_alarm]["original_time"],
            "current_time": new_alarm_time,
            "snoozed": True
        }
        del self.alarms[closest_alarm]
        return new_alarm_time, snooze_duration

    def get_alarms(self):
        return self.alarms