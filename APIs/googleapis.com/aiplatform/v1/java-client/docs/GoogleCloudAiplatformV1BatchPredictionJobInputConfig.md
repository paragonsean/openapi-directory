

# GoogleCloudAiplatformV1BatchPredictionJobInputConfig

Configures the input to BatchPredictionJob. See Model.supported_input_storage_formats for Model's supported input formats, and how instances should be expressed via any of them.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bigquerySource** | [**GoogleCloudAiplatformV1BigQuerySource**](GoogleCloudAiplatformV1BigQuerySource.md) |  |  [optional] |
|**gcsSource** | [**GoogleCloudAiplatformV1GcsSource**](GoogleCloudAiplatformV1GcsSource.md) |  |  [optional] |
|**instancesFormat** | **String** | Required. The format in which instances are given, must be one of the Model&#39;s supported_input_storage_formats. |  [optional] |



