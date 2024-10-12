# SchedulerManagementClient.JobStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**executionCount** | **Number** | Gets the number of times this job has executed. | [optional] [readonly] 
**failureCount** | **Number** | Gets the number of times this job has failed. | [optional] [readonly] 
**faultedCount** | **Number** | Gets the number of faulted occurrences (occurrences that were retried and failed as many times as the retry policy states). | [optional] [readonly] 
**lastExecutionTime** | **Date** | Gets the time the last occurrence executed in ISO-8601 format.  Could be empty if job has not run yet. | [optional] [readonly] 
**nextExecutionTime** | **Date** | Gets the time of the next occurrence in ISO-8601 format. Could be empty if the job is completed. | [optional] [readonly] 


