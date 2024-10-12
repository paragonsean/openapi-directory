# NetBoxApi.WritablePrefix

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**depth** | **Number** |  | [optional] [readonly] 
**children** | **Number** |  | [optional] [readonly] 
**comments** | **String** |  | [optional] 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**description** | **String** |  | [optional] 
**display** | **String** |  | [optional] [readonly] 
**family** | **String** |  | [optional] [readonly] 
**id** | **Number** |  | [optional] [readonly] 
**isPool** | **Boolean** | All IP addresses within this prefix are considered usable | [optional] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**markUtilized** | **Boolean** | Treat as 100% utilized | [optional] 
**prefix** | **String** | IPv4 or IPv6 network with mask | 
**role** | **Number** | The primary function of this prefix | [optional] 
**site** | **Number** |  | [optional] 
**status** | **String** | Operational status of this prefix | [optional] 
**tags** | [**[NestedTag]**](NestedTag.md) |  | [optional] 
**tenant** | **Number** |  | [optional] 
**url** | **String** |  | [optional] [readonly] 
**vlan** | **Number** |  | [optional] 
**vrf** | **Number** |  | [optional] 



## Enum: StatusEnum


* `container` (value: `"container"`)

* `active` (value: `"active"`)

* `reserved` (value: `"reserved"`)

* `deprecated` (value: `"deprecated"`)




