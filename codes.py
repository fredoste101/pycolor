

class Raw16Color():
    """
        https://stackabuse.com/how-to-print-colored-text-in-python/
    """

    def __init__(self):
        COLOR_CODE_ESCAPE = "\033["

        COLOR_CODE_STYLE_NORMAL     = "0"
        COLOR_CODE_STYLE_BOLD       = "1"
        COLOR_CODE_STYLE_LIGHT      = "2"
        COLOR_CODE_STYLE_ITALIC     = "3"
        COLOR_CODE_STYLE_UNDERLINED = "4"
        COLOR_CODE_STYLE_BLINK      = "5"


        COLOR_CODE_FOREGROUND_BLACK     = "30"
        COLOR_CODE_FOREGROUND_RED       = "31"
        COLOR_CODE_FOREGROUND_GREEN     = "32"
        COLOR_CODE_FOREGROUND_YELLOW    = "33"
        COLOR_CODE_FOREGROUND_BLUE      = "34"
        COLOR_CODE_FOREGROUND_PURPLE    = "35"
        COLOR_CODE_FOREGROUND_CYAN      = "36"
        COLOR_CODE_FOREGROUND_WHITE     = "37"


        self.reset = COLOR_CODE_ESCAPE + "0;0m"


        self.black    = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_NORMAL + ";" + COLOR_CODE_FOREGROUND_BLACK   + "m"
        self.red      = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_NORMAL + ";" + COLOR_CODE_FOREGROUND_RED     + "m"

        self.green    = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_NORMAL + ";" + COLOR_CODE_FOREGROUND_GREEN   + "m"
        self.yellow   = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_NORMAL + ";" + COLOR_CODE_FOREGROUND_YELLOW  + "m"
        self.blue     = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_NORMAL + ";" + COLOR_CODE_FOREGROUND_BLUE    + "m"
        self.purple   = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_NORMAL + ";" + COLOR_CODE_FOREGROUND_PURPLE  + "m"
        self.cyan     = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_NORMAL + ";" + COLOR_CODE_FOREGROUND_CYAN    + "m"
        self.white    = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_NORMAL + ";" + COLOR_CODE_FOREGROUND_WHITE   + "m"

        self.boldBlack    = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_BOLD + ";" + COLOR_CODE_FOREGROUND_BLACK   + "m"
        self.boldRed      = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_BOLD + ";" + COLOR_CODE_FOREGROUND_RED     + "m"
        self.boldGreen    = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_BOLD + ";" + COLOR_CODE_FOREGROUND_GREEN   + "m"
        self.boldYellow   = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_BOLD + ";" + COLOR_CODE_FOREGROUND_YELLOW  + "m"
        self.boldBlue     = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_BOLD + ";" + COLOR_CODE_FOREGROUND_BLUE    + "m"
        self.boldPurple   = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_BOLD + ";" + COLOR_CODE_FOREGROUND_PURPLE  + "m"
        self.boldCyan     = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_BOLD + ";" + COLOR_CODE_FOREGROUND_CYAN    + "m"
        self.boldWhite    = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_BOLD + ";" + COLOR_CODE_FOREGROUND_WHITE   + "m"

        self.lightBlack    = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_LIGHT + ";" + COLOR_CODE_FOREGROUND_BLACK   + "m"
        self.lightRed      = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_LIGHT + ";" + COLOR_CODE_FOREGROUND_RED     + "m"
        self.lightGreen    = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_LIGHT + ";" + COLOR_CODE_FOREGROUND_GREEN   + "m"
        self.lightYellow   = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_LIGHT + ";" + COLOR_CODE_FOREGROUND_YELLOW  + "m"
        self.lightBlue     = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_LIGHT + ";" + COLOR_CODE_FOREGROUND_BLUE    + "m"
        self.lightPurple   = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_LIGHT + ";" + COLOR_CODE_FOREGROUND_PURPLE  + "m"
        self.lightCyan     = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_LIGHT + ";" + COLOR_CODE_FOREGROUND_CYAN    + "m"
        self.lightWhite    = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_LIGHT + ";" + COLOR_CODE_FOREGROUND_WHITE   + "m"

        self.italicBlack    = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_ITALIC + ";" + COLOR_CODE_FOREGROUND_BLACK   + "m"
        self.italicRed      = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_ITALIC + ";" + COLOR_CODE_FOREGROUND_RED     + "m"
        self.italicGreen    = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_ITALIC + ";" + COLOR_CODE_FOREGROUND_GREEN   + "m"
        self.italicYellow   = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_ITALIC + ";" + COLOR_CODE_FOREGROUND_YELLOW  + "m"
        self.italicBlue     = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_ITALIC + ";" + COLOR_CODE_FOREGROUND_BLUE    + "m"
        self.italicPurple   = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_ITALIC + ";" + COLOR_CODE_FOREGROUND_PURPLE  + "m"
        self.italicCyan     = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_ITALIC + ";" + COLOR_CODE_FOREGROUND_CYAN    + "m"
        self.italicWhite    = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_ITALIC + ";" + COLOR_CODE_FOREGROUND_WHITE   + "m"

        self.underlineBlack    = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_UNDERLINED + ";" + COLOR_CODE_FOREGROUND_BLACK   + "m"
        self.underlineRed      = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_UNDERLINED + ";" + COLOR_CODE_FOREGROUND_RED     + "m"
        self.underlineGreen    = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_UNDERLINED + ";" + COLOR_CODE_FOREGROUND_GREEN   + "m"
        self.underlineYellow   = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_UNDERLINED + ";" + COLOR_CODE_FOREGROUND_YELLOW  + "m"
        self.underlineBlue     = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_UNDERLINED + ";" + COLOR_CODE_FOREGROUND_BLUE    + "m"
        self.underlinePurple   = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_UNDERLINED + ";" + COLOR_CODE_FOREGROUND_PURPLE  + "m"
        self.underlineCyan     = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_UNDERLINED + ";" + COLOR_CODE_FOREGROUND_CYAN    + "m"
        self.underlineWhite    = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_UNDERLINED + ";" + COLOR_CODE_FOREGROUND_WHITE   + "m"


        self.blinkBlack    = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_BLINK + ";" + COLOR_CODE_FOREGROUND_BLACK   + "m"
        self.blinkRed      = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_BLINK + ";" + COLOR_CODE_FOREGROUND_RED     + "m"
        self.blinkGreen    = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_BLINK + ";" + COLOR_CODE_FOREGROUND_GREEN   + "m"
        self.blinkYellow   = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_BLINK + ";" + COLOR_CODE_FOREGROUND_YELLOW  + "m"
        self.blinkBlue     = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_BLINK + ";" + COLOR_CODE_FOREGROUND_BLUE    + "m"
        self.blinkPurple   = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_BLINK + ";" + COLOR_CODE_FOREGROUND_PURPLE  + "m"
        self.blinkCyan     = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_BLINK + ";" + COLOR_CODE_FOREGROUND_CYAN    + "m"
        self.blinkWhite    = COLOR_CODE_ESCAPE + COLOR_CODE_STYLE_BLINK + ";" + COLOR_CODE_FOREGROUND_WHITE   + "m"


if __name__ == "__main__":
    color = Raw16Color()
    print(color.red + "I am red" + color.reset)
    print(color.blue + "I am blue" + color.reset)
    print(color.boldGreen + "I am bold green" + color.reset)
    print(color.blinkCyan + "I am blinking cyan" + color.reset)
    print(color.lightPurple + "I am light purple" + color.reset)