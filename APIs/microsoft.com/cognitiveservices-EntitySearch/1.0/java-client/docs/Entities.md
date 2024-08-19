

# Entities

Defines an entity answer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**queryScenario** | [**QueryScenarioEnum**](#QueryScenarioEnum) | The supported query scenario. This field is set to DominantEntity or DisambiguationItem. The field is set to DominantEntity if Bing determines that only a single entity satisfies the request. For example, a book, movie, person, or attraction. If multiple entities could satisfy the request, the field is set to DisambiguationItem. For example, if the request uses the generic title of a movie franchise, the entity&#39;s type would likely be DisambiguationItem. But, if the request specifies a specific title from the franchise, the entity&#39;s type would likely be DominantEntity. |  [optional] [readonly] |
|**value** | [**List&lt;Thing&gt;**](Thing.md) | A list of entities. |  |



## Enum: QueryScenarioEnum

| Name | Value |
|---- | -----|
| DOMINANT_ENTITY | &quot;DominantEntity&quot; |
| DOMINANT_ENTITY_WITH_DISAMBIGUATION | &quot;DominantEntityWithDisambiguation&quot; |
| DISAMBIGUATION | &quot;Disambiguation&quot; |
| LIST | &quot;List&quot; |
| LIST_WITH_PIVOT | &quot;ListWithPivot&quot; |



