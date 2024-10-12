

# Events


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessRole** | **String** | The user&#39;s access role for this calendar. Read-only. Possible values are:   - \&quot;none\&quot; - The user has no access.  - \&quot;freeBusyReader\&quot; - The user has read access to free/busy information.  - \&quot;reader\&quot; - The user has read access to the calendar. Private events will appear to users with reader access, but event details will be hidden.  - \&quot;writer\&quot; - The user has read and write access to the calendar. Private events will appear to users with writer access, and event details will be visible.  - \&quot;owner\&quot; - The user has ownership of the calendar. This role has all of the permissions of the writer role with the additional ability to see and manipulate ACLs. |  [optional] |
|**defaultReminders** | [**List&lt;EventReminder&gt;**](EventReminder.md) | The default reminders on the calendar for the authenticated user. These reminders apply to all events on this calendar that do not explicitly override them (i.e. do not have reminders.useDefault set to True). |  [optional] |
|**description** | **String** | Description of the calendar. Read-only. |  [optional] |
|**etag** | **String** | ETag of the collection. |  [optional] |
|**items** | [**List&lt;Event&gt;**](Event.md) | List of events on the calendar. |  [optional] |
|**kind** | **String** | Type of the collection (\&quot;calendar#events\&quot;). |  [optional] |
|**nextPageToken** | **String** | Token used to access the next page of this result. Omitted if no further results are available, in which case nextSyncToken is provided. |  [optional] |
|**nextSyncToken** | **String** | Token used at a later point in time to retrieve only the entries that have changed since this result was returned. Omitted if further results are available, in which case nextPageToken is provided. |  [optional] |
|**summary** | **String** | Title of the calendar. Read-only. |  [optional] |
|**timeZone** | **String** | The time zone of the calendar. Read-only. |  [optional] |
|**updated** | **OffsetDateTime** | Last modification time of the calendar (as a RFC3339 timestamp). Read-only. |  [optional] |



