# TimeSeriesInsightsClient.EnvironmentCreationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataRetentionTime** | **String** | ISO8601 timespan specifying the minimum number of days the environment&#39;s events will be available for query. | 
**partitionKeyProperties** | [**[PartitionKeyProperty]**](PartitionKeyProperty.md) | The list of partition keys according to which the data in the environment will be ordered. | [optional] 
**storageLimitExceededBehavior** | **String** | The behavior the Time Series Insights service should take when the environment&#39;s capacity has been exceeded. If \&quot;PauseIngress\&quot; is specified, new events will not be read from the event source. If \&quot;PurgeOldData\&quot; is specified, new events will continue to be read and old events will be deleted from the environment. The default behavior is PurgeOldData. | [optional] 



## Enum: StorageLimitExceededBehaviorEnum


* `PurgeOldData` (value: `"PurgeOldData"`)

* `PauseIngress` (value: `"PauseIngress"`)




