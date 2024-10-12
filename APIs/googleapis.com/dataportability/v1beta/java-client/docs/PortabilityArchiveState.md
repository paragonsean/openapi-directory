

# PortabilityArchiveState

Resource that contains the state of an Archive job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The resource name of ArchiveJob&#39;s PortabilityArchiveState singleton. The format is: archiveJobs/{archive_job}/portabilityArchiveState. archive_job is the job ID provided in the request. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Resource that represents the state of the Archive job. |  [optional] |
|**urls** | **List&lt;String&gt;** | If the state is complete, this method returns the signed URLs of the objects in the Cloud Storage bucket. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| IN_PROGRESS | &quot;IN_PROGRESS&quot; |
| COMPLETE | &quot;COMPLETE&quot; |
| FAILED | &quot;FAILED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |



