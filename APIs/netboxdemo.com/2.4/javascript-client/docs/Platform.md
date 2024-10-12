# NetBoxApi.Platform

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **Number** |  | [optional] [readonly] 
**manufacturer** | [**NestedManufacturer**](NestedManufacturer.md) |  | [optional] 
**name** | **String** |  | 
**napalmArgs** | **String** | Additional arguments to pass when initiating the NAPALM driver (JSON format) | [optional] 
**napalmDriver** | **String** | The name of the NAPALM driver to use when interacting with devices | [optional] 
**rpcClient** | **String** |  | [optional] 
**slug** | **String** |  | 



## Enum: RpcClientEnum


* `juniper-junos` (value: `"juniper-junos"`)

* `cisco-ios` (value: `"cisco-ios"`)

* `opengear` (value: `"opengear"`)




