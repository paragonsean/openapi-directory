# StreamAnalyticsManagementClient.InputProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diagnostics** | [**Diagnostics**](Diagnostics.md) |  | [optional] 
**etag** | **String** | The current entity tag for the input. This is an opaque string. You can use it to detect whether the resource has changed between requests. You can also use it in the If-Match or If-None-Match headers for write operations for optimistic concurrency. | [optional] [readonly] 
**serialization** | [**Serialization**](Serialization.md) |  | [optional] 
**type** | **String** | Indicates whether the input is a source of reference data or stream data. Required on PUT (CreateOrReplace) requests. | [optional] 


