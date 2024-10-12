# HetznerCloudApi.CreateFloatingIPRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** |  | [optional] 
**homeLocation** | **String** | Home Location (routing is optimized for that Location). Only optional if Server argument is passed. | [optional] 
**labels** | **Object** | User-defined labels (key-value pairs) | [optional] 
**name** | **String** |  | [optional] 
**server** | **Number** | Server to assign the Floating IP to | [optional] 
**type** | **String** | Floating IP type | 



## Enum: TypeEnum


* `ipv4` (value: `"ipv4"`)

* `ipv6` (value: `"ipv6"`)




