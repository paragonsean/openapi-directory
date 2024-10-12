# CloudBillingApi.CloudCdnWorkload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cacheFillOriginService** | **String** | The source service for the cache fill. | [optional] 
**cacheFillRate** | [**Usage**](Usage.md) |  | [optional] 
**cacheFillRegions** | [**CacheFillRegions**](CacheFillRegions.md) |  | [optional] 
**cacheLookUpRate** | [**Usage**](Usage.md) |  | [optional] 



## Enum: CacheFillOriginServiceEnum


* `UNSPECIFIED` (value: `"CACHE_FILL_ORIGIN_SERVICE_UNSPECIFIED"`)

* `GOOGLE_CLOUD_STORAGE_BUCKET` (value: `"CACHE_FILL_ORIGIN_SERVICE_GOOGLE_CLOUD_STORAGE_BUCKET"`)

* `BACKEND_SERVICE` (value: `"CACHE_FILL_ORIGIN_SERVICE_BACKEND_SERVICE"`)




