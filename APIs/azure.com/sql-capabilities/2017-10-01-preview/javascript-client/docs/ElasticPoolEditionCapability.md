# SqlManagementClient.ElasticPoolEditionCapability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The elastic pool edition name. | [optional] [readonly] 
**reason** | **String** | The reason for the capability not being available. | [optional] 
**status** | **String** | The status of the capability. | [optional] [readonly] 
**supportedElasticPoolPerformanceLevels** | [**[ElasticPoolPerformanceLevelCapability]**](ElasticPoolPerformanceLevelCapability.md) | The list of supported elastic pool DTU levels for the edition. | [optional] [readonly] 
**zoneRedundant** | **Boolean** | Whether or not zone redundancy is supported for the edition. | [optional] [readonly] 



## Enum: StatusEnum


* `Visible` (value: `"Visible"`)

* `Available` (value: `"Available"`)

* `Default` (value: `"Default"`)

* `Disabled` (value: `"Disabled"`)




