# NetBoxApi.WritableIPRange

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | **Number** |  | [optional] [readonly] 
**comments** | **String** |  | [optional] 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**description** | **String** |  | [optional] 
**display** | **String** |  | [optional] [readonly] 
**endAddress** | **String** | IPv4 or IPv6 address (with mask) | 
**family** | **String** |  | [optional] [readonly] 
**id** | **Number** |  | [optional] [readonly] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**role** | **Number** | The primary function of this range | [optional] 
**size** | **Number** |  | [optional] [readonly] 
**startAddress** | **String** | IPv4 or IPv6 address (with mask) | 
**status** | **String** | Operational status of this range | [optional] 
**tags** | [**[NestedTag]**](NestedTag.md) |  | [optional] 
**tenant** | **Number** |  | [optional] 
**url** | **String** |  | [optional] [readonly] 
**vrf** | **Number** |  | [optional] 



## Enum: StatusEnum


* `active` (value: `"active"`)

* `reserved` (value: `"reserved"`)

* `deprecated` (value: `"deprecated"`)




