# NetBoxApi.WritableIPAddress

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **String** | IPv4 or IPv6 address (with mask) | 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**description** | **String** |  | [optional] 
**family** | **Number** |  | [optional] [readonly] 
**id** | **Number** |  | [optional] [readonly] 
**_interface** | **Number** |  | [optional] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**natInside** | **Number** | The IP for which this address is the \&quot;outside\&quot; IP | [optional] 
**natOutside** | **Number** |  | 
**role** | **Number** | The functional role of this IP | [optional] 
**status** | **Number** | The operational status of this IP | [optional] 
**tags** | **[String]** |  | [optional] 
**tenant** | **Number** |  | [optional] 
**vrf** | **Number** |  | [optional] 



## Enum: RoleEnum


* `10` (value: `10`)

* `20` (value: `20`)

* `30` (value: `30`)

* `40` (value: `40`)

* `41` (value: `41`)

* `42` (value: `42`)

* `43` (value: `43`)

* `44` (value: `44`)





## Enum: StatusEnum


* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)

* `5` (value: `5`)




