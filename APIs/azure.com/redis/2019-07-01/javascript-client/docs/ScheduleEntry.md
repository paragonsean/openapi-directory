# RedisManagementClient.ScheduleEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dayOfWeek** | **String** | Day of the week when a cache can be patched. | 
**maintenanceWindow** | **String** | ISO8601 timespan specifying how much time cache patching can take.  | [optional] 
**startHourUtc** | **Number** | Start hour after which cache patching can start. | 



## Enum: DayOfWeekEnum


* `Monday` (value: `"Monday"`)

* `Tuesday` (value: `"Tuesday"`)

* `Wednesday` (value: `"Wednesday"`)

* `Thursday` (value: `"Thursday"`)

* `Friday` (value: `"Friday"`)

* `Saturday` (value: `"Saturday"`)

* `Sunday` (value: `"Sunday"`)

* `Everyday` (value: `"Everyday"`)

* `Weekend` (value: `"Weekend"`)




