# SandboxApi.ConfiguredRouteDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeErrorOverride** | **Boolean** | Whether error overrides are enabled or not. | [optional] 
**activeLatency** | **Boolean** | Whether latency delays are enabled or not. | [optional] 
**defaultLatency** | **Number** | A delay in milliseconds applied to requests at a &#39;normal&#39; level. | [optional] 
**errorOverrideType** | **String** | The type of error override applied to this route. | 
**loadLatency** | **Number** | A delay in milliseconds applied to requests at a &#39;high&#39; level. | [optional] 
**loadThreshold** | **Number** | The threshold in transactions/second to signify &#39;high&#39; load | [optional] 
**method** | **String** |  | [optional] 
**path** | **String** |  | [optional] 
**properties** | **{String: String}** |  | [optional] 
**routeConfig** | [**RouteConfig**](RouteConfig.md) |  | [optional] 
**transport** | **String** |  | [optional] 



## Enum: ErrorOverrideTypeEnum


* `NONE` (value: `"NONE"`)

* `TIMEOUT` (value: `"TIMEOUT"`)

* `SERVICE_DOWN` (value: `"SERVICE_DOWN"`)




