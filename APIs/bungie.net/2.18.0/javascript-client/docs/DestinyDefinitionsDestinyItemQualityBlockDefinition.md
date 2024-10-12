# BungieNetApi.DestinyDefinitionsDestinyItemQualityBlockDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currentVersion** | **Number** | The latest version available for this item. | [optional] 
**displayVersionWatermarkIcons** | **[String]** | Icon overlays to denote the item version and power cap status. | [optional] 
**infusionCategoryHash** | **Number** | The hash identifier for the infusion. It does not map to a Definition entity.  DEPRECATED: Items can now have multiple infusion categories. Please use infusionCategoryHashes instead. | [optional] 
**infusionCategoryHashes** | **[Number]** | If any one of these hashes matches any value in another item&#39;s infusionCategoryHashes, the two can infuse with each other. | [optional] 
**infusionCategoryName** | **String** | The string identifier for this item&#39;s \&quot;infusability\&quot;, if any.   Items that match the same infusionCategoryName are allowed to infuse with each other.  DEPRECATED: Items can now have multiple infusion categories. Please use infusionCategoryHashes instead. | [optional] 
**itemLevels** | **[Number]** | The \&quot;base\&quot; defined level of an item. This is a list because, in theory, each Expansion could define its own base level for an item.  In practice, not only was that never done in Destiny 1, but now this isn&#39;t even populated at all. When it&#39;s not populated, the level at which it spawns has to be inferred by Reward information, of which BNet receives an imperfect view and will only be reliable on instanced data as a result. | [optional] 
**progressionLevelRequirementHash** | **Number** | An item can refer to pre-set level requirements. They are defined in DestinyProgressionLevelRequirementDefinition, and you can use this hash to find the appropriate definition. | [optional] 
**qualityLevel** | **Number** | qualityLevel is used in combination with the item&#39;s level to calculate stats like Attack and Defense. It plays a role in that calculation, but not nearly as large as itemLevel does. | [optional] 
**versions** | [**[DestinyDefinitionsDestinyItemVersionDefinition]**](DestinyDefinitionsDestinyItemVersionDefinition.md) | The list of versions available for this item. | [optional] 


