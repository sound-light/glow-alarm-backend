from yeelight import discover_bulbs, Bulb, LightType
import time
import threading

class BulbControl:
    @staticmethod
    def get_bulb_ips():
        bulbs = discover_bulbs()
        return [bulb['ip'] for bulb in bulbs]

    @staticmethod
    def blink_periodically(ip, interval, duration):
        bulb = Bulb(ip, auto_on=True)
        end_time = time.time() + duration
        while time.time() < end_time:
            bulb.turn_on()
            time.sleep(interval / 2)
            bulb.turn_off()
            time.sleep(interval / 2)

    @staticmethod
    def disaster_function_high_priority(ip):
        bulb = Bulb(ip, auto_on=True)
        while True:
            for brightness in [50, 70, 100]:
                bulb.set_rgb(255, 0, 0)  # 빨간색
                bulb.set_brightness(brightness)
                time.sleep(15)
                bulb.turn_off()
                time.sleep(5)

    @staticmethod
    def disaster_function_medium_priority(ip):
        bulb = Bulb(ip, auto_on=True)
        while True:
            for brightness in [10, 30, 50]:
                bulb.set_rgb(0, 0, 255)  # 파란색
                bulb.set_brightness(brightness)
                time.sleep(10)
                bulb.turn_off()
                time.sleep(5)

    @staticmethod
    def personal_alarm(ip, selected_color, duration=60):
        bulb = Bulb(ip, auto_on=True)
        end_time = time.time() + duration
        while time.time() < end_time:
            bulb.set_rgb(selected_color[0], selected_color[1], selected_color[2])
            bulb.turn_on()
            time.sleep(4)
            bulb.turn_off()
            time.sleep(1)
        bulb.turn_off()

    @staticmethod
    def start_alarm(ip, alarm_type, *args):
        if alarm_type == "high":
            thread = threading.Thread(target=BulbControl.disaster_function_high_priority, args=(ip,))
        elif alarm_type == "medium":
            thread = threading.Thread(target=BulbControl.disaster_function_medium_priority, args=(ip,))
        elif alarm_type == "personal":
            thread = threading.Thread(target=BulbControl.personal_alarm, args=(ip, *args))
        else:
            raise ValueError("Invalid alarm type")
        
        thread.start()
        return thread

    @staticmethod
    def snooze_alarm(ip, selected_color, snooze_time=300):
        time.sleep(snooze_time)  # 스누즈 시간 동안 대기
        BulbControl.personal_alarm(ip, selected_color)

    @staticmethod
    def start_alarm_with_snooze(ip, selected_color, duration=60, snooze_time=300):
        alarm_thread = threading.Thread(target=BulbControl.personal_alarm, 
                                        args=(ip, selected_color, duration))
        alarm_thread.start()
        return alarm_thread

    @staticmethod
    def snooze_current_alarm(ip, selected_color, snooze_time=300):
        BulbControl.stop_alarm(ip)  # 현재 알람 중지
        snooze_thread = threading.Thread(target=BulbControl.snooze_alarm, args=(ip, selected_color, snooze_time))
        snooze_thread.start()
        return snooze_thread

    @staticmethod
    def stop_alarm(ip):
        bulb = Bulb(ip, auto_on=True)
        bulb.turn_off()