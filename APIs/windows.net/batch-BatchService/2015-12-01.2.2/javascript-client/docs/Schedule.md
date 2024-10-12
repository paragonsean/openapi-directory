# BatchService.Schedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doNotRunAfter** | **Date** | Gets or sets a time after which no job will be created under this job schedule.  The schedule will move to the completed state as soon as this deadline is past and there is no active job under this job schedule. | [optional] 
**doNotRunUntil** | **Date** | Gets or sets the earliest time at which any job may be created under this job schedule. If you do not specify a doNotRunUntil time, the schedule becomes ready to create jobs immediately. | [optional] 
**recurrenceInterval** | **String** | Gets or sets the time interval between the start times of two successive jobs under the job schedule. A job schedule can have at most one active job under it at any given time. | [optional] 
**startWindow** | **String** | Gets or sets the time interval, starting from the time at which the schedule indicates a job should be created, within which a job must be created.  If a job is not created within the startWindow interval, then the &#39;opportunity&#39; is lost; no job will be created until the next recurrence of the schedule. | [optional] 


