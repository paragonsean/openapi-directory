

# Show

A `Show` object describes one occurrence of a radio program. A result set may contain multiple occurrences of the same show with difference `start` and `end` values.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**ShowLinks**](ShowLinks.md) |  |  [optional] |
|**category** | **String** | Program/show category |  [optional] |
|**description** | **String** | HTML-formatted description of the playlist or program/show |  [optional] |
|**duration** | **Integer** | Duration in seconds |  [optional] |
|**end** | **OffsetDateTime** | UTC datetime ISO-8601 |  [optional] |
|**hideDj** | **Boolean** | Should the client application hide information about the show&#39;s DJs/hosts? |  [optional] |
|**id** | **Integer** |  |  [optional] |
|**image** | **String** |  |  [optional] |
|**oneOff** | **Boolean** | Is the show a one-off in the schedule instead of repeating? |  [optional] |
|**since** | **Integer** | Since what year has the program/show existed? |  [optional] |
|**start** | **OffsetDateTime** | UTC datetime ISO-8601 |  [optional] |
|**timezone** | **String** | Station&#39;s time zone |  [optional] |
|**title** | **String** | Program/show title |  [optional] |
|**url** | **String** | URL to web site for the program/show |  [optional] |



