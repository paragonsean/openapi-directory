# ServiceFabricClientApis.RepairTask

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | The requested repair action. Must be specified when the repair task is created, and is immutable once set.  | 
**description** | **String** | A description of the purpose of the repair task, or other informational details. May be set when the repair task is created, and is immutable once set.  | [optional] 
**executor** | **String** | The name of the repair executor. Must be specified in Claimed and later states, and is immutable once set. | [optional] 
**executorData** | **String** | A data string that the repair executor can use to store its internal state. | [optional] 
**flags** | **Number** | A bitwise-OR of the following values, which gives additional details about the status of the repair task. - 1 - Cancellation of the repair has been requested - 2 - Abort of the repair has been requested - 4 - Approval of the repair was forced via client request  | [optional] 
**history** | [**RepairTaskHistory**](RepairTaskHistory.md) |  | [optional] 
**impact** | [**RepairImpactDescriptionBase**](RepairImpactDescriptionBase.md) |  | [optional] 
**performPreparingHealthCheck** | **Boolean** | A value to determine if health checks will be performed when the repair task enters the Preparing state. | [optional] 
**performRestoringHealthCheck** | **Boolean** | A value to determine if health checks will be performed when the repair task enters the Restoring state. | [optional] 
**preparingHealthCheckState** | [**RepairTaskHealthCheckState**](RepairTaskHealthCheckState.md) |  | [optional] 
**restoringHealthCheckState** | [**RepairTaskHealthCheckState**](RepairTaskHealthCheckState.md) |  | [optional] 
**resultCode** | **Number** | A numeric value providing additional details about the result of the repair task execution. May be specified in the Restoring and later states, and is immutable once set.  | [optional] 
**resultDetails** | **String** | A string providing additional details about the result of the repair task execution. May be specified in the Restoring and later states, and is immutable once set.  | [optional] 
**resultStatus** | **String** | A value describing the overall result of the repair task execution. Must be specified in the Restoring and later states, and is immutable once set.  - Invalid - Indicates that the repair task result is invalid. All Service Fabric enumerations have the invalid value. - Succeeded - Indicates that the repair task completed execution successfully. - Cancelled - Indicates that the repair task was cancelled prior to execution. - Interrupted - Indicates that execution of the repair task was interrupted by a cancellation request after some work had already been performed. - Failed - Indicates that there was a failure during execution of the repair task. Some work may have been performed. - Pending - Indicates that the repair task result is not yet available, because the repair task has not finished executing.  | [optional] 
**state** | **String** | The workflow state of the repair task. Valid initial states are Created, Claimed, and Preparing.  - Invalid - Indicates that the repair task state is invalid. All Service Fabric enumerations have the invalid value. - Created - Indicates that the repair task has been created. - Claimed - Indicates that the repair task has been claimed by a repair executor. - Preparing - Indicates that the Repair Manager is preparing the system to handle the impact of the repair task, usually by taking resources offline gracefully. - Approved - Indicates that the repair task has been approved by the Repair Manager and is safe to execute. - Executing - Indicates that execution of the repair task is in progress. - Restoring - Indicates that the Repair Manager is restoring the system to its pre-repair state, usually by bringing resources back online. - Completed - Indicates that the repair task has completed, and no further state changes will occur.  | 
**target** | [**RepairTargetDescriptionBase**](RepairTargetDescriptionBase.md) |  | [optional] 
**taskId** | **String** | The ID of the repair task. | 
**version** | **String** | The version of the repair task. When creating a new repair task, the version must be set to zero.  When updating a repair task,  the version is used for optimistic concurrency checks.  If the version is  set to zero, the update will not check for write conflicts.  If the version is set to a non-zero value, then the  update will only succeed if the actual current version of the repair task matches this value.  | [optional] 



## Enum: ResultStatusEnum


* `Invalid` (value: `"Invalid"`)

* `Succeeded` (value: `"Succeeded"`)

* `Cancelled` (value: `"Cancelled"`)

* `Interrupted` (value: `"Interrupted"`)

* `Failed` (value: `"Failed"`)

* `Pending` (value: `"Pending"`)





## Enum: StateEnum


* `Invalid` (value: `"Invalid"`)

* `Created` (value: `"Created"`)

* `Claimed` (value: `"Claimed"`)

* `Preparing` (value: `"Preparing"`)

* `Approved` (value: `"Approved"`)

* `Executing` (value: `"Executing"`)

* `Restoring` (value: `"Restoring"`)

* `Completed` (value: `"Completed"`)




