basic.show_icon(IconNames.HEART)
radio.set_group(17)

def on_forever():
    radio.send_value("x", Math.idiv(input.acceleration(Dimension.X), 10))
    basic.pause(100)
    radio.send_value("y", Math.idiv(input.acceleration(Dimension.Y), 10))
    basic.pause(100)
basic.forever(on_forever)
