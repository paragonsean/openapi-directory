# DiscoveryEngineApi.GoogleCloudDiscoveryengineV1betaSuggestionDenyListEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockPhrase** | **String** | Required. Phrase to block from suggestions served. Can be maximum 125 characters. | [optional] 
**matchOperator** | **String** | Required. The match operator to apply for this phrase. Whether to block the exact phrase, or block any suggestions containing this phrase. | [optional] 



## Enum: MatchOperatorEnum


* `MATCH_OPERATOR_UNSPECIFIED` (value: `"MATCH_OPERATOR_UNSPECIFIED"`)

* `EXACT_MATCH` (value: `"EXACT_MATCH"`)

* `CONTAINS` (value: `"CONTAINS"`)




