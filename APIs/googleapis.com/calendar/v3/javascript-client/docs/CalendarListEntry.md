# CalendarApi.CalendarListEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessRole** | **String** | The effective access role that the authenticated user has on the calendar. Read-only. Possible values are:   - \&quot;freeBusyReader\&quot; - Provides read access to free/busy information.  - \&quot;reader\&quot; - Provides read access to the calendar. Private events will appear to users with reader access, but event details will be hidden.  - \&quot;writer\&quot; - Provides read and write access to the calendar. Private events will appear to users with writer access, and event details will be visible.  - \&quot;owner\&quot; - Provides ownership of the calendar. This role has all of the permissions of the writer role with the additional ability to see and manipulate ACLs. | [optional] 
**backgroundColor** | **String** | The main color of the calendar in the hexadecimal format \&quot;#0088aa\&quot;. This property supersedes the index-based colorId property. To set or change this property, you need to specify colorRgbFormat&#x3D;true in the parameters of the insert, update and patch methods. Optional. | [optional] 
**colorId** | **String** | The color of the calendar. This is an ID referring to an entry in the calendar section of the colors definition (see the colors endpoint). This property is superseded by the backgroundColor and foregroundColor properties and can be ignored when using these properties. Optional. | [optional] 
**conferenceProperties** | [**ConferenceProperties**](ConferenceProperties.md) |  | [optional] 
**defaultReminders** | [**[EventReminder]**](EventReminder.md) | The default reminders that the authenticated user has for this calendar. | [optional] 
**deleted** | **Boolean** | Whether this calendar list entry has been deleted from the calendar list. Read-only. Optional. The default is False. | [optional] [default to false]
**description** | **String** | Description of the calendar. Optional. Read-only. | [optional] 
**etag** | **String** | ETag of the resource. | [optional] 
**foregroundColor** | **String** | The foreground color of the calendar in the hexadecimal format \&quot;#ffffff\&quot;. This property supersedes the index-based colorId property. To set or change this property, you need to specify colorRgbFormat&#x3D;true in the parameters of the insert, update and patch methods. Optional. | [optional] 
**hidden** | **Boolean** | Whether the calendar has been hidden from the list. Optional. The attribute is only returned when the calendar is hidden, in which case the value is true. | [optional] [default to false]
**id** | **String** | Identifier of the calendar. | [optional] 
**kind** | **String** | Type of the resource (\&quot;calendar#calendarListEntry\&quot;). | [optional] [default to &#39;calendar#calendarListEntry&#39;]
**location** | **String** | Geographic location of the calendar as free-form text. Optional. Read-only. | [optional] 
**notificationSettings** | [**CalendarListEntryNotificationSettings**](CalendarListEntryNotificationSettings.md) |  | [optional] 
**primary** | **Boolean** | Whether the calendar is the primary calendar of the authenticated user. Read-only. Optional. The default is False. | [optional] [default to false]
**selected** | **Boolean** | Whether the calendar content shows up in the calendar UI. Optional. The default is False. | [optional] [default to false]
**summary** | **String** | Title of the calendar. Read-only. | [optional] 
**summaryOverride** | **String** | The summary that the authenticated user has set for this calendar. Optional. | [optional] 
**timeZone** | **String** | The time zone of the calendar. Optional. Read-only. | [optional] 


