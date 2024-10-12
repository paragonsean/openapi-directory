# SqlManagementClient.ElasticPoolPerformanceLevelCapability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**includedMaxSize** | [**MaxSizeCapability**](MaxSizeCapability.md) |  | [optional] 
**maxDatabaseCount** | **Number** | The maximum number of databases supported. | [optional] [readonly] 
**performanceLevel** | [**PerformanceLevelCapability**](PerformanceLevelCapability.md) |  | [optional] 
**reason** | **String** | The reason for the capability not being available. | [optional] 
**sku** | [**ElasticPoolPerformanceLevelCapabilitySku**](ElasticPoolPerformanceLevelCapabilitySku.md) |  | [optional] 
**status** | **String** | The status of the capability. | [optional] [readonly] 
**supportedLicenseTypes** | [**[LicenseTypeCapability]**](LicenseTypeCapability.md) | List of supported license types. | [optional] [readonly] 
**supportedMaxSizes** | [**[MaxSizeRangeCapability]**](MaxSizeRangeCapability.md) | The list of supported max sizes. | [optional] [readonly] 
**supportedPerDatabaseMaxPerformanceLevels** | [**[ElasticPoolPerDatabaseMaxPerformanceLevelCapability]**](ElasticPoolPerDatabaseMaxPerformanceLevelCapability.md) | The list of supported per database max performance levels. | [optional] [readonly] 
**supportedPerDatabaseMaxSizes** | [**[MaxSizeRangeCapability]**](MaxSizeRangeCapability.md) | The list of supported per database max sizes. | [optional] [readonly] 



## Enum: StatusEnum


* `Visible` (value: `"Visible"`)

* `Available` (value: `"Available"`)

* `Default` (value: `"Default"`)

* `Disabled` (value: `"Disabled"`)




