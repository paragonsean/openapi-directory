# VertexAiApi.GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringBigQueryTable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bigqueryTablePath** | **String** | The created BigQuery table to store logs. Customer could do their own query &amp; analysis. Format: &#x60;bq://.model_deployment_monitoring_._&#x60; | [optional] 
**logSource** | **String** | The source of log. | [optional] 
**logType** | **String** | The type of log. | [optional] 
**requestResponseLoggingSchemaVersion** | **String** | Output only. The schema version of the request/response logging BigQuery table. Default to v1 if unset. | [optional] [readonly] 



## Enum: LogSourceEnum


* `LOG_SOURCE_UNSPECIFIED` (value: `"LOG_SOURCE_UNSPECIFIED"`)

* `TRAINING` (value: `"TRAINING"`)

* `SERVING` (value: `"SERVING"`)





## Enum: LogTypeEnum


* `LOG_TYPE_UNSPECIFIED` (value: `"LOG_TYPE_UNSPECIFIED"`)

* `PREDICT` (value: `"PREDICT"`)

* `EXPLAIN` (value: `"EXPLAIN"`)




