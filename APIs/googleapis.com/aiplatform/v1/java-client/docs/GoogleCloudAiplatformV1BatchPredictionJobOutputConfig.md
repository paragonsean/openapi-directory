

# GoogleCloudAiplatformV1BatchPredictionJobOutputConfig

Configures the output of BatchPredictionJob. See Model.supported_output_storage_formats for supported output formats, and how predictions are expressed via any of them.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bigqueryDestination** | [**GoogleCloudAiplatformV1BigQueryDestination**](GoogleCloudAiplatformV1BigQueryDestination.md) |  |  [optional] |
|**gcsDestination** | [**GoogleCloudAiplatformV1GcsDestination**](GoogleCloudAiplatformV1GcsDestination.md) |  |  [optional] |
|**predictionsFormat** | **String** | Required. The format in which Vertex AI gives the predictions, must be one of the Model&#39;s supported_output_storage_formats. |  [optional] |



