# CdnManagementClient.CacheExpirationActionParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**odataType** | **String** |  | 
**cacheBehavior** | **String** | Caching behavior for the requests | 
**cacheDuration** | **String** | The duration for which the content needs to be cached. Allowed format is [d.]hh:mm:ss | [optional] 
**cacheType** | **String** | The level at which the content needs to be cached. | 



## Enum: OdataTypeEnum


* `#Microsoft.Azure.Cdn.Models.DeliveryRuleCacheExpirationActionParameters` (value: `"#Microsoft.Azure.Cdn.Models.DeliveryRuleCacheExpirationActionParameters"`)





## Enum: CacheBehaviorEnum


* `BypassCache` (value: `"BypassCache"`)

* `Override` (value: `"Override"`)

* `SetIfMissing` (value: `"SetIfMissing"`)





## Enum: CacheTypeEnum


* `All` (value: `"All"`)




