

# DscCompilationJobProperties

Definition of Dsc Compilation job properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_configuration** | [**DscConfigurationAssociationProperty**](DscConfigurationAssociationProperty.md) |  |  [optional] |
|**creationTime** | **OffsetDateTime** | Gets the creation time of the job. |  [optional] [readonly] |
|**endTime** | **OffsetDateTime** | Gets the end time of the job. |  [optional] [readonly] |
|**exception** | **String** | Gets the exception of the job. |  [optional] [readonly] |
|**jobId** | **UUID** | Gets the id of the job. |  [optional] [readonly] |
|**lastModifiedTime** | **OffsetDateTime** | Gets the last modified time of the job. |  [optional] [readonly] |
|**lastStatusModifiedTime** | **OffsetDateTime** | Gets the last status modified time of the job. |  [optional] [readonly] |
|**parameters** | **Map&lt;String, String&gt;** | Gets or sets the parameters of the job. |  [optional] |
|**provisioningState** | **JobProvisioningStateProperty** |  |  [optional] |
|**runOn** | **String** | Gets or sets the runOn which specifies the group name where the job is to be executed. |  [optional] |
|**startTime** | **OffsetDateTime** | Gets the start time of the job. |  [optional] [readonly] |
|**startedBy** | **String** | Gets the compilation job started by. |  [optional] [readonly] |
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



