

# SpellResult


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**suggestedQuery** | **String** | The suggested spelling of the query. |  [optional] |
|**suggestedQueryHtml** | [**SafeHtmlProto**](SafeHtmlProto.md) |  |  [optional] |
|**suggestionType** | [**SuggestionTypeEnum**](#SuggestionTypeEnum) | Suggestion triggered for the current query. |  [optional] |



## Enum: SuggestionTypeEnum

| Name | Value |
|---- | -----|
| SUGGESTION_TYPE_UNSPECIFIED | &quot;SUGGESTION_TYPE_UNSPECIFIED&quot; |
| NON_EMPTY_RESULTS_SPELL_SUGGESTION | &quot;NON_EMPTY_RESULTS_SPELL_SUGGESTION&quot; |
| ZERO_RESULTS_FULL_PAGE_REPLACEMENT | &quot;ZERO_RESULTS_FULL_PAGE_REPLACEMENT&quot; |



