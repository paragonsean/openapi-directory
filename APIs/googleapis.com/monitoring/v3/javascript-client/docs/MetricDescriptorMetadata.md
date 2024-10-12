# CloudMonitoringApi.MetricDescriptorMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ingestDelay** | **String** | The delay of data points caused by ingestion. Data points older than this age are guaranteed to be ingested and available to be read, excluding data loss due to errors. | [optional] 
**launchStage** | **String** | Deprecated. Must use the MetricDescriptor.launch_stage instead. | [optional] 
**samplePeriod** | **String** | The sampling period of metric data points. For metrics which are written periodically, consecutive data points are stored at this time interval, excluding data loss due to errors. Metrics with a higher granularity have a smaller sampling period. | [optional] 



## Enum: LaunchStageEnum


* `LAUNCH_STAGE_UNSPECIFIED` (value: `"LAUNCH_STAGE_UNSPECIFIED"`)

* `UNIMPLEMENTED` (value: `"UNIMPLEMENTED"`)

* `PRELAUNCH` (value: `"PRELAUNCH"`)

* `EARLY_ACCESS` (value: `"EARLY_ACCESS"`)

* `ALPHA` (value: `"ALPHA"`)

* `BETA` (value: `"BETA"`)

* `GA` (value: `"GA"`)

* `DEPRECATED` (value: `"DEPRECATED"`)




