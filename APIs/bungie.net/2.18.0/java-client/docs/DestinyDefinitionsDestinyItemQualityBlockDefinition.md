

# DestinyDefinitionsDestinyItemQualityBlockDefinition

An item's \"Quality\" determines its calculated stats. The Level at which the item spawns is combined with its \"qualityLevel\" along with some additional calculations to determine the value of those stats.  In Destiny 2, most items don't have default item levels and quality, making this property less useful: these apparently are almost always determined by the complex mechanisms of the Reward system rather than statically. They are still provided here in case they are still useful for people. This also contains some information about Infusion.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentVersion** | **Integer** | The latest version available for this item. |  [optional] |
|**displayVersionWatermarkIcons** | **List&lt;String&gt;** | Icon overlays to denote the item version and power cap status. |  [optional] |
|**infusionCategoryHash** | **Integer** | The hash identifier for the infusion. It does not map to a Definition entity.  DEPRECATED: Items can now have multiple infusion categories. Please use infusionCategoryHashes instead. |  [optional] |
|**infusionCategoryHashes** | **List&lt;Integer&gt;** | If any one of these hashes matches any value in another item&#39;s infusionCategoryHashes, the two can infuse with each other. |  [optional] |
|**infusionCategoryName** | **String** | The string identifier for this item&#39;s \&quot;infusability\&quot;, if any.   Items that match the same infusionCategoryName are allowed to infuse with each other.  DEPRECATED: Items can now have multiple infusion categories. Please use infusionCategoryHashes instead. |  [optional] |
|**itemLevels** | **List&lt;Integer&gt;** | The \&quot;base\&quot; defined level of an item. This is a list because, in theory, each Expansion could define its own base level for an item.  In practice, not only was that never done in Destiny 1, but now this isn&#39;t even populated at all. When it&#39;s not populated, the level at which it spawns has to be inferred by Reward information, of which BNet receives an imperfect view and will only be reliable on instanced data as a result. |  [optional] |
|**progressionLevelRequirementHash** | **Integer** | An item can refer to pre-set level requirements. They are defined in DestinyProgressionLevelRequirementDefinition, and you can use this hash to find the appropriate definition. |  [optional] |
|**qualityLevel** | **Integer** | qualityLevel is used in combination with the item&#39;s level to calculate stats like Attack and Defense. It plays a role in that calculation, but not nearly as large as itemLevel does. |  [optional] |
|**versions** | [**List&lt;DestinyDefinitionsDestinyItemVersionDefinition&gt;**](DestinyDefinitionsDestinyItemVersionDefinition.md) | The list of versions available for this item. |  [optional] |



