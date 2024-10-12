

# MetricDescriptorMetadata

Additional annotations that can be used to guide the usage of a metric.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ingestDelay** | **String** | The delay of data points caused by ingestion. Data points older than this age are guaranteed to be ingested and available to be read, excluding data loss due to errors. |  [optional] |
|**launchStage** | [**LaunchStageEnum**](#LaunchStageEnum) | Deprecated. Must use the MetricDescriptor.launch_stage instead. |  [optional] |
|**samplePeriod** | **String** | The sampling period of metric data points. For metrics which are written periodically, consecutive data points are stored at this time interval, excluding data loss due to errors. Metrics with a higher granularity have a smaller sampling period. |  [optional] |



## Enum: LaunchStageEnum

| Name | Value |
|---- | -----|
| LAUNCH_STAGE_UNSPECIFIED | &quot;LAUNCH_STAGE_UNSPECIFIED&quot; |
| UNIMPLEMENTED | &quot;UNIMPLEMENTED&quot; |
| PRELAUNCH | &quot;PRELAUNCH&quot; |
| EARLY_ACCESS | &quot;EARLY_ACCESS&quot; |
| ALPHA | &quot;ALPHA&quot; |
| BETA | &quot;BETA&quot; |
| GA | &quot;GA&quot; |
| DEPRECATED | &quot;DEPRECATED&quot; |



