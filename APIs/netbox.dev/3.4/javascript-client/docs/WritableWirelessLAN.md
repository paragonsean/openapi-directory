# NetBoxApi.WritableWirelessLAN

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
**group** | **Number** |  | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**ssid** | **String** |  | 
**status** | **String** |  | [optional] 
**tags** | [**[NestedTag]**](NestedTag.md) |  | [optional] 
**tenant** | **Number** |  | [optional] 
**url** | **String** |  | [optional] [readonly] 
**vlan** | **Number** |  | [optional] 



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


* `active` (value: `"active"`)

* `reserved` (value: `"reserved"`)

* `disabled` (value: `"disabled"`)

* `deprecated` (value: `"deprecated"`)




