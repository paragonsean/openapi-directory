# SqlManagementClient.ServiceLevelObjectiveCapability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | The unique ID of the service objective. | [optional] [readonly] 
**includedMaxSize** | [**MaxSizeCapability**](MaxSizeCapability.md) |  | [optional] 
**name** | **String** | The service objective name. | [optional] [readonly] 
**performanceLevel** | [**PerformanceLevelCapability**](PerformanceLevelCapability.md) |  | [optional] 
**reason** | **String** | The reason for the capability not being available. | [optional] 
**status** | **String** | The status of the capability. | [optional] [readonly] 
**supportedMaxSizes** | [**[MaxSizeCapability]**](MaxSizeCapability.md) | The list of supported maximum database sizes for this service objective. | [optional] [readonly] 



## Enum: StatusEnum


* `Visible` (value: `"Visible"`)

* `Available` (value: `"Available"`)

* `Default` (value: `"Default"`)

* `Disabled` (value: `"Disabled"`)




