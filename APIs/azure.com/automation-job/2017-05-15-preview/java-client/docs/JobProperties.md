

# JobProperties

Definition of job properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationTime** | **OffsetDateTime** | Gets or sets the creation time of the job. |  [optional] |
|**endTime** | **OffsetDateTime** | Gets or sets the end time of the job. |  [optional] |
|**exception** | **String** | Gets or sets the exception of the job. |  [optional] |
|**jobId** | **UUID** | Gets or sets the id of the job. |  [optional] |
|**lastModifiedTime** | **OffsetDateTime** | Gets or sets the last modified time of the job. |  [optional] |
|**lastStatusModifiedTime** | **OffsetDateTime** | Gets or sets the last status modified time of the job. |  [optional] |
|**parameters** | **Map&lt;String, String&gt;** | Gets or sets the parameters of the job. |  [optional] |
|**provisioningState** | **JobProvisioningStateProperty** |  |  [optional] |
|**runOn** | **String** | Gets or sets the runOn which specifies the group name where the job is to be executed. |  [optional] |
|**runbook** | [**RunbookAssociationProperty**](RunbookAssociationProperty.md) |  |  [optional] |
|**startTime** | **OffsetDateTime** | Gets or sets the start time of the job. |  [optional] |
|**startedBy** | **String** | Gets or sets the job started by. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Gets or sets the status of the job. |  [optional] |
|**statusDetails** | **String** | Gets or sets the status details of the job. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NEW | &quot;New&quot; |
| ACTIVATING | &quot;Activating&quot; |
| RUNNING | &quot;Running&quot; |
| COMPLETED | &quot;Completed&quot; |
| FAILED | &quot;Failed&quot; |
| STOPPED | &quot;Stopped&quot; |
| BLOCKED | &quot;Blocked&quot; |
| SUSPENDED | &quot;Suspended&quot; |
| DISCONNECTED | &quot;Disconnected&quot; |
| SUSPENDING | &quot;Suspending&quot; |
| STOPPING | &quot;Stopping&quot; |
| RESUMING | &quot;Resuming&quot; |
| REMOVING | &quot;Removing&quot; |



