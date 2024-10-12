# BungieNetApi.DestinyDefinitionsRecordsDestinyRecordDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completionInfo** | [**DestinyDefinitionsRecordsDestinyRecordCompletionBlock**](DestinyDefinitionsRecordsDestinyRecordCompletionBlock.md) |  | [optional] 
**displayProperties** | [**DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition**](DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.md) |  | [optional] 
**expirationInfo** | [**DestinyDefinitionsRecordsDestinyRecordExpirationBlock**](DestinyDefinitionsRecordsDestinyRecordExpirationBlock.md) |  | [optional] 
**forTitleGilding** | **Boolean** |  | [optional] 
**hash** | **Number** | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to. | [optional] 
**index** | **Number** | The index of the entity as it was found in the investment tables. | [optional] 
**intervalInfo** | [**DestinyDefinitionsRecordsDestinyRecordIntervalBlock**](DestinyDefinitionsRecordsDestinyRecordIntervalBlock.md) | Some records have multiple &#39;interval&#39; objectives, and the record may be claimed at each completed interval | [optional] 
**loreHash** | **Number** |  | [optional] 
**objectiveHashes** | **[Number]** |  | [optional] 
**parentNodeHashes** | **[Number]** | A quick reference to presentation nodes that have this node as a child. Presentation nodes can be parented under multiple parents. | [optional] 
**presentationInfo** | [**DestinyDefinitionsPresentationDestinyPresentationChildBlock**](DestinyDefinitionsPresentationDestinyPresentationChildBlock.md) |  | [optional] 
**presentationNodeType** | **Number** |  | [optional] 
**recordValueStyle** | **Number** |  | [optional] 
**redacted** | **Boolean** | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | [optional] 
**requirements** | [**DestinyDefinitionsPresentationDestinyPresentationNodeRequirementsBlock**](DestinyDefinitionsPresentationDestinyPresentationNodeRequirementsBlock.md) |  | [optional] 
**rewardItems** | [**[DestinyDestinyItemQuantity]**](DestinyDestinyItemQuantity.md) | If there is any publicly available information about rewards earned for achieving this record, this is the list of those items.   However, note that some records intentionally have \&quot;hidden\&quot; rewards. These will not be returned in this list. | [optional] 
**scope** | **Number** | Indicates whether this Record&#39;s state is determined on a per-character or on an account-wide basis. | [optional] 
**shouldShowLargeIcons** | **Boolean** | A hint to show a large icon for a reward | [optional] 
**stateInfo** | [**DestinyDefinitionsRecordsSchemaRecordStateBlock**](DestinyDefinitionsRecordsSchemaRecordStateBlock.md) |  | [optional] 
**titleInfo** | [**DestinyDefinitionsRecordsDestinyRecordTitleBlock**](DestinyDefinitionsRecordsDestinyRecordTitleBlock.md) |  | [optional] 
**traitHashes** | **[Number]** |  | [optional] 
**traitIds** | **[String]** |  | [optional] 


