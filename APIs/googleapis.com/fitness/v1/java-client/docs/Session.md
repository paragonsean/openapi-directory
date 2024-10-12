

# Session

Sessions contain metadata, such as a user-friendly name and time interval information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeTimeMillis** | **String** | Session active time. While start_time_millis and end_time_millis define the full session time, the active time can be shorter and specified by active_time_millis. If the inactive time during the session is known, it should also be inserted via a com.google.activity.segment data point with a STILL activity value |  [optional] |
|**activityType** | **Integer** | The type of activity this session represents. |  [optional] |
|**application** | [**Application**](Application.md) |  |  [optional] |
|**description** | **String** | A description for this session. |  [optional] |
|**endTimeMillis** | **String** | An end time, in milliseconds since epoch, inclusive. |  [optional] |
|**id** | **String** | A client-generated identifier that is unique across all sessions owned by this particular user. |  [optional] |
|**modifiedTimeMillis** | **String** | A timestamp that indicates when the session was last modified. |  [optional] |
|**name** | **String** | A human readable name of the session. |  [optional] |
|**startTimeMillis** | **String** | A start time, in milliseconds since epoch, inclusive. |  [optional] |



