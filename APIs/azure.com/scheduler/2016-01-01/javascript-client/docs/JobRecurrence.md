# SchedulerManagementClient.JobRecurrence

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **Number** | Gets or sets the maximum number of times that the job should run. | [optional] 
**endTime** | **Date** | Gets or sets the time at which the job will complete. | [optional] 
**frequency** | **String** | Gets or sets the frequency of recurrence (second, minute, hour, day, week, month). | [optional] 
**interval** | **Number** | Gets or sets the interval between retries. | [optional] 
**schedule** | [**JobRecurrenceSchedule**](JobRecurrenceSchedule.md) |  | [optional] 



## Enum: FrequencyEnum


* `Minute` (value: `"Minute"`)

* `Hour` (value: `"Hour"`)

* `Day` (value: `"Day"`)

* `Week` (value: `"Week"`)

* `Month` (value: `"Month"`)




