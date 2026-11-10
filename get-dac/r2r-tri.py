import r2r_dac as r2r
import signal_generator as sg

try:
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, False)
    t = 0.0
    while True:
        voltage = sg.get_triangle_wave_amplitude(10, t) * 2.0
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(1000)
        t += 1.0 / 1000
except KeyboardInterrupt:
    print("\nОстановлено.")
finally:
    if 'dac' in locals(): dac.deinit()