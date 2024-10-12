

# EventAttendee


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalGuests** | **Integer** | Number of additional guests. Optional. The default is 0. |  [optional] |
|**comment** | **String** | The attendee&#39;s response comment. Optional. |  [optional] |
|**displayName** | **String** | The attendee&#39;s name, if available. Optional. |  [optional] |
|**email** | **String** | The attendee&#39;s email address, if available. This field must be present when adding an attendee. It must be a valid email address as per RFC5322. Required when adding an attendee. |  [optional] |
|**id** | **String** | The attendee&#39;s Profile ID, if available. |  [optional] |
|**optional** | **Boolean** | Whether this is an optional attendee. Optional. The default is False. |  [optional] |
|**organizer** | **Boolean** | Whether the attendee is the organizer of the event. Read-only. The default is False. |  [optional] |
|**resource** | **Boolean** | Whether the attendee is a resource. Can only be set when the attendee is added to the event for the first time. Subsequent modifications are ignored. Optional. The default is False. |  [optional] |
|**responseStatus** | **String** | The attendee&#39;s response status. Possible values are:   - \&quot;needsAction\&quot; - The attendee has not responded to the invitation (recommended for new events).  - \&quot;declined\&quot; - The attendee has declined the invitation.  - \&quot;tentative\&quot; - The attendee has tentatively accepted the invitation.  - \&quot;accepted\&quot; - The attendee has accepted the invitation.  Warning: If you add an event using the values declined, tentative, or accepted, attendees with the \&quot;Add invitations to my calendar\&quot; setting set to \&quot;When I respond to invitation in email\&quot; won&#39;t see an event on their calendar unless they choose to change their invitation response in the event invitation email. |  [optional] |
|**self** | **Boolean** | Whether this entry represents the calendar on which this copy of the event appears. Read-only. The default is False. |  [optional] |



