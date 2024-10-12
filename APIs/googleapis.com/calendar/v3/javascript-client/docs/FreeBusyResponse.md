# CalendarApi.FreeBusyResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendars** | [**{String: FreeBusyCalendar}**](FreeBusyCalendar.md) | List of free/busy information for calendars. | [optional] 
**groups** | [**{String: FreeBusyGroup}**](FreeBusyGroup.md) | Expansion of groups. | [optional] 
**kind** | **String** | Type of the resource (\&quot;calendar#freeBusy\&quot;). | [optional] [default to &#39;calendar#freeBusy&#39;]
**timeMax** | **Date** | The end of the interval. | [optional] 
**timeMin** | **Date** | The start of the interval. | [optional] 


