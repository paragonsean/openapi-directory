

# JobCollectionItemProperties

Job collection item properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationTime** | **OffsetDateTime** | The creation time of the job. |  [optional] [readonly] |
|**endTime** | **OffsetDateTime** | The end time of the job. |  [optional] [readonly] |
|**jobId** | **UUID** | The id of the job. |  [optional] [readonly] |
|**lastModifiedTime** | **OffsetDateTime** | The last modified time of the job. |  [optional] [readonly] |
|**provisioningState** | **String** | The provisioning state of a resource. |  [optional] [readonly] |
|**runOn** | **String** | Specifies the runOn group name where the job was executed. |  [optional] |
|**runbook** | [**RunbookAssociationProperty**](RunbookAssociationProperty.md) |  |  [optional] |
|**startTime** | **OffsetDateTime** | The start time of the job. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the job. |  [optional] [readonly] |



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



