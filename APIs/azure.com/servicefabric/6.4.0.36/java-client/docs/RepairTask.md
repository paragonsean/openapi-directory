

# RepairTask

Represents a repair task, which includes information about what kind of repair was requested, what its progress is, and what its final result was.  This type supports the Service Fabric platform; it is not meant to be used directly from your code.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | **String** | The requested repair action. Must be specified when the repair task is created, and is immutable once set. |  |
|**description** | **String** | A description of the purpose of the repair task, or other informational details. May be set when the repair task is created, and is immutable once set. |  [optional] |
|**executor** | **String** | The name of the repair executor. Must be specified in Claimed and later states, and is immutable once set. |  [optional] |
|**executorData** | **String** | A data string that the repair executor can use to store its internal state. |  [optional] |
|**flags** | **Integer** | A bitwise-OR of the following values, which gives additional details about the status of the repair task. - 1 - Cancellation of the repair has been requested - 2 - Abort of the repair has been requested - 4 - Approval of the repair was forced via client request |  [optional] |
|**history** | [**RepairTaskHistory**](RepairTaskHistory.md) |  |  [optional] |
|**impact** | [**RepairImpactDescriptionBase**](RepairImpactDescriptionBase.md) |  |  [optional] |
|**performPreparingHealthCheck** | **Boolean** | A value to determine if health checks will be performed when the repair task enters the Preparing state. |  [optional] |
|**performRestoringHealthCheck** | **Boolean** | A value to determine if health checks will be performed when the repair task enters the Restoring state. |  [optional] |
|**preparingHealthCheckState** | **RepairTaskHealthCheckState** |  |  [optional] |
|**restoringHealthCheckState** | **RepairTaskHealthCheckState** |  |  [optional] |
|**resultCode** | **Integer** | A numeric value providing additional details about the result of the repair task execution. May be specified in the Restoring and later states, and is immutable once set. |  [optional] |
|**resultDetails** | **String** | A string providing additional details about the result of the repair task execution. May be specified in the Restoring and later states, and is immutable once set. |  [optional] |
|**resultStatus** | [**ResultStatusEnum**](#ResultStatusEnum) | A value describing the overall result of the repair task execution. Must be specified in the Restoring and later states, and is immutable once set. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The workflow state of the repair task. Valid initial states are Created, Claimed, and Preparing. |  |
|**target** | [**RepairTargetDescriptionBase**](RepairTargetDescriptionBase.md) |  |  [optional] |
|**taskId** | **String** | The ID of the repair task. |  |
|**version** | **String** | The version of the repair task. When creating a new repair task, the version must be set to zero.  When updating a repair task, the version is used for optimistic concurrency checks.  If the version is set to zero, the update will not check for write conflicts.  If the version is set to a non-zero value, then the update will only succeed if the actual current version of the repair task matches this value. |  [optional] |



## Enum: ResultStatusEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| INTERRUPTED | &quot;Interrupted&quot; |
| FAILED | &quot;Failed&quot; |
| PENDING | &quot;Pending&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| CREATED | &quot;Created&quot; |
| CLAIMED | &quot;Claimed&quot; |
| PREPARING | &quot;Preparing&quot; |
| APPROVED | &quot;Approved&quot; |
| EXECUTING | &quot;Executing&quot; |
| RESTORING | &quot;Restoring&quot; |
| COMPLETED | &quot;Completed&quot; |



