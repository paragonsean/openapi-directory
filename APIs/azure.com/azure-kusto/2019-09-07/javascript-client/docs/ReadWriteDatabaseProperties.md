# KustoManagementClient.ReadWriteDatabaseProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hotCachePeriod** | **String** | The time the data should be kept in cache for fast queries in TimeSpan. | [optional] 
**provisioningState** | **String** | The provisioned state of the resource. | [optional] [readonly] 
**softDeletePeriod** | **String** | The time the data should be kept before it stops being accessible to queries in TimeSpan. | [optional] 
**statistics** | [**DatabaseStatistics**](DatabaseStatistics.md) |  | [optional] 



## Enum: ProvisioningStateEnum


* `Running` (value: `"Running"`)

* `Creating` (value: `"Creating"`)

* `Deleting` (value: `"Deleting"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Moving` (value: `"Moving"`)




