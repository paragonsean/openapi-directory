

# GoogleCloudDiscoveryengineV1betaSuggestionDenyListEntry

Suggestion deny list entry identifying the phrase to block from suggestions and the applied operation for the phrase.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blockPhrase** | **String** | Required. Phrase to block from suggestions served. Can be maximum 125 characters. |  [optional] |
|**matchOperator** | [**MatchOperatorEnum**](#MatchOperatorEnum) | Required. The match operator to apply for this phrase. Whether to block the exact phrase, or block any suggestions containing this phrase. |  [optional] |



## Enum: MatchOperatorEnum

| Name | Value |
|---- | -----|
| MATCH_OPERATOR_UNSPECIFIED | &quot;MATCH_OPERATOR_UNSPECIFIED&quot; |
| EXACT_MATCH | &quot;EXACT_MATCH&quot; |
| CONTAINS | &quot;CONTAINS&quot; |



