#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-06-26 15:14:22

import paho.mqtt.client as mqtt
import json
import base64


def on_connect(client, userdata, flags, rc):
    print("connect" + str(rc))
    client.subscribe("lora/rxpk")


def on_message(client, userdata, msg):
    print(msg.topic + "  msg " + msg.payload)
    jdata = json.loads(msg.payload)
    # print jdata
    get_data = jdata["data"]

    print(get_data)
    print(base64.b64decode(get_data))


def main():

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("10.21.20.8", 1883, 60)

    client.loop_forever()


if __name__ == "__main__":
    main()
