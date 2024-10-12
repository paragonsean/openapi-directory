

# GoogleAnalyticsAdminV1betaDataStream

A resource message representing a data stream.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**androidAppStreamData** | [**GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamData**](GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamData.md) |  |  [optional] |
|**createTime** | **String** | Output only. Time when this stream was originally created. |  [optional] [readonly] |
|**displayName** | **String** | Human-readable display name for the Data Stream. Required for web data streams. The max allowed display name length is 255 UTF-16 code units. |  [optional] |
|**iosAppStreamData** | [**GoogleAnalyticsAdminV1betaDataStreamIosAppStreamData**](GoogleAnalyticsAdminV1betaDataStreamIosAppStreamData.md) |  |  [optional] |
|**name** | **String** | Output only. Resource name of this Data Stream. Format: properties/{property_id}/dataStreams/{stream_id} Example: \&quot;properties/1000/dataStreams/2000\&quot; |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. Immutable. The type of this DataStream resource. |  [optional] |
|**updateTime** | **String** | Output only. Time when stream payload fields were last updated. |  [optional] [readonly] |
|**webStreamData** | [**GoogleAnalyticsAdminV1betaDataStreamWebStreamData**](GoogleAnalyticsAdminV1betaDataStreamWebStreamData.md) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DATA_STREAM_TYPE_UNSPECIFIED | &quot;DATA_STREAM_TYPE_UNSPECIFIED&quot; |
| WEB_DATA_STREAM | &quot;WEB_DATA_STREAM&quot; |
| ANDROID_APP_DATA_STREAM | &quot;ANDROID_APP_DATA_STREAM&quot; |
| IOS_APP_DATA_STREAM | &quot;IOS_APP_DATA_STREAM&quot; |



