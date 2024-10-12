

# ReadWriteDatabaseProperties

Class representing the Kusto database properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hotCachePeriod** | **String** | The time the data should be kept in cache for fast queries in TimeSpan. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioned state of the resource. |  [optional] [readonly] |
|**softDeletePeriod** | **String** | The time the data should be kept before it stops being accessible to queries in TimeSpan. |  [optional] |
|**statistics** | [**DatabaseStatistics**](DatabaseStatistics.md) |  |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| RUNNING | &quot;Running&quot; |
| CREATING | &quot;Creating&quot; |
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| MOVING | &quot;Moving&quot; |



