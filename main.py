current_temperature = 0

def on_forever():
    global current_temperature
    current_temperature = input.temperature()
    basic.show_number(current_temperature)
    basic.pause(1000)
    basic.clear_screen()
basic.forever(on_forever)
