

# FreeBusyRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**calendarExpansionMax** | **Integer** | Maximal number of calendars for which FreeBusy information is to be provided. Optional. Maximum value is 50. |  [optional] |
|**groupExpansionMax** | **Integer** | Maximal number of calendar identifiers to be provided for a single group. Optional. An error is returned for a group with more members than this value. Maximum value is 100. |  [optional] |
|**items** | [**List&lt;FreeBusyRequestItem&gt;**](FreeBusyRequestItem.md) | List of calendars and/or groups to query. |  [optional] |
|**timeMax** | **OffsetDateTime** | The end of the interval for the query formatted as per RFC3339. |  [optional] |
|**timeMin** | **OffsetDateTime** | The start of the interval for the query formatted as per RFC3339. |  [optional] |
|**timeZone** | **String** | Time zone used in the response. Optional. The default is UTC. |  [optional] |



