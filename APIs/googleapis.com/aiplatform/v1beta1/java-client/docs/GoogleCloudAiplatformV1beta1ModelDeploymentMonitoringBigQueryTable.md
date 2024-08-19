

# GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringBigQueryTable

ModelDeploymentMonitoringBigQueryTable specifies the BigQuery table name as well as some information of the logs stored in this table.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bigqueryTablePath** | **String** | The created BigQuery table to store logs. Customer could do their own query &amp; analysis. Format: &#x60;bq://.model_deployment_monitoring_._&#x60; |  [optional] |
|**logSource** | [**LogSourceEnum**](#LogSourceEnum) | The source of log. |  [optional] |
|**logType** | [**LogTypeEnum**](#LogTypeEnum) | The type of log. |  [optional] |
|**requestResponseLoggingSchemaVersion** | **String** | Output only. The schema version of the request/response logging BigQuery table. Default to v1 if unset. |  [optional] [readonly] |



## Enum: LogSourceEnum

| Name | Value |
|---- | -----|
| LOG_SOURCE_UNSPECIFIED | &quot;LOG_SOURCE_UNSPECIFIED&quot; |
| TRAINING | &quot;TRAINING&quot; |
| SERVING | &quot;SERVING&quot; |



## Enum: LogTypeEnum

| Name | Value |
|---- | -----|
| LOG_TYPE_UNSPECIFIED | &quot;LOG_TYPE_UNSPECIFIED&quot; |
| PREDICT | &quot;PREDICT&quot; |
| EXPLAIN | &quot;EXPLAIN&quot; |



