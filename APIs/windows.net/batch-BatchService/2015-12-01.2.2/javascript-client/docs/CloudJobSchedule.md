# BatchService.CloudJobSchedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creationTime** | **Date** | Gets or sets the creation time of the job schedule. | [optional] 
**displayName** | **String** | Gets or sets the display name for the schedule. | [optional] 
**eTag** | **String** | Gets or sets the ETag of the job schedule. | [optional] 
**executionInfo** | [**JobScheduleExecutionInformation**](JobScheduleExecutionInformation.md) |  | [optional] 
**id** | **String** | Gets or sets a string that uniquely identifies the schedule within the account. A GUID is recommended. | [optional] 
**jobSpecification** | [**JobSpecification**](JobSpecification.md) |  | [optional] 
**lastModified** | **Date** | Gets or sets the last modified time of the job schedule. | [optional] 
**metadata** | [**[MetadataItem]**](MetadataItem.md) | Gets or sets a list of name-value pairs associated with the schedule as metadata. | [optional] 
**previousState** | **String** | Gets or sets the previous state of the job schedule. | [optional] 
**previousStateTransitionTime** | **Date** | Gets or sets the time at which the job schedule entered its previous state. | [optional] 
**schedule** | [**Schedule**](Schedule.md) |  | [optional] 
**state** | **String** | Gets or sets the current state of the job schedule. | [optional] 
**stateTransitionTime** | **Date** | Gets or sets the time at which the job schedule entered the current state. | [optional] 
**stats** | [**JobScheduleStatistics**](JobScheduleStatistics.md) |  | [optional] 
**url** | **String** | Gets or sets the URL of the job schedule. | [optional] 



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




