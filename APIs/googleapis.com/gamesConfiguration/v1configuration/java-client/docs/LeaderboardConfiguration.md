

# LeaderboardConfiguration

An leaderboard configuration resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**draft** | [**LeaderboardConfigurationDetail**](LeaderboardConfigurationDetail.md) |  |  [optional] |
|**id** | **String** | The ID of the leaderboard. |  [optional] |
|**kind** | **String** | Uniquely identifies the type of this resource. Value is always the fixed string &#x60;gamesConfiguration#leaderboardConfiguration&#x60;. |  [optional] |
|**published** | [**LeaderboardConfigurationDetail**](LeaderboardConfigurationDetail.md) |  |  [optional] |
|**scoreMax** | **String** | Maximum score that can be posted to this leaderboard. |  [optional] |
|**scoreMin** | **String** | Minimum score that can be posted to this leaderboard. |  [optional] |
|**scoreOrder** | [**ScoreOrderEnum**](#ScoreOrderEnum) |  |  [optional] |
|**token** | **String** | The token for this resource. |  [optional] |



## Enum: ScoreOrderEnum

| Name | Value |
|---- | -----|
| SCORE_ORDER_UNSPECIFIED | &quot;SCORE_ORDER_UNSPECIFIED&quot; |
| LARGER_IS_BETTER | &quot;LARGER_IS_BETTER&quot; |
| SMALLER_IS_BETTER | &quot;SMALLER_IS_BETTER&quot; |



