# CloudLoggingApi.SavedQuery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The timestamp when the saved query was created. | [optional] [readonly] 
**description** | **String** | Optional. A human readable description of the saved query. | [optional] 
**displayName** | **String** | Optional. The user specified title for the SavedQuery. | [optional] 
**loggingQuery** | [**LoggingQuery**](LoggingQuery.md) |  | [optional] 
**name** | **String** | Output only. Resource name of the saved query.In the format: \&quot;projects/[PROJECT_ID]/locations/[LOCATION_ID]/savedQueries/[QUERY_ID]\&quot; For a list of supported locations, see Supported Regions (https://cloud.google.com/logging/docs/region-support#bucket-regions)After the saved query is created, the location cannot be changed.If the user doesn&#39;t provide a QUERY_ID, the system will generate an alphanumeric ID. | [optional] [readonly] 
**opsAnalyticsQuery** | [**OpsAnalyticsQuery**](OpsAnalyticsQuery.md) |  | [optional] 
**updateTime** | **String** | Output only. The timestamp when the saved query was last updated. | [optional] [readonly] 
**visibility** | **String** | Required. The visibility status of this query, which determines its ownership. | [optional] 



## Enum: VisibilityEnum


* `VISIBILITY_UNSPECIFIED` (value: `"VISIBILITY_UNSPECIFIED"`)

* `PRIVATE` (value: `"PRIVATE"`)

* `SHARED` (value: `"SHARED"`)




