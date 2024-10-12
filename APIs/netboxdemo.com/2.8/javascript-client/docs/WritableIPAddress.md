# NetBoxApi.WritableIPAddress

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **String** | IPv4 or IPv6 address (with mask) | 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**description** | **String** |  | [optional] 
**dnsName** | **String** | Hostname or FQDN (not case-sensitive) | [optional] 
**family** | **String** |  | [optional] [readonly] 
**id** | **Number** |  | [optional] [readonly] 
**_interface** | **Number** |  | [optional] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**natInside** | **Number** | The IP for which this address is the \&quot;outside\&quot; IP | [optional] 
**natOutside** | **Number** |  | 
**role** | **String** | The functional role of this IP | [optional] 
**status** | **String** | The operational status of this IP | [optional] 
**tags** | **[String]** |  | [optional] 
**tenant** | **Number** |  | [optional] 
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




