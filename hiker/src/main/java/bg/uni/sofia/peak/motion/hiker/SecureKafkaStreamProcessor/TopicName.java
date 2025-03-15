package bg.uni.sofia.peak.motion.hiker.SecureKafkaStreamProcessor;

public enum TopicName {
    EXECUTIONS_REQUEST("executions-request-topic-v1"),
    EXECUTIONS_RESULT("executions-result-topic-v1"),
    COMMANDS("commands-topic-v1");

    private final String value;

    TopicName(String value) {
        if (value == null || value.isBlank()) {
            throw new IllegalArgumentException("Value of TopicName cannot be null or blank");
        }

        this.value = value;
    }

    public String getValue() {
        return value;
    }
}