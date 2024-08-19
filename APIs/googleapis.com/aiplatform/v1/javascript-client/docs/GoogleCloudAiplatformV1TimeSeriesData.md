# VertexAiApi.GoogleCloudAiplatformV1TimeSeriesData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tensorboardTimeSeriesId** | **String** | Required. The ID of the TensorboardTimeSeries, which will become the final component of the TensorboardTimeSeries&#39; resource name | [optional] 
**valueType** | **String** | Required. Immutable. The value type of this time series. All the values in this time series data must match this value type. | [optional] 
**values** | [**[GoogleCloudAiplatformV1TimeSeriesDataPoint]**](GoogleCloudAiplatformV1TimeSeriesDataPoint.md) | Required. Data points in this time series. | [optional] 



## Enum: ValueTypeEnum


* `VALUE_TYPE_UNSPECIFIED` (value: `"VALUE_TYPE_UNSPECIFIED"`)

* `SCALAR` (value: `"SCALAR"`)

* `TENSOR` (value: `"TENSOR"`)

* `BLOB_SEQUENCE` (value: `"BLOB_SEQUENCE"`)




