package bg.uni.sofia.peak.motion.hiker.SecureKafkaStreamProcessor;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/kafka")
public class KafkaController {

    private final KafkaProducerService kafkaProducerService;
    private final KafkaConsumerService kafkaConsumerService;

    public KafkaController(KafkaProducerService kafkaProducerService, KafkaConsumerService kafkaConsumerService) {
        this.kafkaProducerService = kafkaProducerService;
        this.kafkaConsumerService = kafkaConsumerService;
    }

    @GetMapping("/send")
    public ResponseEntity<String> sendMessage(@RequestParam(required = false, defaultValue = "default-topic") String topic,
                                              @RequestParam(required = false, defaultValue = "default-message") String message) {
        System.out.println("Producer Failed");
        kafkaProducerService.sendMessage(topic, message);
        System.out.println("Producer Success");
        return ResponseEntity.ok("Message sent to Kafka: " + message);
    }

//    @GetMapping("/messages")
//    public ResponseEntity<List<String>> getConsumedMessages() {
//        return ResponseEntity.ok(kafkaConsumerService.getReceivedMessages());
//    }
}
