# GooglePlayGameServices.PlayerScoreResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beatenScoreTimeSpans** | **[String]** | The time spans where the submitted score is better than the existing score for that time span. | [optional] 
**formattedScore** | **String** | The formatted value of the submitted score. | [optional] 
**kind** | **String** | Uniquely identifies the type of this resource. Value is always the fixed string &#x60;games#playerScoreResponse&#x60;. | [optional] 
**leaderboardId** | **String** | The leaderboard ID that this score was submitted to. | [optional] 
**scoreTag** | **String** | Additional information about this score. Values will contain no more than 64 URI-safe characters as defined by section 2.3 of RFC 3986. | [optional] 
**unbeatenScores** | [**[PlayerScore]**](PlayerScore.md) | The scores in time spans that have not been beaten. As an example, the submitted score may be better than the player&#39;s &#x60;DAILY&#x60; score, but not better than the player&#39;s scores for the &#x60;WEEKLY&#x60; or &#x60;ALL_TIME&#x60; time spans. | [optional] 



## Enum: [BeatenScoreTimeSpansEnum]


* `ALL_TIME` (value: `"ALL_TIME"`)

* `WEEKLY` (value: `"WEEKLY"`)

* `DAILY` (value: `"DAILY"`)




