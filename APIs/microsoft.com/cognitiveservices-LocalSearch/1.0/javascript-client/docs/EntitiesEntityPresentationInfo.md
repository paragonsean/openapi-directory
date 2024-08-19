# LocalSearchClient.EntitiesEntityPresentationInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **String** |  | 
**entityScenario** | **String** | The supported scenario. | [default to &#39;DominantEntity&#39;]
**entitySubTypeHints** | **[String]** |  | [optional] [readonly] 
**entityTypeDisplayHint** | **String** | A display version of the entity hint. For example, if entityTypeHints is Artist, this field may be set to American Singer. | [optional] [readonly] 
**entityTypeHints** | **[String]** | A list of hints that indicate the entity&#39;s type. The list could contain a single hint such as Movie or a list of hints such as Place, LocalBusiness, Restaurant. Each successive hint in the array narrows the entity&#39;s type. | [optional] [readonly] 
**query** | **String** |  | [optional] [readonly] 



## Enum: EntityScenarioEnum


* `DominantEntity` (value: `"DominantEntity"`)

* `DisambiguationItem` (value: `"DisambiguationItem"`)

* `ListItem` (value: `"ListItem"`)





## Enum: [EntityTypeHintsEnum]


* `Place` (value: `"Place"`)

* `LocalBusiness` (value: `"LocalBusiness"`)

* `Restaurant` (value: `"Restaurant"`)

* `Hotel` (value: `"Hotel"`)




