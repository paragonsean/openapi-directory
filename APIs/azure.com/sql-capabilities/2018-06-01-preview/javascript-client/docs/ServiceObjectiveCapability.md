# SqlManagementClient.ServiceObjectiveCapability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**computeModel** | **String** | The compute model | [optional] [readonly] 
**id** | **String** | The unique ID of the service objective. | [optional] [readonly] 
**includedMaxSize** | [**MaxSizeCapability**](MaxSizeCapability.md) |  | [optional] 
**name** | **String** | The service objective name. | [optional] [readonly] 
**performanceLevel** | [**PerformanceLevelCapability**](PerformanceLevelCapability.md) |  | [optional] 
**reason** | **String** | The reason for the capability not being available. | [optional] 
**sku** | [**ElasticPoolPerformanceLevelCapabilitySku**](ElasticPoolPerformanceLevelCapabilitySku.md) |  | [optional] 
**status** | **String** | The status of the capability. | [optional] [readonly] 
**supportedAutoPauseDelay** | [**AutoPauseDelayTimeRange**](AutoPauseDelayTimeRange.md) |  | [optional] 
**supportedLicenseTypes** | [**[LicenseTypeCapability]**](LicenseTypeCapability.md) | List of supported license types. | [optional] [readonly] 
**supportedMaxSizes** | [**[MaxSizeRangeCapability]**](MaxSizeRangeCapability.md) | The list of supported maximum database sizes. | [optional] [readonly] 
**supportedMinCapacities** | [**[MinCapacityCapability]**](MinCapacityCapability.md) | List of supported min capacities | [optional] [readonly] 
**zoneRedundant** | **Boolean** | Whether or not zone redundancy is supported for the service objective. | [optional] [readonly] 



## Enum: StatusEnum


* `Visible` (value: `"Visible"`)

* `Available` (value: `"Available"`)

* `Default` (value: `"Default"`)

* `Disabled` (value: `"Disabled"`)




