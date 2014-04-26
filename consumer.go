package servo

import (
	"fmt"
	"time"

	"github.com/Shopify/sarama"
)

func Cons() {
	h := &sarama.ClientConfig{MetadataRetries: 1, WaitForElection: 250 * time.Millisecond}
	client, err := sarama.NewClient("my_client", []string{"192.168.90.5:9092"}, h)
	if err != nil {
		panic(err)
	} else {
		fmt.Println("> connected")
	}
	defer client.Close()

	consumer, err := sarama.NewConsumer(client, "my_topic", 0, "my_consumer_group", &sarama.ConsumerConfig{MaxWaitTime: 200})
	if err != nil {
		panic(err)
	} else {
		fmt.Println("> consumer ready")
	}
	defer consumer.Close()

	msgCount := 0
consumerLoop:
	for {
		select {
		case event := <-consumer.Events():
			if event.Err != nil {
				panic(event.Err)
			}
			msgCount += 1
		case <-time.After(5 * time.Second):
			fmt.Println("> timed out")
			break consumerLoop
		}
	}
	fmt.Println("Got", msgCount, "messages.")
}
