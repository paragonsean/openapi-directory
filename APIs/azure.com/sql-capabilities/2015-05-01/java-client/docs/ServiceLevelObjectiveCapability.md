

# ServiceLevelObjectiveCapability

The service objectives capability.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** | The unique ID of the service objective. |  [optional] [readonly] |
|**includedMaxSize** | [**MaxSizeCapability**](MaxSizeCapability.md) |  |  [optional] |
|**name** | **String** | The service objective name. |  [optional] [readonly] |
|**performanceLevel** | [**PerformanceLevelCapability**](PerformanceLevelCapability.md) |  |  [optional] |
|**reason** | **String** | The reason for the capability not being available. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the capability. |  [optional] [readonly] |
|**supportedMaxSizes** | [**List&lt;MaxSizeCapability&gt;**](MaxSizeCapability.md) | The list of supported maximum database sizes for this service objective. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| VISIBLE | &quot;Visible&quot; |
| AVAILABLE | &quot;Available&quot; |
| DEFAULT | &quot;Default&quot; |
| DISABLED | &quot;Disabled&quot; |



