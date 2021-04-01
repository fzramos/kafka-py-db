# Goal
- Make a program that receives a Kafka message and, based on it, does some action on to the connected database

# Steps to run program on a Windows Machine
- Note that all new terminals after step 2 should be in set in "kafka_2.13-2.7.0" directory
1. Download and install WSL2 and Ubuntu 20.04 LTS as it is the most performant way to run Kafka on a Windows machine without using a virtual machine.
    - Note that this takes several restarts and you need to run the wsl update file from a powershell with admin privilege
2. Install Kafka on to Ubuntu terminal
3. Run Zookeeper in the terminal (defaults to port 2128)
    ```
    bin/zookeeper-server-start.sh config/zookeeper.properties
    ```
4. Run Kafka Broker in a different terminal (runs Kafka and its storage and defaults to port 9092)
    ```
    bin/kafka-server-start.sh config/server.properties
    ```
5. On a different terminal create the topic 'numtest'
    ```
    bin/kafka-topics.sh --create --topic numtest --bootstrap-server localhost:9092
    ```
6. Run producer program which adds messages to the numtest topic
7. Run consumer program which reads the messages in the numtest topic and adds it to a database
8. Shut down zookeeper by typing Ctrl+C on it's respective terminal
9. Then run this command 
    ```
    rm -rf /tmp/kafka-logs /tmp/zookeeper
    ```

# Alternative to running the python scripts
- If you would like to test producer and consumer roles directly, you can run these in 2 seperate terminals
1. Follow steps 1-5 of above instructions
2. In a new terminal start the producer with the command:
    ```
    bin/kafka-console-consumer.sh --topic numtest --from-beginning --bootstrap-server localhost:9092
    ```
3. In another teminal start the consumer with the command:
    ```
    bin/kafka-console-producer.sh --topic numtest --bootstrap-server localhost:9092
    ```
4. Type into producer terminal and consumer terminal should update after each enter
5. To shut down these commands, type Ctrl+C in both terminals and follow steps 8 and 9 in the above instructions