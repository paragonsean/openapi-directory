# NetBoxApi.VirtualDeviceContext

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | **String** |  | [optional] 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**description** | **String** |  | [optional] 
**device** | [**NestedDevice**](NestedDevice.md) |  | 
**display** | **String** |  | [optional] [readonly] 
**id** | **Number** |  | [optional] [readonly] 
**identifier** | **Number** | Numeric identifier unique to the parent device | [optional] 
**interfaceCount** | **Number** |  | [optional] [readonly] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**name** | **String** |  | 
**primaryIp** | [**NestedIPAddress**](NestedIPAddress.md) |  | [optional] 
**primaryIp4** | [**NestedIPAddress**](NestedIPAddress.md) |  | [optional] 
**primaryIp6** | [**NestedIPAddress**](NestedIPAddress.md) |  | [optional] 
**status** | **String** |  | 
**tags** | [**[NestedTag]**](NestedTag.md) |  | [optional] 
**tenant** | [**NestedTenant**](NestedTenant.md) |  | [optional] 
**url** | **String** |  | [optional] [readonly] 



## Enum: StatusEnum


* `active` (value: `"active"`)

* `planned` (value: `"planned"`)

* `offline` (value: `"offline"`)




