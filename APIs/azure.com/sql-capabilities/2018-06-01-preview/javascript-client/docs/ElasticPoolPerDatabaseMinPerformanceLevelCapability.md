# SqlManagementClient.ElasticPoolPerDatabaseMinPerformanceLevelCapability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **Number** | The minimum performance level per database. | [optional] [readonly] 
**reason** | **String** | The reason for the capability not being available. | [optional] 
**status** | **String** | The status of the capability. | [optional] [readonly] 
**unit** | **String** | Unit type used to measure performance level. | [optional] [readonly] 



## Enum: StatusEnum


* `Visible` (value: `"Visible"`)

* `Available` (value: `"Available"`)

* `Default` (value: `"Default"`)

* `Disabled` (value: `"Disabled"`)





## Enum: UnitEnum


* `DTU` (value: `"DTU"`)

* `VCores` (value: `"VCores"`)




