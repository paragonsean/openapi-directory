

# EnterpriseTopazSidekickAgendaEntry

An AgendaEntry, e.g., a Calendar Event.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agendaItemUrl** | **String** | URL of the agenda item. |  [optional] |
|**chronology** | [**ChronologyEnum**](#ChronologyEnum) | The chronology from the present. |  [optional] |
|**creator** | [**EnterpriseTopazSidekickPerson**](EnterpriseTopazSidekickPerson.md) |  |  [optional] |
|**currentUserAttendingStatus** | [**CurrentUserAttendingStatusEnum**](#CurrentUserAttendingStatusEnum) | Attendance status for the current user making the request. This is a convenience data member in order to avoid figuring out the same by iterating the invitee list above on the caller side. |  [optional] |
|**description** | **String** | Description of the agenda item (i.e., typically, summary in calendar event). |  [optional] |
|**document** | [**List&lt;EnterpriseTopazSidekickCommonDocument&gt;**](EnterpriseTopazSidekickCommonDocument.md) | Items related to the current AgendaEntry. E.g., related drive/mail/groups documents. |  [optional] |
|**endDate** | **String** | End date \&quot;Friday, August 26\&quot; in the user&#39;s timezone. |  [optional] |
|**endTime** | **String** | End time (HH:mm) in the user&#39;s timezone. |  [optional] |
|**endTimeMs** | **String** | End time in milliseconds |  [optional] |
|**eventId** | **String** | Event id provided by Calendar API. |  [optional] |
|**guestsCanInviteOthers** | **Boolean** | Whether the guests can invite other guests. |  [optional] |
|**guestsCanModify** | **Boolean** | Whether the guests can modify the event. |  [optional] |
|**guestsCanSeeGuests** | **Boolean** | Whether the guests of the event can be seen. If false, the user is going to be reported as the only attendee to the meeting, even though there may be more attendees. |  [optional] |
|**hangoutId** | **String** | Hangout meeting identifier. |  [optional] |
|**hangoutUrl** | **String** | Absolute URL for the Hangout meeting. |  [optional] |
|**invitee** | [**List&lt;EnterpriseTopazSidekickPerson&gt;**](EnterpriseTopazSidekickPerson.md) | People attending the meeting. |  [optional] |
|**isAllDay** | **Boolean** | Whether the entry lasts all day. |  [optional] |
|**lastModificationTimeMs** | **String** | Last time the event was modified. |  [optional] |
|**location** | **String** | Agenda item location. |  [optional] |
|**notifyToUser** | **Boolean** | Whether this should be notified to the user. |  [optional] |
|**otherAttendeesExcluded** | **Boolean** | Whether guest list is not returned because number of attendees is too large. |  [optional] |
|**requesterIsOwner** | **Boolean** | Whether the requester is the owner of the agenda entry. |  [optional] |
|**showFullEventDetailsToUse** | **Boolean** | Whether the details of this entry should be displayed to the user. |  [optional] |
|**startDate** | **String** | Start date \&quot;Friday, August 26\&quot; in the user&#39;s timezone. |  [optional] |
|**startTime** | **String** | Start time (HH:mm) in the user&#39;s timezone. |  [optional] |
|**startTimeMs** | **String** | Start time in milliseconds. |  [optional] |
|**timeZone** | **String** | User&#39;s calendar timezone; |  [optional] |
|**title** | **String** | Title of the agenda item. |  [optional] |



## Enum: ChronologyEnum

| Name | Value |
|---- | -----|
| STALE | &quot;STALE&quot; |
| ALL_DAY | &quot;ALL_DAY&quot; |
| PAST | &quot;PAST&quot; |
| RECENTLY_PAST | &quot;RECENTLY_PAST&quot; |
| PRESENT | &quot;PRESENT&quot; |
| NEAR_FUTURE | &quot;NEAR_FUTURE&quot; |
| FUTURE | &quot;FUTURE&quot; |



## Enum: CurrentUserAttendingStatusEnum

| Name | Value |
|---- | -----|
| AWAITING | &quot;AWAITING&quot; |
| TRUE | &quot;true&quot; |
| FALSE | &quot;false&quot; |
| MAYBE | &quot;MAYBE&quot; |



