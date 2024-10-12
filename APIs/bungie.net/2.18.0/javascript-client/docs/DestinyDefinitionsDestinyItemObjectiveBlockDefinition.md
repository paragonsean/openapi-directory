# BungieNetApi.DestinyDefinitionsDestinyItemObjectiveBlockDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayActivityHashes** | **[Number]** | For every entry in objectiveHashes, there is a corresponding entry in this array at the same index. If the objective is meant to be associated with a specific DestinyActivityDefinition, there will be a valid hash at that index. Otherwise, it will be invalid (0).  Rendered somewhat obsolete by perObjectiveDisplayProperties, which currently has much the same information but may end up with more info in the future. | [optional] 
**displayAsStatTracker** | **Boolean** |  | [optional] 
**narrative** | **String** | The localized string for narrative text related to this quest step, if any. | [optional] 
**objectiveHashes** | **[Number]** | The hashes to Objectives (DestinyObjectiveDefinition) that are part of this Quest Step, in the order that they should be rendered. | [optional] 
**objectiveVerbName** | **String** | The localized string describing an action to be performed associated with the objectives, if any. | [optional] 
**perObjectiveDisplayProperties** | [**[DestinyDefinitionsDestinyObjectiveDisplayProperties]**](DestinyDefinitionsDestinyObjectiveDisplayProperties.md) | One entry per Objective on the item, it will have related display information. | [optional] 
**questTypeHash** | **Number** | A hashed value for the questTypeIdentifier, because apparently I like to be redundant. | [optional] 
**questTypeIdentifier** | **String** | The identifier for the type of quest being performed, if any. Not associated with any fixed definition, yet. | [optional] 
**questlineItemHash** | **Number** | The hash for the DestinyInventoryItemDefinition representing the Quest to which this Quest Step belongs. | [optional] 
**requireFullObjectiveCompletion** | **Boolean** | If True, all objectives must be completed for the step to be completed. If False, any one objective can be completed for the step to be completed. | [optional] 


