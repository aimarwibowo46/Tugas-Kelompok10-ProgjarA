# Task ventilator
# Binds PUSH socket to tcp://localhost:5557
# Sends batch of tasks to workers via that socket
#
# Author: Lev Givon <lev(at)columbia(dot)edu>

import zmq
import random
import time


context = zmq.Context()

# Socket to send messages on
sender = context.socket(zmq.PUSH)
sender.bind("tcp://*:5557")

# Socket with direct access to the sink: used to synchronize start of batch
sink = context.socket(zmq.PUSH)
sink.connect("tcp://localhost:5558")

sink1 = context.socket(zmq.PUSH)
sink1.connect("tcp://localhost:5559")

sink2 = context.socket(zmq.PUSH)
sink2.connect("tcp://localhost:5560")

while True:
    print("Press Enter when the workers are ready: ")
    input()
    print("Sending tasks to workers...")

    # The first message is "0" and signals start of batch
    sink.send(b'0')

    # Initialize random number generator
    # random.seed()

    # Send 10 tasks
    # total_msec = 0
    for task_nbr in range(5):

        # Random workload from 1 to 100 msecs
        workload = random.randint(0, 2)
        # if(workload == 0):

        sender.send_string(f"{workload}")

    # print(f"Total expected cost: {total_msec} msec")
    print(f"Generator finished, i'll Summon the Executioner")

    # Give 0MQ time to deliver
    time.sleep(5)
    # input = input("Exit? Y/N")
    # if(str(input) == "Y" or str(input)  == "y"):
    #     break
    