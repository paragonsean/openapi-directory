# StorageCacheMgmtClient.Cache

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | A fully qualified URL. | [optional] 
**location** | **String** | Region name string. | [optional] 
**name** | **String** | Schema for the name of resources served by this provider. Note that objects will contain an odata @id annotation as appropriate. This will contain the complete URL of the object. These names are case-preserving, but not case sensitive. | [optional] 
**properties** | [**CacheProperties**](CacheProperties.md) |  | [optional] 
**sku** | [**CacheSku**](CacheSku.md) |  | [optional] 
**tags** | **Object** | ARM tags as name/value pairs. | [optional] 
**type** | **String** | Type of the Cache; Microsoft.StorageCache/Cache | [optional] [readonly] 


