# BatchService.CloudJobSchedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creationTime** | **Date** |  | [optional] 
**displayName** | **String** |  | [optional] 
**eTag** | **String** | This is an opaque string. You can use it to detect whether the job schedule has changed between requests. In particular, you can be pass the ETag with an Update Job Schedule request to specify that your changes should take effect only if nobody else has modified the schedule in the meantime. | [optional] 
**executionInfo** | [**JobScheduleExecutionInformation**](JobScheduleExecutionInformation.md) |  | [optional] 
**id** | **String** | It is common to use a GUID for the id. | [optional] 
**jobSpecification** | [**JobSpecification**](JobSpecification.md) |  | [optional] 
**lastModified** | **Date** | This is the last time at which the schedule level data, such as the job specification or recurrence information, changed. It does not factor in job-level changes such as new jobs being created or jobs changing state. | [optional] 
**metadata** | [**[MetadataItem]**](MetadataItem.md) | The Batch service does not assign any meaning to metadata; it is solely for the use of user code. | [optional] 
**previousState** | [**JobScheduleState**](JobScheduleState.md) |  | [optional] 
**previousStateTransitionTime** | **Date** | This property is not present if the job schedule is in its initial active state. | [optional] 
**schedule** | [**Schedule**](Schedule.md) |  | [optional] 
**state** | [**JobScheduleState**](JobScheduleState.md) |  | [optional] 
**stateTransitionTime** | **Date** |  | [optional] 
**stats** | [**JobScheduleStatistics**](JobScheduleStatistics.md) |  | [optional] 
**url** | **String** |  | [optional] 


