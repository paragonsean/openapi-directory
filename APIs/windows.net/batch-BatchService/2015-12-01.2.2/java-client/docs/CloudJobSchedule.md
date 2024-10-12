

# CloudJobSchedule

A job schedule that allows recurring jobs by specifying when to run jobs and a specification used to create each job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationTime** | **OffsetDateTime** | Gets or sets the creation time of the job schedule. |  [optional] |
|**displayName** | **String** | Gets or sets the display name for the schedule. |  [optional] |
|**eTag** | **String** | Gets or sets the ETag of the job schedule. |  [optional] |
|**executionInfo** | [**JobScheduleExecutionInformation**](JobScheduleExecutionInformation.md) |  |  [optional] |
|**id** | **String** | Gets or sets a string that uniquely identifies the schedule within the account. A GUID is recommended. |  [optional] |
|**jobSpecification** | [**JobSpecification**](JobSpecification.md) |  |  [optional] |
|**lastModified** | **OffsetDateTime** | Gets or sets the last modified time of the job schedule. |  [optional] |
|**metadata** | [**List&lt;MetadataItem&gt;**](MetadataItem.md) | Gets or sets a list of name-value pairs associated with the schedule as metadata. |  [optional] |
|**previousState** | [**PreviousStateEnum**](#PreviousStateEnum) | Gets or sets the previous state of the job schedule. |  [optional] |
|**previousStateTransitionTime** | **OffsetDateTime** | Gets or sets the time at which the job schedule entered its previous state. |  [optional] |
|**schedule** | [**Schedule**](Schedule.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Gets or sets the current state of the job schedule. |  [optional] |
|**stateTransitionTime** | **OffsetDateTime** | Gets or sets the time at which the job schedule entered the current state. |  [optional] |
|**stats** | [**JobScheduleStatistics**](JobScheduleStatistics.md) |  |  [optional] |
|**url** | **String** | Gets or sets the URL of the job schedule. |  [optional] |



## Enum: PreviousStateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| COMPLETED | &quot;completed&quot; |
| DISABLED | &quot;disabled&quot; |
| TERMINATING | &quot;terminating&quot; |
| DELETING | &quot;deleting&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| COMPLETED | &quot;completed&quot; |
| DISABLED | &quot;disabled&quot; |
| TERMINATING | &quot;terminating&quot; |
| DELETING | &quot;deleting&quot; |



