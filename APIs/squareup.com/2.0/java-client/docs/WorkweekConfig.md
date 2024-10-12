

# WorkweekConfig

Sets the day of the week and hour of the day that a business starts a workweek. This is used to calculate overtime pay.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **String** | A read-only timestamp in RFC 3339 format; presented in UTC. |  [optional] |
|**id** | **String** | The UUID for this object. |  [optional] |
|**startOfDayLocalTime** | **String** | The local time at which a business week ends. Represented as a string in &#x60;HH:MM&#x60; format (&#x60;HH:MM:SS&#x60; is also accepted, but seconds are truncated). |  |
|**startOfWeek** | **String** | The day of the week on which a business week ends for compensation purposes. |  |
|**updatedAt** | **String** | A read-only timestamp in RFC 3339 format; presented in UTC. |  [optional] |
|**version** | **Integer** | Used for resolving concurrency issues. The request fails if the version provided does not match the server version at the time of the request. If not provided, Square executes a blind write; potentially overwriting data from another write. |  [optional] |



