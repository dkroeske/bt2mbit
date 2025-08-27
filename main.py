# init

counter = 0

def on_button_pressed_a():
    global counter
    counter = counter + 1
    basic.show_number(counter % 10)
    bluetooth.uart_write_value("Counter", counter)

def init():
    input.on_button_pressed(Button.A, on_button_pressed_a)
    bluetooth.set_transmit_power(5)
    bluetooth.start_uart_service()
    basic.show_icon(IconNames.HEART)

def main():
    init()
    while True:
        led.toggle(4, 4)
        pause(1000)

# Start
main()