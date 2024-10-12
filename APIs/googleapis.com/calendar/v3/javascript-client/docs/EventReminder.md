# CalendarApi.EventReminder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **String** | The method used by this reminder. Possible values are:   - \&quot;email\&quot; - Reminders are sent via email.  - \&quot;popup\&quot; - Reminders are sent via a UI popup.   Required when adding a reminder. | [optional] 
**minutes** | **Number** | Number of minutes before the start of the event when the reminder should trigger. Valid values are between 0 and 40320 (4 weeks in minutes). Required when adding a reminder. | [optional] 


