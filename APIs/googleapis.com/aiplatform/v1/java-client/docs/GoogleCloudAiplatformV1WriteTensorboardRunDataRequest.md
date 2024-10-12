

# GoogleCloudAiplatformV1WriteTensorboardRunDataRequest

Request message for TensorboardService.WriteTensorboardRunData.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**tensorboardRun** | **String** | Required. The resource name of the TensorboardRun to write data to. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}&#x60; |  [optional] |
|**timeSeriesData** | [**List&lt;GoogleCloudAiplatformV1TimeSeriesData&gt;**](GoogleCloudAiplatformV1TimeSeriesData.md) | Required. The TensorboardTimeSeries data to write. Values with in a time series are indexed by their step value. Repeated writes to the same step will overwrite the existing value for that step. The upper limit of data points per write request is 5000. |  [optional] |



