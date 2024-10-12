# SqlManagementClient.ElasticPoolPerDatabaseMaxDtuCapability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **Number** | The maximum DTUs per database. | [optional] [readonly] 
**reason** | **String** | The reason for the capability not being available. | [optional] 
**status** | **String** | The status of the capability. | [optional] [readonly] 
**supportedPerDatabaseMinDtus** | [**[ElasticPoolPerDatabaseMinDtuCapability]**](ElasticPoolPerDatabaseMinDtuCapability.md) | The list of supported min database DTUs. | [optional] [readonly] 



## Enum: StatusEnum


* `Visible` (value: `"Visible"`)

* `Available` (value: `"Available"`)

* `Default` (value: `"Default"`)

* `Disabled` (value: `"Disabled"`)




