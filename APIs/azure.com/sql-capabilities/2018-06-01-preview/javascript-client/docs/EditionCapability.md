# SqlManagementClient.EditionCapability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The database edition name. | [optional] [readonly] 
**readScale** | [**ReadScaleCapability**](ReadScaleCapability.md) |  | [optional] 
**reason** | **String** | The reason for the capability not being available. | [optional] 
**status** | **String** | The status of the capability. | [optional] [readonly] 
**supportedServiceLevelObjectives** | [**[ServiceObjectiveCapability]**](ServiceObjectiveCapability.md) | The list of supported service objectives for the edition. | [optional] [readonly] 
**supportedStorageCapabilities** | [**[StorageCapability]**](StorageCapability.md) | The list of supported storage capabilities for this edition | [optional] [readonly] 
**zoneRedundant** | **Boolean** | Whether or not zone redundancy is supported for the edition. | [optional] [readonly] 



## Enum: StatusEnum


* `Visible` (value: `"Visible"`)

* `Available` (value: `"Available"`)

* `Default` (value: `"Default"`)

* `Disabled` (value: `"Disabled"`)




