

# ScheduledSynchronizationSettingProperties

A Scheduled synchronization setting data transfer object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | Time at which the synchronization setting was created. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Gets or sets the provisioning state |  [optional] [readonly] |
|**recurrenceInterval** | [**RecurrenceIntervalEnum**](#RecurrenceIntervalEnum) | Recurrence Interval |  |
|**synchronizationTime** | **OffsetDateTime** | Synchronization time |  |
|**userName** | **String** | Name of the user who created the synchronization setting. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| CREATING | &quot;Creating&quot; |
| DELETING | &quot;Deleting&quot; |
| MOVING | &quot;Moving&quot; |
| FAILED | &quot;Failed&quot; |



## Enum: RecurrenceIntervalEnum

| Name | Value |
|---- | -----|
| HOUR | &quot;Hour&quot; |
| DAY | &quot;Day&quot; |



