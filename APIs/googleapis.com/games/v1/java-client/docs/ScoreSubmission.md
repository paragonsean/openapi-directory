

# ScoreSubmission

A request to submit a score to leaderboards.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kind** | **String** | Uniquely identifies the type of this resource. Value is always the fixed string &#x60;games#scoreSubmission&#x60;. |  [optional] |
|**leaderboardId** | **String** | The leaderboard this score is being submitted to. |  [optional] |
|**score** | **String** | The new score being submitted. |  [optional] |
|**scoreTag** | **String** | Additional information about this score. Values will contain no more than 64 URI-safe characters as defined by section 2.3 of RFC 3986. |  [optional] |
|**signature** | **String** | Signature Values will contain URI-safe characters as defined by section 2.3 of RFC 3986. |  [optional] |



