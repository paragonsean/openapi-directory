

# CloudCdnWorkload

Specifies usage for Cloud CDN resources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cacheFillOriginService** | [**CacheFillOriginServiceEnum**](#CacheFillOriginServiceEnum) | The source service for the cache fill. |  [optional] |
|**cacheFillRate** | [**Usage**](Usage.md) |  |  [optional] |
|**cacheFillRegions** | [**CacheFillRegions**](CacheFillRegions.md) |  |  [optional] |
|**cacheLookUpRate** | [**Usage**](Usage.md) |  |  [optional] |



## Enum: CacheFillOriginServiceEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;CACHE_FILL_ORIGIN_SERVICE_UNSPECIFIED&quot; |
| GOOGLE_CLOUD_STORAGE_BUCKET | &quot;CACHE_FILL_ORIGIN_SERVICE_GOOGLE_CLOUD_STORAGE_BUCKET&quot; |
| BACKEND_SERVICE | &quot;CACHE_FILL_ORIGIN_SERVICE_BACKEND_SERVICE&quot; |



