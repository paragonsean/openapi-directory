# SqlManagementClient.ManagedInstanceVcoresCapability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**includedMaxSize** | [**MaxSizeCapability**](MaxSizeCapability.md) |  | [optional] 
**instancePoolSupported** | **Boolean** | True if this service objective is supported for managed instances in an instance pool. | [optional] [readonly] 
**name** | **String** | The virtual cores identifier. | [optional] [readonly] 
**reason** | **String** | The reason for the capability not being available. | [optional] 
**standaloneSupported** | **Boolean** | True if this service objective is supported for standalone managed instances. | [optional] [readonly] 
**status** | **String** | The status of the capability. | [optional] [readonly] 
**supportedStorageSizes** | [**[MaxSizeRangeCapability]**](MaxSizeRangeCapability.md) | Storage size ranges. | [optional] [readonly] 
**value** | **Number** | The virtual cores value. | [optional] [readonly] 



## Enum: StatusEnum


* `Visible` (value: `"Visible"`)

* `Available` (value: `"Available"`)

* `Default` (value: `"Default"`)

* `Disabled` (value: `"Disabled"`)




