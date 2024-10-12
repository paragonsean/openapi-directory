# NetBoxApi.WritableVirtualMachineWithConfigContext

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | **Number** |  | [optional] 
**comments** | **String** |  | [optional] 
**configContext** | **Object** |  | [optional] [readonly] 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**description** | **String** |  | [optional] 
**device** | **Number** |  | [optional] 
**disk** | **Number** |  | [optional] 
**display** | **String** |  | [optional] [readonly] 
**id** | **Number** |  | [optional] [readonly] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**localContextData** | **Object** |  | [optional] 
**memory** | **Number** |  | [optional] 
**name** | **String** |  | 
**platform** | **Number** |  | [optional] 
**primaryIp** | **String** |  | [optional] [readonly] 
**primaryIp4** | **Number** |  | [optional] 
**primaryIp6** | **Number** |  | [optional] 
**role** | **Number** |  | [optional] 
**site** | **Number** |  | [optional] 
**status** | **String** |  | [optional] 
**tags** | [**[NestedTag]**](NestedTag.md) |  | [optional] 
**tenant** | **Number** |  | [optional] 
**url** | **String** |  | [optional] [readonly] 
**vcpus** | **Number** |  | [optional] 



## Enum: StatusEnum


* `offline` (value: `"offline"`)

* `active` (value: `"active"`)

* `planned` (value: `"planned"`)

* `staged` (value: `"staged"`)

* `failed` (value: `"failed"`)

* `decommissioning` (value: `"decommissioning"`)




