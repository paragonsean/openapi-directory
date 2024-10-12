

# ShareSynchronization

A ShareSynchronization data transfer object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consumerEmail** | **String** | Email of the user who created the synchronization |  [optional] |
|**consumerName** | **String** | Name of the user who created the synchronization |  [optional] |
|**consumerTenantName** | **String** | Tenant name of the consumer who created the synchronization |  [optional] |
|**durationMs** | **Integer** | synchronization duration |  [optional] |
|**endTime** | **OffsetDateTime** | End time of synchronization |  [optional] |
|**message** | **String** | message of synchronization |  [optional] |
|**startTime** | **OffsetDateTime** | start time of synchronization |  [optional] |
|**status** | **String** | Raw Status |  [optional] |
|**synchronizationId** | **String** | Synchronization id |  [optional] |
|**synchronizationMode** | [**SynchronizationModeEnum**](#SynchronizationModeEnum) | Synchronization mode |  [optional] [readonly] |



## Enum: SynchronizationModeEnum

| Name | Value |
|---- | -----|
| INCREMENTAL | &quot;Incremental&quot; |
| FULL_SYNC | &quot;FullSync&quot; |



