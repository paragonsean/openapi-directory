# TimeSeriesInsightsClient.EnvironmentResourceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataAccessFqdn** | **String** | The fully qualified domain name used to access the environment data, e.g. to query the environment&#39;s events or upload reference data for the environment. | [optional] [readonly] 
**dataAccessId** | **String** | An id used to access the environment data, e.g. to query the environment&#39;s events or upload reference data for the environment. | [optional] [readonly] 
**dataRetentionTime** | **String** | ISO8601 timespan specifying the minimum number of days the environment&#39;s events will be available for query. | 
**storageLimitExceededBehavior** | **String** | The behavior the Time Series Insights service should take when the environment&#39;s capacity has been exceeded. If \&quot;PauseIngress\&quot; is specified, new events will not be read from the event source. If \&quot;PurgeOldData\&quot; is specified, new events will continue to be read and old events will be deleted from the environment. The default behavior is PurgeOldData. | [optional] 
**creationTime** | **Date** | The time the resource was created. | [optional] [readonly] 
**provisioningState** | **String** | Provisioning state of the resource. | [optional] [readonly] 



## Enum: StorageLimitExceededBehaviorEnum


* `PurgeOldData` (value: `"PurgeOldData"`)

* `PauseIngress` (value: `"PauseIngress"`)





## Enum: ProvisioningStateEnum


* `Accepted` (value: `"Accepted"`)

* `Creating` (value: `"Creating"`)

* `Updating` (value: `"Updating"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Deleting` (value: `"Deleting"`)




