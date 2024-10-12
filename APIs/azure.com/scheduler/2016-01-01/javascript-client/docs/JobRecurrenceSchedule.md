# SchedulerManagementClient.JobRecurrenceSchedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hours** | **[Number]** | Gets or sets the hours of the day that the job should execute at. | [optional] 
**minutes** | **[Number]** | Gets or sets the minutes of the hour that the job should execute at. | [optional] 
**monthDays** | **[Number]** | Gets or sets the days of the month that the job should execute on. Must be between 1 and 31. | [optional] 
**monthlyOccurrences** | [**[JobRecurrenceScheduleMonthlyOccurrence]**](JobRecurrenceScheduleMonthlyOccurrence.md) | Gets or sets the occurrences of days within a month. | [optional] 
**weekDays** | **[String]** | Gets or sets the days of the week that the job should execute on. | [optional] 



## Enum: [WeekDaysEnum]


* `Sunday` (value: `"Sunday"`)

* `Monday` (value: `"Monday"`)

* `Tuesday` (value: `"Tuesday"`)

* `Wednesday` (value: `"Wednesday"`)

* `Thursday` (value: `"Thursday"`)

* `Friday` (value: `"Friday"`)

* `Saturday` (value: `"Saturday"`)




