

# GoogleCloudAiplatformV1FetchFeatureValuesRequest

Request message for FeatureOnlineStoreService.FetchFeatureValues. All the features under the requested feature view will be returned.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataFormat** | [**DataFormatEnum**](#DataFormatEnum) | Optional. Response data format. If not set, FeatureViewDataFormat.KEY_VALUE will be used. |  [optional] |
|**dataKey** | [**GoogleCloudAiplatformV1FeatureViewDataKey**](GoogleCloudAiplatformV1FeatureViewDataKey.md) |  |  [optional] |



## Enum: DataFormatEnum

| Name | Value |
|---- | -----|
| FEATURE_VIEW_DATA_FORMAT_UNSPECIFIED | &quot;FEATURE_VIEW_DATA_FORMAT_UNSPECIFIED&quot; |
| KEY_VALUE | &quot;KEY_VALUE&quot; |
| PROTO_STRUCT | &quot;PROTO_STRUCT&quot; |



