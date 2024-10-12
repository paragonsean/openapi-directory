

# LeaderboardEntry

The Leaderboard Entry resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**formattedScore** | **String** | The localized string for the numerical value of this score. |  [optional] |
|**formattedScoreRank** | **String** | The localized string for the rank of this score for this leaderboard. |  [optional] |
|**kind** | **String** | Uniquely identifies the type of this resource. Value is always the fixed string &#x60;games#leaderboardEntry&#x60;. |  [optional] |
|**player** | [**Player**](Player.md) |  |  [optional] |
|**scoreRank** | **String** | The rank of this score for this leaderboard. |  [optional] |
|**scoreTag** | **String** | Additional information about the score. Values must contain no more than 64 URI-safe characters as defined by section 2.3 of RFC 3986. |  [optional] |
|**scoreValue** | **String** | The numerical value of this score. |  [optional] |
|**timeSpan** | [**TimeSpanEnum**](#TimeSpanEnum) | The time span of this high score. |  [optional] |
|**writeTimestampMillis** | **String** | The timestamp at which this score was recorded, in milliseconds since the epoch in UTC. |  [optional] |



## Enum: TimeSpanEnum

| Name | Value |
|---- | -----|
| ALL_TIME | &quot;ALL_TIME&quot; |
| WEEKLY | &quot;WEEKLY&quot; |
| DAILY | &quot;DAILY&quot; |



