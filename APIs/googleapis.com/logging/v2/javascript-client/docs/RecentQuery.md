# CloudLoggingApi.RecentQuery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lastRunTime** | **String** | Output only. The timestamp when this query was last run. | [optional] [readonly] 
**loggingQuery** | [**LoggingQuery**](LoggingQuery.md) |  | [optional] 
**name** | **String** | Output only. Resource name of the recent query.In the format: \&quot;projects/[PROJECT_ID]/locations/[LOCATION_ID]/recentQueries/[QUERY_ID]\&quot; For a list of supported locations, see Supported Regions (https://cloud.google.com/logging/docs/region-support)The QUERY_ID is a system generated alphanumeric ID. | [optional] [readonly] 
**opsAnalyticsQuery** | [**OpsAnalyticsQuery**](OpsAnalyticsQuery.md) |  | [optional] 


