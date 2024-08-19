

# DatabaseProperties

Class representing the Kusto database properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hotCachePeriodInDays** | **Integer** | The number of days of data that should be kept in cache for fast queries. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioned state of the resource. |  [optional] [readonly] |
|**softDeletePeriodInDays** | **Integer** | The number of days data should be kept before it stops being accessible to queries. |  |
|**statistics** | [**DatabaseStatistics**](DatabaseStatistics.md) |  |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| RUNNING | &quot;Running&quot; |
| CREATING | &quot;Creating&quot; |
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |



