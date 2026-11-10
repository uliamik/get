import r2r_adc as adc
import adc_plot as plotter
import time

dac = adc.R2R_ADC(3.183, compare_time=0.0001, verbose=False)
voltage_values, time_values = [], []
duration = 3.0

print(f"Запись (ПС) {duration} сек. Крутите потенциометр!")
try:
    start_time = time.time()
    current_time = 0.0
    while current_time < duration:
        voltage_values.append(dac.get_sc_voltage())
        current_time = time.time() - start_time
        time_values.append(current_time)
    
    plotter.plot_voltage_vs_time(time_values, voltage_values, dac.dynamic_range)
    plotter.plot_sampling_period_hist(time_values)
except KeyboardInterrupt:
    pass
finally:
    dac.deinit()