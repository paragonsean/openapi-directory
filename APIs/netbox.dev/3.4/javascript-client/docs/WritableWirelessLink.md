# NetBoxApi.WritableWirelessLink

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authCipher** | **String** |  | [optional] 
**authPsk** | **String** |  | [optional] 
**authType** | **String** |  | [optional] 
**comments** | **String** |  | [optional] 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**description** | **String** |  | [optional] 
**display** | **String** |  | [optional] [readonly] 
**id** | **Number** |  | [optional] [readonly] 
**interfaceA** | **Number** |  | 
**interfaceB** | **Number** |  | 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**ssid** | **String** |  | [optional] 
**status** | **String** |  | [optional] 
**tags** | [**[NestedTag]**](NestedTag.md) |  | [optional] 
**tenant** | **Number** |  | [optional] 
**url** | **String** |  | [optional] [readonly] 



## Enum: AuthCipherEnum


* `auto` (value: `"auto"`)

* `tkip` (value: `"tkip"`)

* `aes` (value: `"aes"`)





## Enum: AuthTypeEnum


* `open` (value: `"open"`)

* `wep` (value: `"wep"`)

* `wpa-personal` (value: `"wpa-personal"`)

* `wpa-enterprise` (value: `"wpa-enterprise"`)





## Enum: StatusEnum


* `connected` (value: `"connected"`)

* `planned` (value: `"planned"`)

* `decommissioning` (value: `"decommissioning"`)




