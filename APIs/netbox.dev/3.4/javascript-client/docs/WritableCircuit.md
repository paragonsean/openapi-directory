# NetBoxApi.WritableCircuit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cid** | **String** |  | 
**comments** | **String** |  | [optional] 
**commitRate** | **Number** |  | [optional] 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**description** | **String** |  | [optional] 
**display** | **String** |  | [optional] [readonly] 
**id** | **Number** |  | [optional] [readonly] 
**installDate** | **Date** |  | [optional] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**provider** | **Number** |  | 
**status** | **String** |  | [optional] 
**tags** | [**[NestedTag]**](NestedTag.md) |  | [optional] 
**tenant** | **Number** |  | [optional] 
**terminationA** | **Number** |  | [optional] [readonly] 
**terminationDate** | **Date** |  | [optional] 
**terminationZ** | **Number** |  | [optional] [readonly] 
**type** | **Number** |  | 
**url** | **String** |  | [optional] [readonly] 



## Enum: StatusEnum


* `planned` (value: `"planned"`)

* `provisioning` (value: `"provisioning"`)

* `active` (value: `"active"`)

* `offline` (value: `"offline"`)

* `deprovisioning` (value: `"deprovisioning"`)

* `decommissioned` (value: `"decommissioned"`)




