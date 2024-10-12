# KustoManagementClient.DatabaseProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hotCachePeriodInDays** | **Number** | The number of days of data that should be kept in cache for fast queries. | [optional] 
**provisioningState** | **String** | The provisioned state of the resource. | [optional] [readonly] 
**softDeletePeriodInDays** | **Number** | The number of days data should be kept before it stops being accessible to queries. | 
**statistics** | [**DatabaseStatistics**](DatabaseStatistics.md) |  | [optional] 



## Enum: ProvisioningStateEnum


* `Running` (value: `"Running"`)

* `Creating` (value: `"Creating"`)

* `Deleting` (value: `"Deleting"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)




