

# StandardEnvironmentResourceProperties

Properties of the standard environment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataRetentionTime** | **String** | ISO8601 timespan specifying the minimum number of days the environment&#39;s events will be available for query. |  |
|**partitionKeyProperties** | [**List&lt;TimeSeriesIdProperty&gt;**](TimeSeriesIdProperty.md) | The list of event properties which will be used to partition data in the environment. |  [optional] |
|**storageLimitExceededBehavior** | [**StorageLimitExceededBehaviorEnum**](#StorageLimitExceededBehaviorEnum) | The behavior the Time Series Insights service should take when the environment&#39;s capacity has been exceeded. If \&quot;PauseIngress\&quot; is specified, new events will not be read from the event source. If \&quot;PurgeOldData\&quot; is specified, new events will continue to be read and old events will be deleted from the environment. The default behavior is PurgeOldData. |  [optional] |
|**dataAccessFqdn** | **String** | The fully qualified domain name used to access the environment data, e.g. to query the environment&#39;s events or upload reference data for the environment. |  [optional] [readonly] |
|**dataAccessId** | **UUID** | An id used to access the environment data, e.g. to query the environment&#39;s events or upload reference data for the environment. |  [optional] [readonly] |
|**status** | [**EnvironmentStatus**](EnvironmentStatus.md) |  |  [optional] |
|**creationTime** | **OffsetDateTime** | The time the resource was created. |  [optional] [readonly] |
|**provisioningState** | **ProvisioningState** |  |  [optional] |



## Enum: StorageLimitExceededBehaviorEnum

| Name | Value |
|---- | -----|
| PURGE_OLD_DATA | &quot;PurgeOldData&quot; |
| PAUSE_INGRESS | &quot;PauseIngress&quot; |



