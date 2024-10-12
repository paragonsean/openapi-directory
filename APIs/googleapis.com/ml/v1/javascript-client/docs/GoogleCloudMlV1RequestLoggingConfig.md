# AiPlatformTrainingPredictionApi.GoogleCloudMlV1RequestLoggingConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bigqueryTableName** | **String** | Required. Fully qualified BigQuery table name in the following format: \&quot; project_id.dataset_name.table_name\&quot; The specified table must already exist, and the \&quot;Cloud ML Service Agent\&quot; for your project must have permission to write to it. The table must have the following [schema](/bigquery/docs/schemas): Field nameType Mode model STRING REQUIRED model_version STRING REQUIRED time TIMESTAMP REQUIRED raw_data STRING REQUIRED raw_prediction STRING NULLABLE groundtruth STRING NULLABLE  | [optional] 
**samplingPercentage** | **Number** | Percentage of requests to be logged, expressed as a fraction from 0 to 1. For example, if you want to log 10% of requests, enter &#x60;0.1&#x60;. The sampling window is the lifetime of the model version. Defaults to 0. | [optional] 


