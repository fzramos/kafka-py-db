# Goal
- Make a program that receives a Kafka message and, based on it, does some action on to the connected database

# Steps to run program on a Windows Machine
1. Download and install WSL2 and Ubuntu 20.04 LTS as it is the most performant way to run Kafka on a Windows machine without using a virtual machine.
2. Install Kafka on to Ubuntu terminal
3. Run Zookeeper in the terminal
4. Run Kafka Broker in a different terminal(runs Kafka and its storage)
5. On a different terminal create the topic 'numtest'
6. Run producer program which adds messages to the numtest topic
7. Run consumer program which reads the messages in the numtest topic and adds it to a database