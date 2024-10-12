

# CalendarNotification


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**method** | **String** | The method used to deliver the notification. The possible value is:   - \&quot;email\&quot; - Notifications are sent via email.   Required when adding a notification. |  [optional] |
|**type** | **String** | The type of notification. Possible values are:   - \&quot;eventCreation\&quot; - Notification sent when a new event is put on the calendar.  - \&quot;eventChange\&quot; - Notification sent when an event is changed.  - \&quot;eventCancellation\&quot; - Notification sent when an event is cancelled.  - \&quot;eventResponse\&quot; - Notification sent when an attendee responds to the event invitation.  - \&quot;agenda\&quot; - An agenda with the events of the day (sent out in the morning).   Required when adding a notification. |  [optional] |



