# CalendarApi.CalendarList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etag** | **String** | ETag of the collection. | [optional] 
**items** | [**[CalendarListEntry]**](CalendarListEntry.md) | Calendars that are present on the user&#39;s calendar list. | [optional] 
**kind** | **String** | Type of the collection (\&quot;calendar#calendarList\&quot;). | [optional] [default to &#39;calendar#calendarList&#39;]
**nextPageToken** | **String** | Token used to access the next page of this result. Omitted if no further results are available, in which case nextSyncToken is provided. | [optional] 
**nextSyncToken** | **String** | Token used at a later point in time to retrieve only the entries that have changed since this result was returned. Omitted if further results are available, in which case nextPageToken is provided. | [optional] 


