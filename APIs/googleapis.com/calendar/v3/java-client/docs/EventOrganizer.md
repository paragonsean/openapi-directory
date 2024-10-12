

# EventOrganizer

The organizer of the event. If the organizer is also an attendee, this is indicated with a separate entry in attendees with the organizer field set to True. To change the organizer, use the move operation. Read-only, except when importing an event.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | The organizer&#39;s name, if available. |  [optional] |
|**email** | **String** | The organizer&#39;s email address, if available. It must be a valid email address as per RFC5322. |  [optional] |
|**id** | **String** | The organizer&#39;s Profile ID, if available. |  [optional] |
|**self** | **Boolean** | Whether the organizer corresponds to the calendar on which this copy of the event appears. Read-only. The default is False. |  [optional] |



