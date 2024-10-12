

# ConfiguredRouteDetails


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeErrorOverride** | **Boolean** | Whether error overrides are enabled or not. |  [optional] |
|**activeLatency** | **Boolean** | Whether latency delays are enabled or not. |  [optional] |
|**defaultLatency** | **Integer** | A delay in milliseconds applied to requests at a &#39;normal&#39; level. |  [optional] |
|**errorOverrideType** | [**ErrorOverrideTypeEnum**](#ErrorOverrideTypeEnum) | The type of error override applied to this route. |  |
|**loadLatency** | **Integer** | A delay in milliseconds applied to requests at a &#39;high&#39; level. |  [optional] |
|**loadThreshold** | **Integer** | The threshold in transactions/second to signify &#39;high&#39; load |  [optional] |
|**method** | **String** |  |  [optional] |
|**path** | **String** |  |  [optional] |
|**properties** | **Map&lt;String, String&gt;** |  |  [optional] |
|**routeConfig** | [**RouteConfig**](RouteConfig.md) |  |  [optional] |
|**transport** | **String** |  |  [optional] |



## Enum: ErrorOverrideTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;NONE&quot; |
| TIMEOUT | &quot;TIMEOUT&quot; |
| SERVICE_DOWN | &quot;SERVICE_DOWN&quot; |



