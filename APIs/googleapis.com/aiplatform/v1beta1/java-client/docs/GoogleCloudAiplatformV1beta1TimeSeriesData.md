

# GoogleCloudAiplatformV1beta1TimeSeriesData

All the data stored in a TensorboardTimeSeries.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**tensorboardTimeSeriesId** | **String** | Required. The ID of the TensorboardTimeSeries, which will become the final component of the TensorboardTimeSeries&#39; resource name |  [optional] |
|**valueType** | [**ValueTypeEnum**](#ValueTypeEnum) | Required. Immutable. The value type of this time series. All the values in this time series data must match this value type. |  [optional] |
|**values** | [**List&lt;GoogleCloudAiplatformV1beta1TimeSeriesDataPoint&gt;**](GoogleCloudAiplatformV1beta1TimeSeriesDataPoint.md) | Required. Data points in this time series. |  [optional] |



## Enum: ValueTypeEnum

| Name | Value |
|---- | -----|
| VALUE_TYPE_UNSPECIFIED | &quot;VALUE_TYPE_UNSPECIFIED&quot; |
| SCALAR | &quot;SCALAR&quot; |
| TENSOR | &quot;TENSOR&quot; |
| BLOB_SEQUENCE | &quot;BLOB_SEQUENCE&quot; |



