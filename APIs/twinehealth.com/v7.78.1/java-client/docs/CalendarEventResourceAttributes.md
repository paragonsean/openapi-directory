

# CalendarEventResourceAttributes


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allDay** | **Boolean** | True if the calendar event is an all day event, false otherwise. Must be set to true for &#x60;plan-check-in&#x60; event type. If it is true, then &#x60;start_at&#x60; and &#x60;end_at&#x60; must also be set to beginning of day, except &#x60;plan-check-in&#x60; event type does not need an &#x60;end_at&#x60; date. If it is false, then &#x60;start_at&#x60; and &#x60;end_at&#x60; must be on the same day. |  [optional] |
|**attendees** | [**List&lt;CalendarEventResourceAttributesAttendeesInner&gt;**](CalendarEventResourceAttributesAttendeesInner.md) | List of attendees for the calendar event |  [optional] |
|**completedAt** | **String** | The date and time when the calendar event is marked as completed. Only valid for &#x60;plan-check-in&#x60; event type. |  [optional] |
|**completedBy** | **Object** | The coach who marked the calendar event as completed. Only valid for &#x60;plan-check-in&#x60; event type. |  [optional] |
|**description** | **String** |  |  [optional] |
|**endAt** | **String** | The date and time when the calendar event ends. Not valid for &#x60;plan-check-in&#x60; event type. |  [optional] |
|**location** | **String** |  |  [optional] |
|**startAt** | **String** | The date and time when the calendar event starts |  [optional] |
|**timeZone** | **String** | The time zone in which the dates for the calendar event are specified |  [optional] |
|**title** | **String** | The title of the calendar event. Must not be empty or null |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of calendar event. Immutable after event creation. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PLAN_CHECK_IN | &quot;plan-check-in&quot; |
| REMINDER | &quot;reminder&quot; |
| TELEPHONE_CALL | &quot;telephone-call&quot; |
| OFFICE_VISIT | &quot;office-visit&quot; |
| VIDEO_CALL | &quot;video-call&quot; |



