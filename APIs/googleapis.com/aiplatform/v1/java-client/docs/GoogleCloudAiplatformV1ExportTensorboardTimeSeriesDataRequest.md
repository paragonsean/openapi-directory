

# GoogleCloudAiplatformV1ExportTensorboardTimeSeriesDataRequest

Request message for TensorboardService.ExportTensorboardTimeSeriesData.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filter** | **String** | Exports the TensorboardTimeSeries&#39; data that match the filter expression. |  [optional] |
|**orderBy** | **String** | Field to use to sort the TensorboardTimeSeries&#39; data. By default, TensorboardTimeSeries&#39; data is returned in a pseudo random order. |  [optional] |
|**pageSize** | **Integer** | The maximum number of data points to return per page. The default page_size is 1000. Values must be between 1 and 10000. Values above 10000 are coerced to 10000. |  [optional] |
|**pageToken** | **String** | A page token, received from a previous ExportTensorboardTimeSeriesData call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to ExportTensorboardTimeSeriesData must match the call that provided the page token. |  [optional] |



