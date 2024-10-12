# MicrosoftNetApp.PoolProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poolId** | **String** | UUID v4 used to identify the Pool | [optional] [readonly] 
**provisioningState** | **String** | Azure lifecycle management | [optional] [readonly] 
**serviceLevel** | **String** | The service level of the file system | [optional] [default to &#39;Premium&#39;]
**size** | **Number** | Provisioned size of the pool (in bytes). Allowed values are in 4TiB chunks (value must be multiply of 4398046511104). | [optional] [default to 4398046511104]



## Enum: ServiceLevelEnum


* `Standard` (value: `"Standard"`)

* `Premium` (value: `"Premium"`)

* `Ultra` (value: `"Ultra"`)




