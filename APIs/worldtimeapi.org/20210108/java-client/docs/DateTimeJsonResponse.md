

# DateTimeJsonResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**abbreviation** | **String** | the abbreviated name of the timezone |  |
|**clientIp** | **String** | the IP of the client making the request |  |
|**datetime** | **String** | an ISO8601-valid string representing the current, local date/time |  |
|**dayOfWeek** | **Integer** | current day number of the week, where sunday is 0 |  |
|**dayOfYear** | **Integer** | ordinal date of the current year |  |
|**dst** | **Boolean** | flag indicating whether the local time is in daylight savings |  |
|**dstFrom** | **String** | an ISO8601-valid string representing the datetime when daylight savings started for this timezone |  [optional] |
|**dstOffset** | **Integer** | the difference in seconds between the current local time and daylight saving time for the location |  |
|**dstUntil** | **String** | an ISO8601-valid string representing the datetime when daylight savings will end for this timezone |  [optional] |
|**rawOffset** | **Integer** | the difference in seconds between the current local time and the time in UTC, excluding any daylight saving difference (see dst_offset) |  [optional] |
|**timezone** | **String** | timezone in &#x60;Area/Location&#x60; or &#x60;Area/Location/Region&#x60; format |  |
|**unixtime** | **Integer** | number of seconds since the Epoch |  |
|**utcDatetime** | **String** | an ISO8601-valid string representing the current date/time in UTC |  |
|**utcOffset** | **String** | an ISO8601-valid string representing the offset from UTC |  |
|**weekNumber** | **Integer** | the current week number |  |



