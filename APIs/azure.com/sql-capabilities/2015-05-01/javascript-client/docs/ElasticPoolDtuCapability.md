# SqlManagementClient.ElasticPoolDtuCapability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**includedMaxSize** | [**MaxSizeCapability**](MaxSizeCapability.md) |  | [optional] 
**limit** | **Number** | The DTU limit for the pool. | [optional] [readonly] 
**maxDatabaseCount** | **Number** | The maximum number of databases supported. | [optional] [readonly] 
**reason** | **String** | The reason for the capability not being available. | [optional] 
**status** | **String** | The status of the capability. | [optional] [readonly] 
**supportedMaxSizes** | [**[MaxSizeCapability]**](MaxSizeCapability.md) | The list of supported max sizes. | [optional] [readonly] 
**supportedPerDatabaseMaxDtus** | [**[ElasticPoolPerDatabaseMaxDtuCapability]**](ElasticPoolPerDatabaseMaxDtuCapability.md) | The list of supported per database max DTUs. | [optional] [readonly] 
**supportedPerDatabaseMaxSizes** | [**[MaxSizeCapability]**](MaxSizeCapability.md) | The list of supported per database max sizes. | [optional] [readonly] 



## Enum: StatusEnum


* `Visible` (value: `"Visible"`)

* `Available` (value: `"Available"`)

* `Default` (value: `"Default"`)

* `Disabled` (value: `"Disabled"`)




