# DataShareManagementClient.ScheduledTriggerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | Time at which the trigger was created. | [optional] [readonly] 
**provisioningState** | **String** | Gets the provisioning state | [optional] [readonly] 
**recurrenceInterval** | **String** | Recurrence Interval | 
**synchronizationMode** | **String** | Synchronization mode | [optional] 
**synchronizationTime** | **Date** | Synchronization time | 
**triggerStatus** | **String** | Gets the trigger state | [optional] [readonly] 
**userName** | **String** | Name of the user who created the trigger. | [optional] [readonly] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Creating` (value: `"Creating"`)

* `Deleting` (value: `"Deleting"`)

* `Moving` (value: `"Moving"`)

* `Failed` (value: `"Failed"`)





## Enum: RecurrenceIntervalEnum


* `Hour` (value: `"Hour"`)

* `Day` (value: `"Day"`)





## Enum: SynchronizationModeEnum


* `Incremental` (value: `"Incremental"`)

* `FullSync` (value: `"FullSync"`)





## Enum: TriggerStatusEnum


* `Active` (value: `"Active"`)

* `Inactive` (value: `"Inactive"`)

* `SourceSynchronizationSettingDeleted` (value: `"SourceSynchronizationSettingDeleted"`)




