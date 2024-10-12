

# EntitiesEntityPresentationInfo

Defines additional information about an entity such as type hints.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | **String** |  |  |
|**entityScenario** | [**EntityScenarioEnum**](#EntityScenarioEnum) | The supported scenario. |  |
|**entitySubTypeHints** | **List&lt;String&gt;** |  |  [optional] [readonly] |
|**entityTypeDisplayHint** | **String** | A display version of the entity hint. For example, if entityTypeHints is Artist, this field may be set to American Singer. |  [optional] [readonly] |
|**entityTypeHints** | [**List&lt;EntityTypeHintsEnum&gt;**](#List&lt;EntityTypeHintsEnum&gt;) | A list of hints that indicate the entity&#39;s type. The list could contain a single hint such as Movie or a list of hints such as Place, LocalBusiness, Restaurant. Each successive hint in the array narrows the entity&#39;s type. |  [optional] [readonly] |
|**query** | **String** |  |  [optional] [readonly] |



## Enum: EntityScenarioEnum

| Name | Value |
|---- | -----|
| DOMINANT_ENTITY | &quot;DominantEntity&quot; |
| DISAMBIGUATION_ITEM | &quot;DisambiguationItem&quot; |
| LIST_ITEM | &quot;ListItem&quot; |



## Enum: List&lt;EntityTypeHintsEnum&gt;

| Name | Value |
|---- | -----|
| PLACE | &quot;Place&quot; |
| LOCAL_BUSINESS | &quot;LocalBusiness&quot; |
| RESTAURANT | &quot;Restaurant&quot; |
| HOTEL | &quot;Hotel&quot; |



