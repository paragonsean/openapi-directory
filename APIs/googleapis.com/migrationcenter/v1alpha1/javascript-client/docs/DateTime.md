# MigrationCenterApi.DateTime

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **Number** | Optional. Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a datetime without a day. | [optional] 
**hours** | **Number** | Optional. Hours of day in 24 hour format. Should be from 0 to 23, defaults to 0 (midnight). An API may choose to allow the value \&quot;24:00:00\&quot; for scenarios like business closing time. | [optional] 
**minutes** | **Number** | Optional. Minutes of hour of day. Must be from 0 to 59, defaults to 0. | [optional] 
**month** | **Number** | Optional. Month of year. Must be from 1 to 12, or 0 if specifying a datetime without a month. | [optional] 
**nanos** | **Number** | Optional. Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999, defaults to 0. | [optional] 
**seconds** | **Number** | Optional. Seconds of minutes of the time. Must normally be from 0 to 59, defaults to 0. An API may allow the value 60 if it allows leap-seconds. | [optional] 
**timeZone** | [**TimeZone**](TimeZone.md) |  | [optional] 
**utcOffset** | **String** | UTC offset. Must be whole seconds, between -18 hours and +18 hours. For example, a UTC offset of -4:00 would be represented as { seconds: -14400 }. | [optional] 
**year** | **Number** | Optional. Year of date. Must be from 1 to 9999, or 0 if specifying a datetime without a year. | [optional] 


