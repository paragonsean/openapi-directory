

# ParallelismConfiguration

Describes parameters for how a Flink-based Kinesis Data Analytics application executes multiple tasks simultaneously. For more information about parallelism, see <a href=\"https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/parallel.html\">Parallel Execution</a> in the <a href=\"https://ci.apache.org/projects/flink/flink-docs-release-1.8/\">Apache Flink Documentation</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**configurationType** | [**ConfigurationType**](ConfigurationType.md) |  |  |
|**parallelism** | [**Integer**](Integer.md) |  |  [optional] |
|**parallelismPerKPU** | [**Integer**](Integer.md) |  |  [optional] |
|**autoScalingEnabled** | [**Boolean**](Boolean.md) |  |  [optional] |



