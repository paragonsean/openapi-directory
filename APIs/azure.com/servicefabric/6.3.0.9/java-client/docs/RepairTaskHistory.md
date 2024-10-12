

# RepairTaskHistory

A record of the times when the repair task entered each state.  This type supports the Service Fabric platform; it is not meant to be used directly from your code.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**approvedUtcTimestamp** | **OffsetDateTime** | The time when the repair task entered the Approved state |  [optional] |
|**claimedUtcTimestamp** | **OffsetDateTime** | The time when the repair task entered the Claimed state. |  [optional] |
|**completedUtcTimestamp** | **OffsetDateTime** | The time when the repair task entered the Completed state |  [optional] |
|**createdUtcTimestamp** | **OffsetDateTime** | The time when the repair task entered the Created state. |  [optional] |
|**executingUtcTimestamp** | **OffsetDateTime** | The time when the repair task entered the Executing state |  [optional] |
|**preparingHealthCheckEndUtcTimestamp** | **OffsetDateTime** | The time when the repair task completed the health check in the Preparing state. |  [optional] |
|**preparingHealthCheckStartUtcTimestamp** | **OffsetDateTime** | The time when the repair task started the health check in the Preparing state. |  [optional] |
|**preparingUtcTimestamp** | **OffsetDateTime** | The time when the repair task entered the Preparing state. |  [optional] |
|**restoringHealthCheckEndUtcTimestamp** | **OffsetDateTime** | The time when the repair task completed the health check in the Restoring state. |  [optional] |
|**restoringHealthCheckStartUtcTimestamp** | **OffsetDateTime** | The time when the repair task started the health check in the Restoring state. |  [optional] |
|**restoringUtcTimestamp** | **OffsetDateTime** | The time when the repair task entered the Restoring state |  [optional] |



