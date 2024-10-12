# AzureSqlDatabaseCapabilities.ElasticPoolDtuCapability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**includedMaxSize** | [**MaxSizeCapability**](MaxSizeCapability.md) |  | [optional] 
**limit** | **Number** | The maximum size of the database (see &#39;unit&#39; for the units). | [optional] [readonly] 
**maxDatabaseCount** | **Number** | The maximum number of databases supported. | [optional] [readonly] 
**status** | [**CapabilityStatus**](CapabilityStatus.md) |  | [optional] 
**supportedMaxSizes** | [**[MaxSizeCapability]**](MaxSizeCapability.md) | The list of supported max sizes. | [optional] [readonly] 
**supportedPerDatabaseMaxDtus** | [**[ElasticPoolPerDatabaseMaxDtuCapability]**](ElasticPoolPerDatabaseMaxDtuCapability.md) | The list of supported max database DTUs. | [optional] [readonly] 
**supportedPerDatabaseMaxSizes** | [**[MaxSizeCapability]**](MaxSizeCapability.md) | The list of supported max database sizes. | [optional] [readonly] 


