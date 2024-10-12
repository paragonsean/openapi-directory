

# GoogleCloudContactcenterinsightsV1CalculateStatsResponse

The response for calculating conversation statistics.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**averageDuration** | **String** | The average duration of all conversations. The average is calculated using only conversations that have a time duration. |  [optional] |
|**averageTurnCount** | **Integer** | The average number of turns per conversation. |  [optional] |
|**conversationCount** | **Integer** | The total number of conversations. |  [optional] |
|**conversationCountTimeSeries** | [**GoogleCloudContactcenterinsightsV1CalculateStatsResponseTimeSeries**](GoogleCloudContactcenterinsightsV1CalculateStatsResponseTimeSeries.md) |  |  [optional] |
|**customHighlighterMatches** | **Map&lt;String, Integer&gt;** | A map associating each custom highlighter resource name with its respective number of matches in the set of conversations. |  [optional] |
|**issueMatches** | **Map&lt;String, Integer&gt;** | A map associating each issue resource name with its respective number of matches in the set of conversations. Key has the format: &#x60;projects//locations//issueModels//issues/&#x60; Deprecated, use &#x60;issue_matches_stats&#x60; field instead. |  [optional] |
|**issueMatchesStats** | [**Map&lt;String, GoogleCloudContactcenterinsightsV1IssueModelLabelStatsIssueStats&gt;**](GoogleCloudContactcenterinsightsV1IssueModelLabelStatsIssueStats.md) | A map associating each issue resource name with its respective number of matches in the set of conversations. Key has the format: &#x60;projects//locations//issueModels//issues/&#x60; |  [optional] |
|**smartHighlighterMatches** | **Map&lt;String, Integer&gt;** | A map associating each smart highlighter display name with its respective number of matches in the set of conversations. |  [optional] |



