

# EnvironmentResourceProperties

Properties of the environment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataAccessFqdn** | **String** | The fully qualified domain name used to access the environment data, e.g. to query the environment&#39;s events or upload reference data for the environment. |  [optional] [readonly] |
|**dataAccessId** | **UUID** | An id used to access the environment data, e.g. to query the environment&#39;s events or upload reference data for the environment. |  [optional] [readonly] |
|**dataRetentionTime** | **String** | ISO8601 timespan specifying the minimum number of days the environment&#39;s events will be available for query. |  |
|**storageLimitExceededBehavior** | [**StorageLimitExceededBehaviorEnum**](#StorageLimitExceededBehaviorEnum) | The behavior the Time Series Insights service should take when the environment&#39;s capacity has been exceeded. If \&quot;PauseIngress\&quot; is specified, new events will not be read from the event source. If \&quot;PurgeOldData\&quot; is specified, new events will continue to be read and old events will be deleted from the environment. The default behavior is PurgeOldData. |  [optional] |
|**creationTime** | **OffsetDateTime** | The time the resource was created. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Provisioning state of the resource. |  [optional] [readonly] |



## Enum: StorageLimitExceededBehaviorEnum

| Name | Value |
|---- | -----|
| PURGE_OLD_DATA | &quot;PurgeOldData&quot; |
| PAUSE_INGRESS | &quot;PauseIngress&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| ACCEPTED | &quot;Accepted&quot; |
| CREATING | &quot;Creating&quot; |
| UPDATING | &quot;Updating&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| DELETING | &quot;Deleting&quot; |



