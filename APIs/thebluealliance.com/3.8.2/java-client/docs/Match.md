

# Match


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actualTime** | **Long** | UNIX timestamp (seconds since 1-Jan-1970 00:00:00) of actual match start time. |  [optional] |
|**alliances** | [**MatchAlliances**](MatchAlliances.md) |  |  [optional] |
|**compLevel** | [**CompLevelEnum**](#CompLevelEnum) | The competition level the match was played at. |  |
|**eventKey** | **String** | Event key of the event the match was played at. |  |
|**key** | **String** | TBA match key with the format &#x60;yyyy[EVENT_CODE]_[COMP_LEVEL]m[MATCH_NUMBER]&#x60;, where &#x60;yyyy&#x60; is the year, and &#x60;EVENT_CODE&#x60; is the event code of the event, &#x60;COMP_LEVEL&#x60; is (qm, ef, qf, sf, f), and &#x60;MATCH_NUMBER&#x60; is the match number in the competition level. A set number may be appended to the competition level if more than one match in required per set. |  |
|**matchNumber** | **Integer** | The match number of the match in the competition level. |  |
|**postResultTime** | **Long** | UNIX timestamp (seconds since 1-Jan-1970 00:00:00) when the match result was posted. |  [optional] |
|**predictedTime** | **Long** | UNIX timestamp (seconds since 1-Jan-1970 00:00:00) of the TBA predicted match start time. |  [optional] |
|**scoreBreakdown** | **Object** | Score breakdown for auto, teleop, etc. points. Varies from year to year. May be null. |  [optional] |
|**setNumber** | **Integer** | The set number in a series of matches where more than one match is required in the match series. |  |
|**time** | **Long** | UNIX timestamp (seconds since 1-Jan-1970 00:00:00) of the scheduled match time, as taken from the published schedule. |  [optional] |
|**videos** | [**List&lt;MatchVideosInner&gt;**](MatchVideosInner.md) | Array of video objects associated with this match. |  [optional] |
|**winningAlliance** | [**WinningAllianceEnum**](#WinningAllianceEnum) | The color (red/blue) of the winning alliance. Will contain an empty string in the event of no winner, or a tie. |  [optional] |



## Enum: CompLevelEnum

| Name | Value |
|---- | -----|
| QM | &quot;qm&quot; |
| EF | &quot;ef&quot; |
| QF | &quot;qf&quot; |
| SF | &quot;sf&quot; |
| F | &quot;f&quot; |



## Enum: WinningAllianceEnum

| Name | Value |
|---- | -----|
| RED | &quot;red&quot; |
| BLUE | &quot;blue&quot; |
| EMPTY | &quot;&quot; |



