package servo

import (
	"time"
	"fmt"
	"github.com/Shopify/sarama"
)

func Prod() {
	client, err := sarama.NewClient("client_id", []string{"192.168.90.5:9092"}, &sarama.ClientConfig{MetadataRetries: 1, WaitForElection: 250 * time.Millisecond})
	if err != nil {
		panic(err)
	} else {
		fmt.Println("> connected")
	}
	defer client.Close()

	h := &sarama.ProducerConfig{RequiredAcks: 1, MaxBufferedBytes: 1024, MaxBufferTime: 1000}
	producer, err := sarama.NewProducer(client, h)
	if err != nil {
		panic(err)
	}
	defer producer.Close()

	err = producer.SendMessage("my_topic", nil, sarama.StringEncoder("testing 123"))
	if err != nil {
		panic(err)
	} else {
		fmt.Println("> message sent")
	}
}
