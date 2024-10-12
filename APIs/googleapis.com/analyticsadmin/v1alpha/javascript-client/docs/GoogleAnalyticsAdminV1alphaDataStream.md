# GoogleAnalyticsAdminApi.GoogleAnalyticsAdminV1alphaDataStream

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**androidAppStreamData** | [**GoogleAnalyticsAdminV1alphaDataStreamAndroidAppStreamData**](GoogleAnalyticsAdminV1alphaDataStreamAndroidAppStreamData.md) |  | [optional] 
**createTime** | **String** | Output only. Time when this stream was originally created. | [optional] [readonly] 
**displayName** | **String** | Human-readable display name for the Data Stream. Required for web data streams. The max allowed display name length is 255 UTF-16 code units. | [optional] 
**iosAppStreamData** | [**GoogleAnalyticsAdminV1alphaDataStreamIosAppStreamData**](GoogleAnalyticsAdminV1alphaDataStreamIosAppStreamData.md) |  | [optional] 
**name** | **String** | Output only. Resource name of this Data Stream. Format: properties/{property_id}/dataStreams/{stream_id} Example: \&quot;properties/1000/dataStreams/2000\&quot; | [optional] [readonly] 
**type** | **String** | Required. Immutable. The type of this DataStream resource. | [optional] 
**updateTime** | **String** | Output only. Time when stream payload fields were last updated. | [optional] [readonly] 
**webStreamData** | [**GoogleAnalyticsAdminV1alphaDataStreamWebStreamData**](GoogleAnalyticsAdminV1alphaDataStreamWebStreamData.md) |  | [optional] 



## Enum: TypeEnum


* `DATA_STREAM_TYPE_UNSPECIFIED` (value: `"DATA_STREAM_TYPE_UNSPECIFIED"`)

* `WEB_DATA_STREAM` (value: `"WEB_DATA_STREAM"`)

* `ANDROID_APP_DATA_STREAM` (value: `"ANDROID_APP_DATA_STREAM"`)

* `IOS_APP_DATA_STREAM` (value: `"IOS_APP_DATA_STREAM"`)




