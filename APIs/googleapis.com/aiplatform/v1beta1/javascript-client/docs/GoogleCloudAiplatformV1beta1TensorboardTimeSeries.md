# VertexAiApi.GoogleCloudAiplatformV1beta1TensorboardTimeSeries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Timestamp when this TensorboardTimeSeries was created. | [optional] [readonly] 
**description** | **String** | Description of this TensorboardTimeSeries. | [optional] 
**displayName** | **String** | Required. User provided name of this TensorboardTimeSeries. This value should be unique among all TensorboardTimeSeries resources belonging to the same TensorboardRun resource (parent resource). | [optional] 
**etag** | **String** | Used to perform a consistent read-modify-write updates. If not set, a blind \&quot;overwrite\&quot; update happens. | [optional] 
**metadata** | [**GoogleCloudAiplatformV1beta1TensorboardTimeSeriesMetadata**](GoogleCloudAiplatformV1beta1TensorboardTimeSeriesMetadata.md) |  | [optional] 
**name** | **String** | Output only. Name of the TensorboardTimeSeries. | [optional] [readonly] 
**pluginData** | **Blob** | Data of the current plugin, with the size limited to 65KB. | [optional] 
**pluginName** | **String** | Immutable. Name of the plugin this time series pertain to. Such as Scalar, Tensor, Blob | [optional] 
**updateTime** | **String** | Output only. Timestamp when this TensorboardTimeSeries was last updated. | [optional] [readonly] 
**valueType** | **String** | Required. Immutable. Type of TensorboardTimeSeries value. | [optional] 



## Enum: ValueTypeEnum


* `VALUE_TYPE_UNSPECIFIED` (value: `"VALUE_TYPE_UNSPECIFIED"`)

* `SCALAR` (value: `"SCALAR"`)

* `TENSOR` (value: `"TENSOR"`)

* `BLOB_SEQUENCE` (value: `"BLOB_SEQUENCE"`)




