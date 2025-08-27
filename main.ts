//  init
let counter = 0
function init() {
    input.onButtonPressed(Button.A, function on_button_pressed_a() {
        
        counter = counter + 1
        basic.showNumber(counter)
        bluetooth.uartWriteValue("Counter", counter)
    })
    bluetooth.setTransmitPower(5)
    bluetooth.startUartService()
}

function main() {
    init()
    while (true) {
        led.toggle(4, 4)
        pause(1000)
    }
}

//  Start
main()
