# StorageManagementClient.ShareProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**freeCapacity** | **Number** | The free space of the storage share in bytes. | [optional] [readonly] 
**healthStatus** | **String** | Current health status. | [optional] [readonly] 
**shareName** | **String** | The name of the storage share. | [optional] [readonly] 
**totalCapacity** | **Number** | The total capacity of the storage share in bytes. | [optional] [readonly] 
**uncPath** | **String** | The UNC path to the storage share. | [optional] [readonly] 
**usedCapacity** | **Number** | The used capacity of the storage share in bytes. | [optional] [readonly] 



## Enum: HealthStatusEnum


* `Unknown` (value: `"Unknown"`)

* `Healthy` (value: `"Healthy"`)

* `Warning` (value: `"Warning"`)

* `Critical` (value: `"Critical"`)




