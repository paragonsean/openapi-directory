# MyBusinessBusinessInformationApi.TimeOfDay

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hours** | **Number** | Hours of day in 24 hour format. Should be from 0 to 23. An API may choose to allow the value \&quot;24:00:00\&quot; for scenarios like business closing time. | [optional] 
**minutes** | **Number** | Minutes of hour of day. Must be from 0 to 59. | [optional] 
**nanos** | **Number** | Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999. | [optional] 
**seconds** | **Number** | Seconds of minutes of the time. Must normally be from 0 to 59. An API may allow the value 60 if it allows leap-seconds. | [optional] 


