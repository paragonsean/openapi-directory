

# PlayerScore

A player score.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**formattedScore** | **String** | The formatted score for this player score. |  [optional] |
|**kind** | **String** | Uniquely identifies the type of this resource. Value is always the fixed string &#x60;games#playerScore&#x60;. |  [optional] |
|**score** | **String** | The numerical value for this player score. |  [optional] |
|**scoreTag** | **String** | Additional information about this score. Values will contain no more than 64 URI-safe characters as defined by section 2.3 of RFC 3986. |  [optional] |
|**timeSpan** | [**TimeSpanEnum**](#TimeSpanEnum) | The time span for this player score. |  [optional] |



## Enum: TimeSpanEnum

| Name | Value |
|---- | -----|
| ALL_TIME | &quot;ALL_TIME&quot; |
| WEEKLY | &quot;WEEKLY&quot; |
| DAILY | &quot;DAILY&quot; |



