# UpdateManagement.ScheduleProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advancedSchedule** | [**AdvancedSchedule**](AdvancedSchedule.md) |  | [optional] 
**creationTime** | **Date** | Gets or sets the creation time. | [optional] 
**description** | **String** | Gets or sets the description. | [optional] 
**expiryTime** | **Date** | Gets or sets the end time of the schedule. | [optional] 
**expiryTimeOffsetMinutes** | **Number** | Gets or sets the expiry time&#39;s offset in minutes. | [optional] 
**frequency** | **String** | Gets or sets the frequency of the schedule. | [optional] 
**interval** | **Number** | Gets or sets the interval of the schedule. | [optional] 
**isEnabled** | **Boolean** | Gets or sets a value indicating whether this schedule is enabled. | [optional] [default to false]
**lastModifiedTime** | **Date** | Gets or sets the last modified time. | [optional] 
**nextRun** | **Date** | Gets or sets the next run time of the schedule. | [optional] 
**nextRunOffsetMinutes** | **Number** | Gets or sets the next run time&#39;s offset in minutes. | [optional] 
**startTime** | **Date** | Gets or sets the start time of the schedule. | [optional] 
**startTimeOffsetMinutes** | **Number** | Gets the start time&#39;s offset in minutes. | [optional] [readonly] 
**timeZone** | **String** | Gets or sets the time zone of the schedule. | [optional] 



## Enum: FrequencyEnum


* `OneTime` (value: `"OneTime"`)

* `Day` (value: `"Day"`)

* `Hour` (value: `"Hour"`)

* `Week` (value: `"Week"`)

* `Month` (value: `"Month"`)

* `Minute` (value: `"Minute"`)




