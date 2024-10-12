

# ShareSubscriptionSynchronization

A ShareSubscriptionSynchronization data transfer object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**durationMs** | **Integer** | Synchronization duration |  [optional] [readonly] |
|**endTime** | **OffsetDateTime** | End time of synchronization |  [optional] [readonly] |
|**message** | **String** | message of Synchronization |  [optional] [readonly] |
|**startTime** | **OffsetDateTime** | start time of synchronization |  [optional] [readonly] |
|**status** | **String** | Raw Status |  [optional] [readonly] |
|**synchronizationId** | **String** | Synchronization id |  |
|**synchronizationMode** | [**SynchronizationModeEnum**](#SynchronizationModeEnum) | Synchronization Mode |  [optional] [readonly] |



## Enum: SynchronizationModeEnum

| Name | Value |
|---- | -----|
| INCREMENTAL | &quot;Incremental&quot; |
| FULL_SYNC | &quot;FullSync&quot; |



