# NetBoxApi.WritableVirtualMachineWithConfigContext

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | **Number** |  | 
**comments** | **String** |  | [optional] 
**configContext** | **{String: String}** |  | [optional] [readonly] 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**disk** | **Number** |  | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**localContextData** | **String** |  | [optional] 
**memory** | **Number** |  | [optional] 
**name** | **String** |  | 
**platform** | **Number** |  | [optional] 
**primaryIp** | **String** |  | [optional] [readonly] 
**primaryIp4** | **Number** |  | [optional] 
**primaryIp6** | **Number** |  | [optional] 
**role** | **Number** |  | [optional] 
**site** | **String** |  | [optional] [readonly] 
**status** | **String** |  | [optional] 
**tags** | **[String]** |  | [optional] 
**tenant** | **Number** |  | [optional] 
**vcpus** | **Number** |  | [optional] 



## Enum: StatusEnum


* `offline` (value: `"offline"`)

* `active` (value: `"active"`)

* `planned` (value: `"planned"`)

* `staged` (value: `"staged"`)

* `failed` (value: `"failed"`)

* `decommissioning` (value: `"decommissioning"`)




