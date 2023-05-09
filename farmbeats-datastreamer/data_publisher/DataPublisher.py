import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import threading

lock = threading.Lock()

class DataPublisher:
    def __init__(self):
        print("constructor")
        self.serial_data_array = [0]
        self.client = mqtt.Client("farmbeats")
       # self.client.username_pw_set(username="joeax",password="Picard2023!")
       # self.client.connect("76.17.142.126", port=21883)
        self.client.connect("10.0.0.165")

    def send_data(self, data):
        print("invoke send_data")
        data = self.__process_data(data)
        try:
            lock.acquire()
            #with self.serial as serial:
            print("publishing")
            self.client.publish("farmbeats_sarah",data.encode('utf-8'))
            lock.release()
        except Exception as e:
            return None

    def __process_data(self, data):
        if not isinstance(data, str):
            data = str(data)
        if not data.endswith("\n"):
            data += "\n"
        return data

    def send_data_array(self, data_array):
        data_string = self.__process_data_array(data_array)
        self.send_data(data_string)

    def __process_data_array(self, data_array):
        data_string = ""
        for data in data_array:
            data_string += str(data)
            data_string += ","
        return data_string

    def read_data(self):
        try:
            lock.acquire()
            with self.serial as serial:
                data = serial.readline().decode()
            lock.release()
        except Exception as e:
            return None
        if data == "":
            return None
        if data != "":
            self.serial_data_array = data.split(",")
        else:
            self.serial_data_array[0] = data
        return self.serial_data_array
