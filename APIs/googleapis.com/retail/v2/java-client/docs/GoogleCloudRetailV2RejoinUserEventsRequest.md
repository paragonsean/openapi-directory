

# GoogleCloudRetailV2RejoinUserEventsRequest

Request message for RejoinUserEvents method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**userEventRejoinScope** | [**UserEventRejoinScopeEnum**](#UserEventRejoinScopeEnum) | The type of the user event rejoin to define the scope and range of the user events to be rejoined with the latest product catalog. Defaults to &#x60;USER_EVENT_REJOIN_SCOPE_UNSPECIFIED&#x60; if this field is not set, or set to an invalid integer value. |  [optional] |



## Enum: UserEventRejoinScopeEnum

| Name | Value |
|---- | -----|
| USER_EVENT_REJOIN_SCOPE_UNSPECIFIED | &quot;USER_EVENT_REJOIN_SCOPE_UNSPECIFIED&quot; |
| JOINED_EVENTS | &quot;JOINED_EVENTS&quot; |
| UNJOINED_EVENTS | &quot;UNJOINED_EVENTS&quot; |



