# KustoManagementClient.ReadOnlyFollowingDatabaseProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachedDatabaseConfigurationName** | **String** | The name of the attached database configuration cluster | [optional] [readonly] 
**hotCachePeriod** | **String** | The time the data should be kept in cache for fast queries in TimeSpan. | [optional] 
**leaderClusterResourceId** | **String** | The name of the leader cluster | [optional] [readonly] 
**principalsModificationKind** | **String** | The principals modification kind of the database | [optional] [readonly] 
**provisioningState** | **String** | The provisioned state of the resource. | [optional] [readonly] 
**softDeletePeriod** | **String** | The time the data should be kept before it stops being accessible to queries in TimeSpan. | [optional] [readonly] 
**statistics** | [**DatabaseStatistics**](DatabaseStatistics.md) |  | [optional] 



## Enum: PrincipalsModificationKindEnum


* `Union` (value: `"Union"`)

* `Replace` (value: `"Replace"`)

* `None` (value: `"None"`)





## Enum: ProvisioningStateEnum


* `Running` (value: `"Running"`)

* `Creating` (value: `"Creating"`)

* `Deleting` (value: `"Deleting"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Moving` (value: `"Moving"`)




