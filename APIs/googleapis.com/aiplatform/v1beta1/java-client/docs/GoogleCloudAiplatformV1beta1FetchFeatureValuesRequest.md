

# GoogleCloudAiplatformV1beta1FetchFeatureValuesRequest

Request message for FeatureOnlineStoreService.FetchFeatureValues. All the features under the requested feature view will be returned.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataFormat** | [**DataFormatEnum**](#DataFormatEnum) | Optional. Response data format. If not set, FeatureViewDataFormat.KEY_VALUE will be used. |  [optional] |
|**dataKey** | [**GoogleCloudAiplatformV1beta1FeatureViewDataKey**](GoogleCloudAiplatformV1beta1FeatureViewDataKey.md) |  |  [optional] |
|**format** | [**FormatEnum**](#FormatEnum) | Specify response data format. If not set, KeyValue format will be used. Deprecated. Use FetchFeatureValuesRequest.data_format. |  [optional] |
|**id** | **String** | Simple ID. The whole string will be used as is to identify Entity to fetch feature values for. |  [optional] |



## Enum: DataFormatEnum

| Name | Value |
|---- | -----|
| FEATURE_VIEW_DATA_FORMAT_UNSPECIFIED | &quot;FEATURE_VIEW_DATA_FORMAT_UNSPECIFIED&quot; |
| KEY_VALUE | &quot;KEY_VALUE&quot; |
| PROTO_STRUCT | &quot;PROTO_STRUCT&quot; |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| FORMAT_UNSPECIFIED | &quot;FORMAT_UNSPECIFIED&quot; |
| KEY_VALUE | &quot;KEY_VALUE&quot; |
| PROTO_STRUCT | &quot;PROTO_STRUCT&quot; |



