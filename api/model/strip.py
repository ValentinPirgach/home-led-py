from rpi_ws281x import *
import time

# LED strip configuration:
LED_1_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_1_DMA        = 10      # DMA channel to use for generating signal (Between 1 and 14)
LED_1_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_1_STRIP      = ws.WS2811_STRIP_GRB

class StripModel:
    def __init__(self):
        stripesData = {
            "table": {
                "count": 88,
                "pin": 13,
                "brightness": 255,
                "channel": 1
            },
            "stand": {
                "count": 128,
                "pin": 18,
                "brightness": 255,
                "channel": 0
            }
        }
        
        self.stripes = {}
        self.currentColor = [0, 0, 0]
        self.lastColor = [0, 0, 0]

        for key in stripesData:
            config = stripesData[key]

            self.stripes[key] = Adafruit_NeoPixel(
                config['count'],
                config['pin'],
                LED_1_FREQ_HZ,
                LED_1_DMA,
                LED_1_INVERT,
                config['brightness'],
                config['channel'],
                LED_1_STRIP
            )

            self.stripes[key].begin()


    def setColor(self, stripName, color):
        strip = self.stripes[stripName]
        self.currentColor = color

        for i in range(255, 0, -5):
            strip.setBrightness(i)
            strip.show()
            time.sleep(1/500.0)

        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(color[0], color[1], color[2]))

        for i in range(0, 255, 5):
            strip.setBrightness(i)
            strip.show()
            time.sleep(1/500.0)


    def turnOn(self, stripName):
        self.setColor(stripName, self.lastColor)


    def turnOff(self, stripName):
        self.lastColor = self.currentColor
        self.setColor(stripName, [0, 0, 0])


    def setBrightness(self, stripName, brightness):
        strip = self.stripes[stripName]
        
        strip.setBrightness(brightness)
        strip.show()
