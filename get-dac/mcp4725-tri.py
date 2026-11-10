import mcp4725_driver as mcp
import signal_generator as sg

try:
    dac = mcp.MCP4725(5.11, 0x61, False)
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