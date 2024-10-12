

# ServiceObjectiveCapability

The service objectives capability.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**computeModel** | **String** | The compute model |  [optional] [readonly] |
|**id** | **UUID** | The unique ID of the service objective. |  [optional] [readonly] |
|**includedMaxSize** | [**MaxSizeCapability**](MaxSizeCapability.md) |  |  [optional] |
|**name** | **String** | The service objective name. |  [optional] [readonly] |
|**performanceLevel** | [**PerformanceLevelCapability**](PerformanceLevelCapability.md) |  |  [optional] |
|**reason** | **String** | The reason for the capability not being available. |  [optional] |
|**sku** | [**ElasticPoolPerformanceLevelCapabilitySku**](ElasticPoolPerformanceLevelCapabilitySku.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the capability. |  [optional] [readonly] |
|**supportedAutoPauseDelay** | [**AutoPauseDelayTimeRange**](AutoPauseDelayTimeRange.md) |  |  [optional] |
|**supportedLicenseTypes** | [**List&lt;LicenseTypeCapability&gt;**](LicenseTypeCapability.md) | List of supported license types. |  [optional] [readonly] |
|**supportedMaxSizes** | [**List&lt;MaxSizeRangeCapability&gt;**](MaxSizeRangeCapability.md) | The list of supported maximum database sizes. |  [optional] [readonly] |
|**supportedMinCapacities** | [**List&lt;MinCapacityCapability&gt;**](MinCapacityCapability.md) | List of supported min capacities |  [optional] [readonly] |
|**zoneRedundant** | **Boolean** | Whether or not zone redundancy is supported for the service objective. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| VISIBLE | &quot;Visible&quot; |
| AVAILABLE | &quot;Available&quot; |
| DEFAULT | &quot;Default&quot; |
| DISABLED | &quot;Disabled&quot; |



