//package bg.uni.sofia.peak.motion.hiker.SecureKafkaStreamProcessor;
//
//import org.apache.kafka.streams.KafkaStreams;
//import org.apache.kafka.streams.StreamsBuilder;
//import org.apache.kafka.streams.StreamsConfig;
//import org.apache.kafka.streams.kstream.KStream;
//import org.springframework.beans.factory.annotation.Value;
//import org.springframework.kafka.annotation.EnableKafkaStreams;
//import org.springframework.stereotype.Component;
//
//import java.util.Properties;
//
//@Component
//@EnableKafkaStreams
//public class SecureKafkaStreamProcessor {
//
//    @Value("${spring.kafka.streams.bootstrap-servers}")
//    private String bootstrapServers;
//
//    @Value("${spring.kafka.streams.application-id}")
//    private String applicationId;
//
//    public SecureKafkaStreamProcessor() {
//        StreamsBuilder builder = new StreamsBuilder();
//
//        // Example: Read from an input topic and log messages
//        KStream<String, String> stream = builder.stream("secure-input-topic");
//        stream.foreach((key, value) -> System.out.println("Received: " + key + " -> " + value));
//
//        // Kafka Streams properties with SSL
//        Properties props = new Properties();
//        props.put(StreamsConfig.APPLICATION_ID_CONFIG, applicationId);
//        props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
//        props.put("security.protocol", "SSL");
//        props.put("ssl.truststore.location", "/path/to/truststore.jks");
//        props.put("ssl.truststore.password", "myTruststorePassword");
//        props.put("ssl.keystore.location", "/path/to/keystore.jks");
//        props.put("ssl.keystore.password", "myKeystorePassword");
//        props.put("ssl.key.password", "myKeyPassword");
//
//        KafkaStreams streams = new KafkaStreams(builder.build(), props);
//        streams.start();
//
//        // Shutdown hook
//        Runtime.getRuntime().addShutdownHook(new Thread(streams::close));
//    }
//}
