from sensors.BaseSensor import BaseSensor
from grove.adc import ADC

class LightSensor(BaseSensor):
    def __init__(self):
        BaseSensor.__init__(self)
        self.sensor = None
        self.light_sensor_pin = 2
        self.setup()

    def setup(self):
        try:
            self.sensor = ADC()
            self.init = True
        except Exception as e:
            print("LightSensor.setup: " + str(e))
            self.init = False

    def read(self):
        try:    # connect Grove Light Sensor
            if not self.init:
                self.setup()
            light = self.sensor.read_raw(self.light_sensor_pin)
            #light = self.mapNum(light, 0, 2500, 0.00, 1.00)
            #light = self.rolling_average(light, self.measurements, 20)
        except Exception as e:
            print("LightSensor.read: " + str(e))
            light = self.null_value
            self.init = False
        finally:
            return light