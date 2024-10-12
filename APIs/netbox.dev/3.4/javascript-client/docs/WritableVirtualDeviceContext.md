# NetBoxApi.WritableVirtualDeviceContext

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | **String** |  | [optional] 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**description** | **String** |  | [optional] 
**device** | **Number** |  | [optional] 
**display** | **String** |  | [optional] [readonly] 
**id** | **Number** |  | [optional] [readonly] 
**identifier** | **Number** | Numeric identifier unique to the parent device | [optional] 
**interfaceCount** | **Number** |  | [optional] [readonly] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**name** | **String** |  | 
**primaryIp** | **String** |  | [optional] [readonly] 
**primaryIp4** | **Number** |  | [optional] 
**primaryIp6** | **Number** |  | [optional] 
**status** | **String** |  | 
**tags** | [**[NestedTag]**](NestedTag.md) |  | [optional] 
**tenant** | **Number** |  | [optional] 
**url** | **String** |  | [optional] [readonly] 



## Enum: StatusEnum


* `active` (value: `"active"`)

* `planned` (value: `"planned"`)

* `offline` (value: `"offline"`)




