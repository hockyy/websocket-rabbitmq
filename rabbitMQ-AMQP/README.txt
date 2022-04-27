```bash
docker run -d -e RABBITMQ_NODENAME=my-rabbit --name rabbitmq -p 15672:15672 -p 15674:15674 -p 61613:61613 -p 5672:5672 resilva87/docker-rabbitmq-stomp
```

SSH into CLI, then run
```bash
rabbitmq-plugins enable rabbitmq_web_stomp
```