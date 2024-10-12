

# ScheduledTriggerProperties

A Scheduled trigger data transfer object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | Time at which the trigger was created. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Gets the provisioning state |  [optional] [readonly] |
|**recurrenceInterval** | [**RecurrenceIntervalEnum**](#RecurrenceIntervalEnum) | Recurrence Interval |  |
|**synchronizationMode** | [**SynchronizationModeEnum**](#SynchronizationModeEnum) | Synchronization mode |  [optional] |
|**synchronizationTime** | **OffsetDateTime** | Synchronization time |  |
|**triggerStatus** | [**TriggerStatusEnum**](#TriggerStatusEnum) | Gets the trigger state |  [optional] [readonly] |
|**userName** | **String** | Name of the user who created the trigger. |  [optional] [readonly] |



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



## Enum: SynchronizationModeEnum

| Name | Value |
|---- | -----|
| INCREMENTAL | &quot;Incremental&quot; |
| FULL_SYNC | &quot;FullSync&quot; |



## Enum: TriggerStatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| INACTIVE | &quot;Inactive&quot; |
| SOURCE_SYNCHRONIZATION_SETTING_DELETED | &quot;SourceSynchronizationSettingDeleted&quot; |



