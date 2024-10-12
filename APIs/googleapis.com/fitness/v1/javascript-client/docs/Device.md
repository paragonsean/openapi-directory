# FitnessApi.Device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manufacturer** | **String** | Manufacturer of the product/hardware. | [optional] 
**model** | **String** | End-user visible model name for the device. | [optional] 
**type** | **String** | A constant representing the type of the device. | [optional] 
**uid** | **String** | The serial number or other unique ID for the hardware. This field is obfuscated when read by any REST or Android client that did not create the data source. Only the data source creator will see the uid field in clear and normal form. The obfuscation preserves equality; that is, given two IDs, if id1 &#x3D;&#x3D; id2, obfuscated(id1) &#x3D;&#x3D; obfuscated(id2). | [optional] 
**version** | **String** | Version string for the device hardware/software. | [optional] 



## Enum: TypeEnum


* `unknown` (value: `"unknown"`)

* `phone` (value: `"phone"`)

* `tablet` (value: `"tablet"`)

* `watch` (value: `"watch"`)

* `chestStrap` (value: `"chestStrap"`)

* `scale` (value: `"scale"`)

* `headMounted` (value: `"headMounted"`)

* `smartDisplay` (value: `"smartDisplay"`)




