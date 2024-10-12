# NetBoxApi.WritableModule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assetTag** | **String** | A unique tag used to identify this device | [optional] 
**comments** | **String** |  | [optional] 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**description** | **String** |  | [optional] 
**device** | **Number** |  | 
**display** | **String** |  | [optional] [readonly] 
**id** | **Number** |  | [optional] [readonly] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**moduleBay** | **Number** |  | 
**moduleType** | **Number** |  | 
**serial** | **String** |  | [optional] 
**status** | **String** |  | [optional] 
**tags** | [**[NestedTag]**](NestedTag.md) |  | [optional] 
**url** | **String** |  | [optional] [readonly] 



## Enum: StatusEnum


* `offline` (value: `"offline"`)

* `active` (value: `"active"`)

* `planned` (value: `"planned"`)

* `staged` (value: `"staged"`)

* `failed` (value: `"failed"`)

* `decommissioning` (value: `"decommissioning"`)




