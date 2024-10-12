# NetBoxApi.WritableIPAddress

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **String** | IPv4 or IPv6 address (with mask) | 
**assignedObject** | **Object** |  | [optional] [readonly] 
**assignedObjectId** | **Number** |  | [optional] 
**assignedObjectType** | **String** |  | [optional] 
**comments** | **String** |  | [optional] 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**description** | **String** |  | [optional] 
**display** | **String** |  | [optional] [readonly] 
**dnsName** | **String** | Hostname or FQDN (not case-sensitive) | [optional] 
**family** | **String** |  | [optional] [readonly] 
**id** | **Number** |  | [optional] [readonly] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**natInside** | **Number** | The IP for which this address is the \&quot;outside\&quot; IP | [optional] 
**natOutside** | [**[NestedIPAddress]**](NestedIPAddress.md) |  | [optional] [readonly] 
**role** | **String** | The functional role of this IP | [optional] 
**status** | **String** | The operational status of this IP | [optional] 
**tags** | [**[NestedTag]**](NestedTag.md) |  | [optional] 
**tenant** | **Number** |  | [optional] 
**url** | **String** |  | [optional] [readonly] 
**vrf** | **Number** |  | [optional] 



## Enum: RoleEnum


* `loopback` (value: `"loopback"`)

* `secondary` (value: `"secondary"`)

* `anycast` (value: `"anycast"`)

* `vip` (value: `"vip"`)

* `vrrp` (value: `"vrrp"`)

* `hsrp` (value: `"hsrp"`)

* `glbp` (value: `"glbp"`)

* `carp` (value: `"carp"`)





## Enum: StatusEnum


* `active` (value: `"active"`)

* `reserved` (value: `"reserved"`)

* `deprecated` (value: `"deprecated"`)

* `dhcp` (value: `"dhcp"`)

* `slaac` (value: `"slaac"`)




