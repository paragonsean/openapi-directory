# GoogleMyBusinessApi.SpecialHourPeriod

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closeTime** | **String** | The wall time on &#x60;end_date&#x60; when a location closes, expressed in 24hr ISO 8601 extended format. (hh:mm) Valid values are 00:00-24:00, where 24:00 represents midnight at the end of the specified day field. Must be specified if &#x60;is_closed&#x60; is false. | [optional] 
**endDate** | [**ModelDate**](ModelDate.md) |  | [optional] 
**isClosed** | **Boolean** | If true, &#x60;end_date&#x60;, &#x60;open_time&#x60;, and &#x60;close_time&#x60; are ignored, and the date specified in &#x60;start_date&#x60; is treated as the location being closed for the entire day. | [optional] 
**openTime** | **String** | The wall time on &#x60;start_date&#x60; when a location opens, expressed in 24hr ISO 8601 extended format. (hh:mm) Valid values are 00:00-24:00, where 24:00 represents midnight at the end of the specified day field. Must be specified if &#x60;is_closed&#x60; is false. | [optional] 
**startDate** | [**ModelDate**](ModelDate.md) |  | [optional] 


