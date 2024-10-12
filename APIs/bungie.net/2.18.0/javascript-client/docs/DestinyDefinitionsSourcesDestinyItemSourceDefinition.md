# BungieNetApi.DestinyDefinitionsSourcesDestinyItemSourceDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**computedStats** | [**{String: DestinyDefinitionsDestinyInventoryItemStatDefinition}**](DestinyDefinitionsDestinyInventoryItemStatDefinition.md) | The stats computed for this level/quality range. | [optional] 
**level** | **Number** | The level at which the item spawns. Essentially the Primary Key for this source data: there will be multiple of these source entries per item that has source data, grouped by the level at which the item spawns. | [optional] 
**maxLevelRequired** | **Number** | The maximum Character Level required for equipping the item when the item spawns at the item level defined on this DestinyItemSourceDefinition, as far as we saw in our processing. | [optional] 
**maxQuality** | **Number** | The maximum quality at which the item spawns for this level. | [optional] 
**minLevelRequired** | **Number** | The minimum Character Level required for equipping the item when the item spawns at the item level defined on this DestinyItemSourceDefinition, as far as we saw in our processing. | [optional] 
**minQuality** | **Number** | The minimum Quality at which the item spawns for this level. Examine DestinyInventoryItemDefinition for more information about what Quality means. Just don&#39;t ask Phaedrus about it, he&#39;ll never stop talking and you&#39;ll have to write a book about it. | [optional] 
**sourceHashes** | **[Number]** | The DestinyRewardSourceDefinitions found that can spawn the item at this level. | [optional] 


