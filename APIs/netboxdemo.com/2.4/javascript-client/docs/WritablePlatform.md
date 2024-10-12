# NetBoxApi.WritablePlatform

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **Number** |  | [optional] [readonly] 
**manufacturer** | **Number** | Optionally limit this platform to devices of a certain manufacturer | [optional] 
**name** | **String** |  | 
**napalmArgs** | **String** | Additional arguments to pass when initiating the NAPALM driver (JSON format) | [optional] 
**napalmDriver** | **String** | The name of the NAPALM driver to use when interacting with devices | [optional] 
**rpcClient** | **String** |  | [optional] 
**slug** | **String** |  | 



## Enum: RpcClientEnum


* `juniper-junos` (value: `"juniper-junos"`)

* `cisco-ios` (value: `"cisco-ios"`)

* `opengear` (value: `"opengear"`)




