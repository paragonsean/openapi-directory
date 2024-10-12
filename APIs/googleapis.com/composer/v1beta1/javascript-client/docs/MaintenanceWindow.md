# CloudComposerApi.MaintenanceWindow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **String** | Required. Maintenance window end time. It is used only to calculate the duration of the maintenance window. The value for end_time must be in the future, relative to &#x60;start_time&#x60;. | [optional] 
**recurrence** | **String** | Required. Maintenance window recurrence. Format is a subset of [RFC-5545](https://tools.ietf.org/html/rfc5545) &#x60;RRULE&#x60;. The only allowed values for &#x60;FREQ&#x60; field are &#x60;FREQ&#x3D;DAILY&#x60; and &#x60;FREQ&#x3D;WEEKLY;BYDAY&#x3D;...&#x60; Example values: &#x60;FREQ&#x3D;WEEKLY;BYDAY&#x3D;TU,WE&#x60;, &#x60;FREQ&#x3D;DAILY&#x60;. | [optional] 
**startTime** | **String** | Required. Start time of the first recurrence of the maintenance window. | [optional] 


