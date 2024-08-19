

# GoogleCloudAiplatformV1beta1BatchPredictionJobInputConfig

Configures the input to BatchPredictionJob. See Model.supported_input_storage_formats for Model's supported input formats, and how instances should be expressed via any of them.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bigquerySource** | [**GoogleCloudAiplatformV1beta1BigQuerySource**](GoogleCloudAiplatformV1beta1BigQuerySource.md) |  |  [optional] |
|**gcsSource** | [**GoogleCloudAiplatformV1beta1GcsSource**](GoogleCloudAiplatformV1beta1GcsSource.md) |  |  [optional] |
|**instancesFormat** | **String** | Required. The format in which instances are given, must be one of the Model&#39;s supported_input_storage_formats. |  [optional] |



