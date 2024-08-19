

# CacheKeyQueryStringActionParameters

Defines the parameters for the cache-key query string action.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**atOdataType** | [**AtOdataTypeEnum**](#AtOdataTypeEnum) |  |  |
|**queryParameters** | **String** | query parameters to include or exclude (comma separated). |  [optional] |
|**queryStringBehavior** | [**QueryStringBehaviorEnum**](#QueryStringBehaviorEnum) | Caching behavior for the requests |  |



## Enum: AtOdataTypeEnum

| Name | Value |
|---- | -----|
| _MICROSOFT_AZURE_CDN_MODELS_DELIVERY_RULE_CACHE_KEY_QUERY_STRING_BEHAVIOR_ACTION_PARAMETERS | &quot;#Microsoft.Azure.Cdn.Models.DeliveryRuleCacheKeyQueryStringBehaviorActionParameters&quot; |



## Enum: QueryStringBehaviorEnum

| Name | Value |
|---- | -----|
| INCLUDE | &quot;Include&quot; |
| INCLUDE_ALL | &quot;IncludeAll&quot; |
| EXCLUDE | &quot;Exclude&quot; |
| EXCLUDE_ALL | &quot;ExcludeAll&quot; |



