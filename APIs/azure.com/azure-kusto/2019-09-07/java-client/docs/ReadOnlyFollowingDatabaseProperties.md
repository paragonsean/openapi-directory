

# ReadOnlyFollowingDatabaseProperties

Class representing the Kusto database properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attachedDatabaseConfigurationName** | **String** | The name of the attached database configuration cluster |  [optional] [readonly] |
|**hotCachePeriod** | **String** | The time the data should be kept in cache for fast queries in TimeSpan. |  [optional] |
|**leaderClusterResourceId** | **String** | The name of the leader cluster |  [optional] [readonly] |
|**principalsModificationKind** | [**PrincipalsModificationKindEnum**](#PrincipalsModificationKindEnum) | The principals modification kind of the database |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioned state of the resource. |  [optional] [readonly] |
|**softDeletePeriod** | **String** | The time the data should be kept before it stops being accessible to queries in TimeSpan. |  [optional] [readonly] |
|**statistics** | [**DatabaseStatistics**](DatabaseStatistics.md) |  |  [optional] |



## Enum: PrincipalsModificationKindEnum

| Name | Value |
|---- | -----|
| UNION | &quot;Union&quot; |
| REPLACE | &quot;Replace&quot; |
| NONE | &quot;None&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| RUNNING | &quot;Running&quot; |
| CREATING | &quot;Creating&quot; |
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| MOVING | &quot;Moving&quot; |



