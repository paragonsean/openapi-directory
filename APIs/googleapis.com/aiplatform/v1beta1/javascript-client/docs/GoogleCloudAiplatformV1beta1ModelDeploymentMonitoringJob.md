# VertexAiApi.GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysisInstanceSchemaUri** | **String** | YAML schema file uri describing the format of a single instance that you want Tensorflow Data Validation (TFDV) to analyze. If this field is empty, all the feature data types are inferred from predict_instance_schema_uri, meaning that TFDV will use the data in the exact format(data type) as prediction request/response. If there are any data type differences between predict instance and TFDV instance, this field can be used to override the schema. For models trained with Vertex AI, this field must be set as all the fields in predict instance formatted as string. | [optional] 
**bigqueryTables** | [**[GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringBigQueryTable]**](GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringBigQueryTable.md) | Output only. The created bigquery tables for the job under customer project. Customer could do their own query &amp; analysis. There could be 4 log tables in maximum: 1. Training data logging predict request/response 2. Serving data logging predict request/response | [optional] [readonly] 
**createTime** | **String** | Output only. Timestamp when this ModelDeploymentMonitoringJob was created. | [optional] [readonly] 
**displayName** | **String** | Required. The user-defined name of the ModelDeploymentMonitoringJob. The name can be up to 128 characters long and can consist of any UTF-8 characters. Display name of a ModelDeploymentMonitoringJob. | [optional] 
**enableMonitoringPipelineLogs** | **Boolean** | If true, the scheduled monitoring pipeline logs are sent to Google Cloud Logging, including pipeline status and anomalies detected. Please note the logs incur cost, which are subject to [Cloud Logging pricing](https://cloud.google.com/logging#pricing). | [optional] 
**encryptionSpec** | [**GoogleCloudAiplatformV1beta1EncryptionSpec**](GoogleCloudAiplatformV1beta1EncryptionSpec.md) |  | [optional] 
**endpoint** | **String** | Required. Endpoint resource name. Format: &#x60;projects/{project}/locations/{location}/endpoints/{endpoint}&#x60; | [optional] 
**error** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  | [optional] 
**labels** | **{String: String}** | The labels with user-defined metadata to organize your ModelDeploymentMonitoringJob. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. | [optional] 
**latestMonitoringPipelineMetadata** | [**GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringJobLatestMonitoringPipelineMetadata**](GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringJobLatestMonitoringPipelineMetadata.md) |  | [optional] 
**logTtl** | **String** | The TTL of BigQuery tables in user projects which stores logs. A day is the basic unit of the TTL and we take the ceil of TTL/86400(a day). e.g. { second: 3600} indicates ttl &#x3D; 1 day. | [optional] 
**loggingSamplingStrategy** | [**GoogleCloudAiplatformV1beta1SamplingStrategy**](GoogleCloudAiplatformV1beta1SamplingStrategy.md) |  | [optional] 
**modelDeploymentMonitoringObjectiveConfigs** | [**[GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringObjectiveConfig]**](GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringObjectiveConfig.md) | Required. The config for monitoring objectives. This is a per DeployedModel config. Each DeployedModel needs to be configured separately. | [optional] 
**modelDeploymentMonitoringScheduleConfig** | [**GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringScheduleConfig**](GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringScheduleConfig.md) |  | [optional] 
**modelMonitoringAlertConfig** | [**GoogleCloudAiplatformV1beta1ModelMonitoringAlertConfig**](GoogleCloudAiplatformV1beta1ModelMonitoringAlertConfig.md) |  | [optional] 
**name** | **String** | Output only. Resource name of a ModelDeploymentMonitoringJob. | [optional] [readonly] 
**nextScheduleTime** | **String** | Output only. Timestamp when this monitoring pipeline will be scheduled to run for the next round. | [optional] [readonly] 
**predictInstanceSchemaUri** | **String** | YAML schema file uri describing the format of a single instance, which are given to format this Endpoint&#39;s prediction (and explanation). If not set, we will generate predict schema from collected predict requests. | [optional] 
**samplePredictInstance** | **Object** | Sample Predict instance, same format as PredictRequest.instances, this can be set as a replacement of ModelDeploymentMonitoringJob.predict_instance_schema_uri. If not set, we will generate predict schema from collected predict requests. | [optional] 
**scheduleState** | **String** | Output only. Schedule state when the monitoring job is in Running state. | [optional] [readonly] 
**state** | **String** | Output only. The detailed state of the monitoring job. When the job is still creating, the state will be &#39;PENDING&#39;. Once the job is successfully created, the state will be &#39;RUNNING&#39;. Pause the job, the state will be &#39;PAUSED&#39;. Resume the job, the state will return to &#39;RUNNING&#39;. | [optional] [readonly] 
**statsAnomaliesBaseDirectory** | [**GoogleCloudAiplatformV1beta1GcsDestination**](GoogleCloudAiplatformV1beta1GcsDestination.md) |  | [optional] 
**updateTime** | **String** | Output only. Timestamp when this ModelDeploymentMonitoringJob was updated most recently. | [optional] [readonly] 



## Enum: ScheduleStateEnum


* `MONITORING_SCHEDULE_STATE_UNSPECIFIED` (value: `"MONITORING_SCHEDULE_STATE_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `OFFLINE` (value: `"OFFLINE"`)

* `RUNNING` (value: `"RUNNING"`)





## Enum: StateEnum


* `UNSPECIFIED` (value: `"JOB_STATE_UNSPECIFIED"`)

* `QUEUED` (value: `"JOB_STATE_QUEUED"`)

* `PENDING` (value: `"JOB_STATE_PENDING"`)

* `RUNNING` (value: `"JOB_STATE_RUNNING"`)

* `SUCCEEDED` (value: `"JOB_STATE_SUCCEEDED"`)

* `FAILED` (value: `"JOB_STATE_FAILED"`)

* `CANCELLING` (value: `"JOB_STATE_CANCELLING"`)

* `CANCELLED` (value: `"JOB_STATE_CANCELLED"`)

* `PAUSED` (value: `"JOB_STATE_PAUSED"`)

* `EXPIRED` (value: `"JOB_STATE_EXPIRED"`)

* `UPDATING` (value: `"JOB_STATE_UPDATING"`)

* `PARTIALLY_SUCCEEDED` (value: `"JOB_STATE_PARTIALLY_SUCCEEDED"`)




