# EntitySearchClient.Entities

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queryScenario** | **String** | The supported query scenario. This field is set to DominantEntity or DisambiguationItem. The field is set to DominantEntity if Bing determines that only a single entity satisfies the request. For example, a book, movie, person, or attraction. If multiple entities could satisfy the request, the field is set to DisambiguationItem. For example, if the request uses the generic title of a movie franchise, the entity&#39;s type would likely be DisambiguationItem. But, if the request specifies a specific title from the franchise, the entity&#39;s type would likely be DominantEntity. | [optional] [readonly] [default to &#39;DominantEntity&#39;]
**value** | [**[Thing]**](Thing.md) | A list of entities. | 



## Enum: QueryScenarioEnum


* `DominantEntity` (value: `"DominantEntity"`)

* `DominantEntityWithDisambiguation` (value: `"DominantEntityWithDisambiguation"`)

* `Disambiguation` (value: `"Disambiguation"`)

* `List` (value: `"List"`)

* `ListWithPivot` (value: `"ListWithPivot"`)




