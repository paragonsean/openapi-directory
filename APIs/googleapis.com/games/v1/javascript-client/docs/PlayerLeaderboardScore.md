# GooglePlayGameServices.PlayerLeaderboardScore

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**friendsRank** | [**LeaderboardScoreRank**](LeaderboardScoreRank.md) |  | [optional] 
**kind** | **String** | Uniquely identifies the type of this resource. Value is always the fixed string &#x60;games#playerLeaderboardScore&#x60;. | [optional] 
**leaderboardId** | **String** | The ID of the leaderboard this score is in. | [optional] 
**publicRank** | [**LeaderboardScoreRank**](LeaderboardScoreRank.md) |  | [optional] 
**scoreString** | **String** | The formatted value of this score. | [optional] 
**scoreTag** | **String** | Additional information about the score. Values must contain no more than 64 URI-safe characters as defined by section 2.3 of RFC 3986. | [optional] 
**scoreValue** | **String** | The numerical value of this score. | [optional] 
**socialRank** | [**LeaderboardScoreRank**](LeaderboardScoreRank.md) |  | [optional] 
**timeSpan** | **String** | The time span of this score. | [optional] 
**writeTimestamp** | **String** | The timestamp at which this score was recorded, in milliseconds since the epoch in UTC. | [optional] 



## Enum: TimeSpanEnum


* `ALL_TIME` (value: `"ALL_TIME"`)

* `WEEKLY` (value: `"WEEKLY"`)

* `DAILY` (value: `"DAILY"`)




