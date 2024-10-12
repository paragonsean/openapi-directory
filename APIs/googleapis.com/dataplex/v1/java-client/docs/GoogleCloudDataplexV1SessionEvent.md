

# GoogleCloudDataplexV1SessionEvent

These messages contain information about sessions within an environment. The monitored resource is 'Environment'.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventSucceeded** | **Boolean** | The status of the event. |  [optional] |
|**fastStartupEnabled** | **Boolean** | If the session is associated with an environment with fast startup enabled, and was created before being assigned to a user. |  [optional] |
|**message** | **String** | The log message. |  [optional] |
|**query** | [**GoogleCloudDataplexV1SessionEventQueryDetail**](GoogleCloudDataplexV1SessionEventQueryDetail.md) |  |  [optional] |
|**sessionId** | **String** | Unique identifier for the session. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the event. |  [optional] |
|**unassignedDuration** | **String** | The idle duration of a warm pooled session before it is assigned to user. |  [optional] |
|**userId** | **String** | The information about the user that created the session. It will be the email address of the user. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| EVENT_TYPE_UNSPECIFIED | &quot;EVENT_TYPE_UNSPECIFIED&quot; |
| START | &quot;START&quot; |
| STOP | &quot;STOP&quot; |
| QUERY | &quot;QUERY&quot; |
| CREATE | &quot;CREATE&quot; |



