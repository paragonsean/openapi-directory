

# GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigExplanationConfigExplanationBaseline

Output from BatchPredictionJob for Model Monitoring baseline dataset, which can be used to generate baseline attribution scores.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bigquery** | [**GoogleCloudAiplatformV1beta1BigQueryDestination**](GoogleCloudAiplatformV1beta1BigQueryDestination.md) |  |  [optional] |
|**gcs** | [**GoogleCloudAiplatformV1beta1GcsDestination**](GoogleCloudAiplatformV1beta1GcsDestination.md) |  |  [optional] |
|**predictionFormat** | [**PredictionFormatEnum**](#PredictionFormatEnum) | The storage format of the predictions generated BatchPrediction job. |  [optional] |



## Enum: PredictionFormatEnum

| Name | Value |
|---- | -----|
| PREDICTION_FORMAT_UNSPECIFIED | &quot;PREDICTION_FORMAT_UNSPECIFIED&quot; |
| JSONL | &quot;JSONL&quot; |
| BIGQUERY | &quot;BIGQUERY&quot; |



