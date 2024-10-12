# VertexAiApi.GoogleCloudAiplatformV1beta1ModelMonitoringConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alertConfig** | [**GoogleCloudAiplatformV1beta1ModelMonitoringAlertConfig**](GoogleCloudAiplatformV1beta1ModelMonitoringAlertConfig.md) |  | [optional] 
**analysisInstanceSchemaUri** | **String** | YAML schema file uri in Cloud Storage describing the format of a single instance that you want Tensorflow Data Validation (TFDV) to analyze. If there are any data type differences between predict instance and TFDV instance, this field can be used to override the schema. For models trained with Vertex AI, this field must be set as all the fields in predict instance formatted as string. | [optional] 
**objectiveConfigs** | [**[GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfig]**](GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfig.md) | Model monitoring objective config. | [optional] 
**statsAnomaliesBaseDirectory** | [**GoogleCloudAiplatformV1beta1GcsDestination**](GoogleCloudAiplatformV1beta1GcsDestination.md) |  | [optional] 


