

# CacheExpirationActionParameters

Defines the parameters for the cache expiration action.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**atOdataType** | [**AtOdataTypeEnum**](#AtOdataTypeEnum) |  |  |
|**cacheBehavior** | [**CacheBehaviorEnum**](#CacheBehaviorEnum) | Caching behavior for the requests |  |
|**cacheDuration** | **String** | The duration for which the content needs to be cached. Allowed format is [d.]hh:mm:ss |  [optional] |
|**cacheType** | [**CacheTypeEnum**](#CacheTypeEnum) | The level at which the content needs to be cached. |  |



## Enum: AtOdataTypeEnum

| Name | Value |
|---- | -----|
| _MICROSOFT_AZURE_CDN_MODELS_DELIVERY_RULE_CACHE_EXPIRATION_ACTION_PARAMETERS | &quot;#Microsoft.Azure.Cdn.Models.DeliveryRuleCacheExpirationActionParameters&quot; |



## Enum: CacheBehaviorEnum

| Name | Value |
|---- | -----|
| BYPASS_CACHE | &quot;BypassCache&quot; |
| OVERRIDE | &quot;Override&quot; |
| SET_IF_MISSING | &quot;SetIfMissing&quot; |



## Enum: CacheTypeEnum

| Name | Value |
|---- | -----|
| ALL | &quot;All&quot; |



