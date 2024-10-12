# TheBlueAllianceApiV3.Match

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actualTime** | **Number** | UNIX timestamp (seconds since 1-Jan-1970 00:00:00) of actual match start time. | [optional] 
**alliances** | [**MatchAlliances**](MatchAlliances.md) |  | [optional] 
**compLevel** | **String** | The competition level the match was played at. | 
**eventKey** | **String** | Event key of the event the match was played at. | 
**key** | **String** | TBA match key with the format &#x60;yyyy[EVENT_CODE]_[COMP_LEVEL]m[MATCH_NUMBER]&#x60;, where &#x60;yyyy&#x60; is the year, and &#x60;EVENT_CODE&#x60; is the event code of the event, &#x60;COMP_LEVEL&#x60; is (qm, ef, qf, sf, f), and &#x60;MATCH_NUMBER&#x60; is the match number in the competition level. A set number may be appended to the competition level if more than one match in required per set. | 
**matchNumber** | **Number** | The match number of the match in the competition level. | 
**postResultTime** | **Number** | UNIX timestamp (seconds since 1-Jan-1970 00:00:00) when the match result was posted. | [optional] 
**predictedTime** | **Number** | UNIX timestamp (seconds since 1-Jan-1970 00:00:00) of the TBA predicted match start time. | [optional] 
**scoreBreakdown** | **Object** | Score breakdown for auto, teleop, etc. points. Varies from year to year. May be null. | [optional] 
**setNumber** | **Number** | The set number in a series of matches where more than one match is required in the match series. | 
**time** | **Number** | UNIX timestamp (seconds since 1-Jan-1970 00:00:00) of the scheduled match time, as taken from the published schedule. | [optional] 
**videos** | [**[MatchVideosInner]**](MatchVideosInner.md) | Array of video objects associated with this match. | [optional] 
**winningAlliance** | **String** | The color (red/blue) of the winning alliance. Will contain an empty string in the event of no winner, or a tie. | [optional] 



## Enum: CompLevelEnum


* `qm` (value: `"qm"`)

* `ef` (value: `"ef"`)

* `qf` (value: `"qf"`)

* `sf` (value: `"sf"`)

* `f` (value: `"f"`)





## Enum: WinningAllianceEnum


* `red` (value: `"red"`)

* `blue` (value: `"blue"`)

* `empty` (value: `""`)




