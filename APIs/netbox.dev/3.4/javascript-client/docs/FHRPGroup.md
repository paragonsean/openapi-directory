# NetBoxApi.FHRPGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authKey** | **String** |  | [optional] 
**authType** | **String** |  | [optional] 
**comments** | **String** |  | [optional] 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**description** | **String** |  | [optional] 
**display** | **String** |  | [optional] [readonly] 
**groupId** | **Number** |  | 
**id** | **Number** |  | [optional] [readonly] 
**ipAddresses** | [**[NestedIPAddress]**](NestedIPAddress.md) |  | [optional] [readonly] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**name** | **String** |  | [optional] 
**protocol** | **String** |  | 
**tags** | [**[NestedTag]**](NestedTag.md) |  | [optional] 
**url** | **String** |  | [optional] [readonly] 



## Enum: AuthTypeEnum


* `plaintext` (value: `"plaintext"`)

* `md5` (value: `"md5"`)





## Enum: ProtocolEnum


* `vrrp2` (value: `"vrrp2"`)

* `vrrp3` (value: `"vrrp3"`)

* `carp` (value: `"carp"`)

* `clusterxl` (value: `"clusterxl"`)

* `hsrp` (value: `"hsrp"`)

* `glbp` (value: `"glbp"`)

* `other` (value: `"other"`)




