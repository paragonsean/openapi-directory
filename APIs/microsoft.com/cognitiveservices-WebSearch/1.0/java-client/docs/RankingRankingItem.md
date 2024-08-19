

# RankingRankingItem

Defines a search result item to display

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**answerType** | [**AnswerTypeEnum**](#AnswerTypeEnum) | The answer that contains the item to display. Use the type to find the answer in the SearchResponse object. The type is the name of a SearchResponse field. |  |
|**htmlIndex** | **Integer** |  |  [optional] [readonly] |
|**resultIndex** | **Integer** | A zero-based index of the item in the answer.If the item does not include this field, display all items in the answer. For example, display all news articles in the News answer. |  [optional] [readonly] |
|**screenshotIndex** | **Integer** |  |  [optional] [readonly] |
|**textualIndex** | **Integer** |  |  [optional] [readonly] |
|**value** | [**Identifiable**](Identifiable.md) |  |  [optional] |



## Enum: AnswerTypeEnum

| Name | Value |
|---- | -----|
| WEB_PAGES | &quot;WebPages&quot; |
| IMAGES | &quot;Images&quot; |
| SPELL_SUGGESTIONS | &quot;SpellSuggestions&quot; |
| NEWS | &quot;News&quot; |
| RELATED_SEARCHES | &quot;RelatedSearches&quot; |
| VIDEOS | &quot;Videos&quot; |
| COMPUTATION | &quot;Computation&quot; |
| TIME_ZONE | &quot;TimeZone&quot; |



