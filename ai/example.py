from Gemini_pro_sol import Gemini_pro, SmartAlarm

print(Gemini_pro(api_key="API_KEY", message="지진이 발생했습니다."))

API_KEY = "GOOGLE_API_KEY"

# 재난 알림 테스트
disaster_alert = Gemini_pro(api_key=API_KEY, message="지진이 발생했습니다.")
print(f"재난 위험도: {disaster_alert}")

# 스마트 알람 테스트
smart_alarm = SmartAlarm(api_key=API_KEY)
optimal_time = smart_alarm.set_alarm("22:00", "07:00")
print(f"최적 알람 시간: {optimal_time}")

new_alarm_time, snooze_duration = smart_alarm.snooze_alarm("07:00", "조금 더 자고 싶어요")
print(f"스누즈 후 새 알람 시간: {new_alarm_time}, 스누즈 시간: {snooze_duration}분")

alarms = smart_alarm.get_alarms()
print("현재 설정된 알람들:", alarms)