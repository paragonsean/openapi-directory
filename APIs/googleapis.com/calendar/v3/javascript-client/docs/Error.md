# CalendarApi.Error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **String** | Domain, or broad category, of the error. | [optional] 
**reason** | **String** | Specific reason for the error. Some of the possible values are:   - \&quot;groupTooBig\&quot; - The group of users requested is too large for a single query.  - \&quot;tooManyCalendarsRequested\&quot; - The number of calendars requested is too large for a single query.  - \&quot;notFound\&quot; - The requested resource was not found.  - \&quot;internalError\&quot; - The API service has encountered an internal error.  Additional error types may be added in the future, so clients should gracefully handle additional error statuses not included in this list. | [optional] 


