import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time=0.01, verbose=False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def number_to_dac(self, number):
        binary_list = [int(element) for element in bin(number)[2:].zfill(8)]
        GPIO.output(self.bits_gpio, binary_list)

    # --- Задание 1: Метод ПС ---
    def sequential_counting_adc(self):
        for number in range(256):
            self.number_to_dac(number)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio) == 1:
                return number
        return 255

    def get_sc_voltage(self):
        number = self.sequential_counting_adc()
        return (number / 255.0) * self.dynamic_range

    # --- Задание 4: Метод ПП ---
    def successive_approximation_adc(self):
        low = 0
        high = 255
        result = 255
        while low <= high:
            mid = (low + high) // 2
            self.number_to_dac(mid)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio) == 1:
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result

    def get_sar_voltage(self):
        number = self.successive_approximation_adc()
        return (number / 255.0) * self.dynamic_range

if __name__ == "__main__":
    # Для проверки задания 1 и 4 (вывод в консоль)
    adc = R2R_ADC(3.183, compare_time=0.0001, verbose=False)
    print("Тест АЦП (нажмите Ctrl+C для выхода). Крутите потенциометр.")
    try:
        while True:
            v_sc = adc.get_sc_voltage()
            v_sar = adc.get_sar_voltage()
            print(f"ПС: {v_sc:.3f} В | ПП: {v_sar:.3f} В")
    except KeyboardInterrupt:
        adc.deinit()