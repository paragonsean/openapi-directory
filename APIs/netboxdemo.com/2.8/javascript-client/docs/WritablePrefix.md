# NetBoxApi.WritablePrefix

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**description** | **String** |  | [optional] 
**family** | **String** |  | [optional] [readonly] 
**id** | **Number** |  | [optional] [readonly] 
**isPool** | **Boolean** | All IP addresses within this prefix are considered usable | [optional] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**prefix** | **String** | IPv4 or IPv6 network with mask | 
**role** | **Number** | The primary function of this prefix | [optional] 
**site** | **Number** |  | [optional] 
**status** | **String** | Operational status of this prefix | [optional] 
**tags** | **[String]** |  | [optional] 
**tenant** | **Number** |  | [optional] 
**vlan** | **Number** |  | [optional] 
**vrf** | **Number** |  | [optional] 



## Enum: StatusEnum


* `container` (value: `"container"`)

* `active` (value: `"active"`)

* `reserved` (value: `"reserved"`)

* `deprecated` (value: `"deprecated"`)




