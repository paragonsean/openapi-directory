

# EventReminders

Information about the event's reminders for the authenticated user.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**overrides** | [**List&lt;EventReminder&gt;**](EventReminder.md) | If the event doesn&#39;t use the default reminders, this lists the reminders specific to the event, or, if not set, indicates that no reminders are set for this event. The maximum number of override reminders is 5. |  [optional] |
|**useDefault** | **Boolean** | Whether the default reminders of the calendar apply to the event. |  [optional] |



