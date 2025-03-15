package bg.uni.sofia.peak.motion.hiker.SecureKafkaStreamProcessor;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Service
public class KafkaConsumerService {

    @KafkaListener(topics = "firstTopic", groupId = "my-group")
    public void listenFirstTopic(ConsumerRecord<String, String> record) {
        System.out.println("Received message: " + record.value());
    }

    @KafkaListener(topics = "secondTopic", groupId = "my-group")
    public void secondFirstTopic(ConsumerRecord<String, String> record) {
        System.out.println("Received message: " + record.value());
    }
}
