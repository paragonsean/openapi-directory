# VertexAiApi.GoogleCloudAiplatformV1beta1FetchFeatureValuesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataFormat** | **String** | Optional. Response data format. If not set, FeatureViewDataFormat.KEY_VALUE will be used. | [optional] 
**dataKey** | [**GoogleCloudAiplatformV1beta1FeatureViewDataKey**](GoogleCloudAiplatformV1beta1FeatureViewDataKey.md) |  | [optional] 
**format** | **String** | Specify response data format. If not set, KeyValue format will be used. Deprecated. Use FetchFeatureValuesRequest.data_format. | [optional] 
**id** | **String** | Simple ID. The whole string will be used as is to identify Entity to fetch feature values for. | [optional] 



## Enum: DataFormatEnum


* `FEATURE_VIEW_DATA_FORMAT_UNSPECIFIED` (value: `"FEATURE_VIEW_DATA_FORMAT_UNSPECIFIED"`)

* `KEY_VALUE` (value: `"KEY_VALUE"`)

* `PROTO_STRUCT` (value: `"PROTO_STRUCT"`)





## Enum: FormatEnum


* `FORMAT_UNSPECIFIED` (value: `"FORMAT_UNSPECIFIED"`)

* `KEY_VALUE` (value: `"KEY_VALUE"`)

* `PROTO_STRUCT` (value: `"PROTO_STRUCT"`)




