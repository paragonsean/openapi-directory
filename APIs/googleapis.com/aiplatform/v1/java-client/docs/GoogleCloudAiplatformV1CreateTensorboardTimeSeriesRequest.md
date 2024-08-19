

# GoogleCloudAiplatformV1CreateTensorboardTimeSeriesRequest

Request message for TensorboardService.CreateTensorboardTimeSeries.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**parent** | **String** | Required. The resource name of the TensorboardRun to create the TensorboardTimeSeries in. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}&#x60; |  [optional] |
|**tensorboardTimeSeries** | [**GoogleCloudAiplatformV1TensorboardTimeSeries**](GoogleCloudAiplatformV1TensorboardTimeSeries.md) |  |  [optional] |
|**tensorboardTimeSeriesId** | **String** | Optional. The user specified unique ID to use for the TensorboardTimeSeries, which becomes the final component of the TensorboardTimeSeries&#39;s resource name. This value should match \&quot;a-z0-9{0, 127}\&quot; |  [optional] |



