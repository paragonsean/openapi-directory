

# DestinyDefinitionsSourcesDestinyItemSourceDefinition

Properties of a DestinyInventoryItemDefinition that store all of the information we were able to discern about how the item spawns, and where you can find the item.  Items will have many of these sources, one per level at which it spawns, to try and give more granular data about where items spawn for specific level ranges.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**computedStats** | [**Map&lt;String, DestinyDefinitionsDestinyInventoryItemStatDefinition&gt;**](DestinyDefinitionsDestinyInventoryItemStatDefinition.md) | The stats computed for this level/quality range. |  [optional] |
|**level** | **Integer** | The level at which the item spawns. Essentially the Primary Key for this source data: there will be multiple of these source entries per item that has source data, grouped by the level at which the item spawns. |  [optional] |
|**maxLevelRequired** | **Integer** | The maximum Character Level required for equipping the item when the item spawns at the item level defined on this DestinyItemSourceDefinition, as far as we saw in our processing. |  [optional] |
|**maxQuality** | **Integer** | The maximum quality at which the item spawns for this level. |  [optional] |
|**minLevelRequired** | **Integer** | The minimum Character Level required for equipping the item when the item spawns at the item level defined on this DestinyItemSourceDefinition, as far as we saw in our processing. |  [optional] |
|**minQuality** | **Integer** | The minimum Quality at which the item spawns for this level. Examine DestinyInventoryItemDefinition for more information about what Quality means. Just don&#39;t ask Phaedrus about it, he&#39;ll never stop talking and you&#39;ll have to write a book about it. |  [optional] |
|**sourceHashes** | **List&lt;Integer&gt;** | The DestinyRewardSourceDefinitions found that can spawn the item at this level. |  [optional] |



