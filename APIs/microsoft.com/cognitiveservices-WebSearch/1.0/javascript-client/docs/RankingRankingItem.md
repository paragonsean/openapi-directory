# WebSearchClient.RankingRankingItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answerType** | **String** | The answer that contains the item to display. Use the type to find the answer in the SearchResponse object. The type is the name of a SearchResponse field. | [default to &#39;WebPages&#39;]
**htmlIndex** | **Number** |  | [optional] [readonly] 
**resultIndex** | **Number** | A zero-based index of the item in the answer.If the item does not include this field, display all items in the answer. For example, display all news articles in the News answer. | [optional] [readonly] 
**screenshotIndex** | **Number** |  | [optional] [readonly] 
**textualIndex** | **Number** |  | [optional] [readonly] 
**value** | [**Identifiable**](Identifiable.md) |  | [optional] 



## Enum: AnswerTypeEnum


* `WebPages` (value: `"WebPages"`)

* `Images` (value: `"Images"`)

* `SpellSuggestions` (value: `"SpellSuggestions"`)

* `News` (value: `"News"`)

* `RelatedSearches` (value: `"RelatedSearches"`)

* `Videos` (value: `"Videos"`)

* `Computation` (value: `"Computation"`)

* `TimeZone` (value: `"TimeZone"`)




