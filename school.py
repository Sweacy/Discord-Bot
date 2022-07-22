basic.show_string("Setting setups...")
light_level = input.light_level() - 25

def on_forever():
    if input.light_level() >= light_level and input.pin_is_pressed(TouchPin.P1) == False:
        music.play_melody("A - A - A - A - ", 400)
        basic.show_leds("""
            # . . . #
                        # . . . #
                        # . . . #
                        # . . . #
                        . . . . #
        """)
        basic.show_leds("""
            # . . . #
                        # . . # #
                        # . . # #
                        # . . # #
                        . . . # .
        """)
        basic.show_leds("""
            # . . . #
                        # . # # #
                        # . # # #
                        # . # # #
                        . . # . .
        """)
        basic.show_leds("""
            # . . # #
                        # # # # #
                        # # # # #
                        # # # # #
                        . # # . .
        """)
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        . . . . .
        """)
        music.play_melody("A - A - A - A - ", 400)
    else:
        basic.clear_screen()
        music.stop_all_sounds()
        basic.pause(1000)
basic.forever(on_forever)
