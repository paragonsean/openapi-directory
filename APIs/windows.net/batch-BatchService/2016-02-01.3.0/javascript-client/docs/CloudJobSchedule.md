# BatchService.CloudJobSchedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creationTime** | **Date** | The creation time of the job schedule. | [optional] 
**displayName** | **String** | The display name for the schedule. | [optional] 
**eTag** | **String** | The ETag of the job schedule. | [optional] 
**executionInfo** | [**JobScheduleExecutionInformation**](JobScheduleExecutionInformation.md) |  | [optional] 
**id** | **String** | A string that uniquely identifies the schedule within the account. A GUID is recommended. | [optional] 
**jobSpecification** | [**JobSpecification**](JobSpecification.md) |  | [optional] 
**lastModified** | **Date** | The last modified time of the job schedule. | [optional] 
**metadata** | [**[MetadataItem]**](MetadataItem.md) | A list of name-value pairs associated with the schedule as metadata. | [optional] 
**previousState** | **String** | The previous state of the job schedule. | [optional] 
**previousStateTransitionTime** | **Date** | The time at which the job schedule entered its previous state. | [optional] 
**schedule** | [**Schedule**](Schedule.md) |  | [optional] 
**state** | **String** | The current state of the job schedule. | [optional] 
**stateTransitionTime** | **Date** | The time at which the job schedule entered the current state. | [optional] 
**stats** | [**JobScheduleStatistics**](JobScheduleStatistics.md) |  | [optional] 
**url** | **String** | The URL of the job schedule. | [optional] 



## Enum: PreviousStateEnum


* `active` (value: `"active"`)

* `completed` (value: `"completed"`)

* `disabled` (value: `"disabled"`)

* `terminating` (value: `"terminating"`)

* `deleting` (value: `"deleting"`)





## Enum: StateEnum


* `active` (value: `"active"`)

* `completed` (value: `"completed"`)

* `disabled` (value: `"disabled"`)

* `terminating` (value: `"terminating"`)

* `deleting` (value: `"deleting"`)




