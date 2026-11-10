import mcp3021_driver as mcp
import adc_plot as plotter
import time

adc = mcp.MCP3021(5.0, verbose=False)

voltage_values = []
time_values = []

duration = 10.0 

print(f"Идет запись {duration} секунд. Приготовьтесь нажимать кнопку!")
print("Нажмите и удерживайте кнопку 2-3 секунды, затем отпустите.")

try:
    start_time = time.time()
    current_time = 0.0
    
    while current_time < duration:
        voltage_values.append(adc.get_voltage())
        current_time = time.time() - start_time
        time_values.append(current_time)
        
    print("Запись завершена. Строим график...")
    plotter.plot_voltage_vs_time(time_values, voltage_values, adc.dynamic_range)

except KeyboardInterrupt:
    print("\nЗапись прервана.")

finally:
    adc.deinit()