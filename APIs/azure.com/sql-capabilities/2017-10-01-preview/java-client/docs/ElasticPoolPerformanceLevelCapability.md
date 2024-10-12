

# ElasticPoolPerformanceLevelCapability

The Elastic Pool performance level capability.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**includedMaxSize** | [**MaxSizeCapability**](MaxSizeCapability.md) |  |  [optional] |
|**maxDatabaseCount** | **Integer** | The maximum number of databases supported. |  [optional] [readonly] |
|**performanceLevel** | [**PerformanceLevelCapability**](PerformanceLevelCapability.md) |  |  [optional] |
|**reason** | **String** | The reason for the capability not being available. |  [optional] |
|**sku** | [**ElasticPoolPerformanceLevelCapabilitySku**](ElasticPoolPerformanceLevelCapabilitySku.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the capability. |  [optional] [readonly] |
|**supportedLicenseTypes** | [**List&lt;LicenseTypeCapability&gt;**](LicenseTypeCapability.md) | List of supported license types. |  [optional] [readonly] |
|**supportedMaxSizes** | [**List&lt;MaxSizeRangeCapability&gt;**](MaxSizeRangeCapability.md) | The list of supported max sizes. |  [optional] [readonly] |
|**supportedPerDatabaseMaxPerformanceLevels** | [**List&lt;ElasticPoolPerDatabaseMaxPerformanceLevelCapability&gt;**](ElasticPoolPerDatabaseMaxPerformanceLevelCapability.md) | The list of supported per database max performance levels. |  [optional] [readonly] |
|**supportedPerDatabaseMaxSizes** | [**List&lt;MaxSizeRangeCapability&gt;**](MaxSizeRangeCapability.md) | The list of supported per database max sizes. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| VISIBLE | &quot;Visible&quot; |
| AVAILABLE | &quot;Available&quot; |
| DEFAULT | &quot;Default&quot; |
| DISABLED | &quot;Disabled&quot; |



