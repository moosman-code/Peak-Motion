package bg.uni.sofia.peak.motion.hiker.SecureKafkaStreamProcessor;

import org.apache.kafka.clients.admin.Admin;
import org.apache.kafka.clients.admin.AdminClientConfig;
import org.apache.kafka.clients.admin.CreateTopicsResult;
import org.apache.kafka.clients.admin.NewTopic;
import org.apache.kafka.common.config.TopicConfig;

import java.util.Collections;
import java.util.Properties;

public class KafkaTopicConfig {

    private static final int PARTITION_NUMBER = 1;
    private static final short TOPIC_FACTOR = 1;

    public void init() {
        Properties props = new Properties();
        props.put(AdminClientConfig.BOOTSTRAP_SERVERS_CONFIG, "${spring.kafka.bootstrap-servers}");

        Admin admin = Admin.create(props);

        for (TopicName topicName : TopicName.values()) {
            CreateTopicsResult result = createCommandTopic(admin, topicName.getValue());
        }

        admin.close();
    }

    private CreateTopicsResult createCommandTopic(Admin admin, String topicName) {
        return admin.createTopics(Collections.singleton(
                new NewTopic(topicName, PARTITION_NUMBER, TOPIC_FACTOR)
                        .configs(Collections.singletonMap(TopicConfig.CLEANUP_POLICY_CONFIG, TopicConfig.CLEANUP_POLICY_COMPACT))
        ));
    }
}