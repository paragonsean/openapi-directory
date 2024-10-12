

# CheckpointConfiguration

Describes an application's checkpointing configuration. Checkpointing is the process of persisting application state for fault tolerance. For more information, see <a href=\"https://ci.apache.org/projects/flink/flink-docs-release-1.8/concepts/programming-model.html#checkpoints-for-fault-tolerance\"> Checkpoints for Fault Tolerance</a> in the <a href=\"https://ci.apache.org/projects/flink/flink-docs-release-1.8/\">Apache Flink Documentation</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**configurationType** | [**ConfigurationType**](ConfigurationType.md) |  |  |
|**checkpointingEnabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**checkpointInterval** | [**Integer**](Integer.md) |  |  [optional] |
|**minPauseBetweenCheckpoints** | [**Integer**](Integer.md) |  |  [optional] |



