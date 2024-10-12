# CalendarApi.ConferenceSolutionKey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **String** | The conference solution type. If a client encounters an unfamiliar or empty type, it should still be able to display the entry points. However, it should disallow modifications. The possible values are:   - \&quot;eventHangout\&quot; for Hangouts for consumers (deprecated; existing events may show this conference solution type but new conferences cannot be created) - \&quot;eventNamedHangout\&quot; for classic Hangouts for Google Workspace users (deprecated; existing events may show this conference solution type but new conferences cannot be created) - \&quot;hangoutsMeet\&quot; for Google Meet (http://meet.google.com) - \&quot;addOn\&quot; for 3P conference providers | [optional] 


