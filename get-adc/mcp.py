import mcp3021_driver as mcp
import adc_plot as plotter
import time

adc = mcp.MCP3021(5.0, verbose=False)
voltage_values, time_values = [], []
duration = 3.0

print(f"Запись (I2C) {duration} сек. Крутите потенциометр!")
try:
    start_time = time.time()
    current_time = 0.0
    while current_time < duration:
        voltage_values.append(adc.get_voltage())
        current_time = time.time() - start_time
        time_values.append(current_time)
    
    plotter.plot_voltage_vs_time(time_values, voltage_values, adc.dynamic_range)
    plotter.plot_sampling_period_hist(time_values)
except KeyboardInterrupt:
    pass
finally:
    adc.deinit()