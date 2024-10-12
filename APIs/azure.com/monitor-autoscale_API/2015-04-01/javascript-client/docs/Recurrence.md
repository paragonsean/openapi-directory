# MonitorManagementClient.Recurrence

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **String** | the recurrence frequency. How often the schedule profile should take effect. This value must be Week, meaning each week will have the same set of profiles. For example, to set a daily schedule, set **schedule** to every day of the week. The frequency property specifies that the schedule is repeated weekly. | 
**schedule** | [**RecurrentSchedule**](RecurrentSchedule.md) |  | 



## Enum: FrequencyEnum


* `None` (value: `"None"`)

* `Second` (value: `"Second"`)

* `Minute` (value: `"Minute"`)

* `Hour` (value: `"Hour"`)

* `Day` (value: `"Day"`)

* `Week` (value: `"Week"`)

* `Month` (value: `"Month"`)

* `Year` (value: `"Year"`)




