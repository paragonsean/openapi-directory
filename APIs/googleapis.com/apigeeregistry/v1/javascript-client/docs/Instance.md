# ApigeeRegistryApi.Instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build** | [**Build**](Build.md) |  | [optional] 
**config** | [**Config**](Config.md) |  | [optional] 
**createTime** | **String** | Output only. Creation timestamp. | [optional] [readonly] 
**name** | **String** | Format: &#x60;projects/_*_/locations/_*_/instance&#x60;. Currently only &#x60;locations/global&#x60; is supported. | [optional] 
**state** | **String** | Output only. The current state of the Instance. | [optional] [readonly] 
**stateMessage** | **String** | Output only. Extra information of Instance.State if the state is &#x60;FAILED&#x60;. | [optional] [readonly] 
**updateTime** | **String** | Output only. Last update timestamp. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `INACTIVE` (value: `"INACTIVE"`)

* `CREATING` (value: `"CREATING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `UPDATING` (value: `"UPDATING"`)

* `DELETING` (value: `"DELETING"`)

* `FAILED` (value: `"FAILED"`)




