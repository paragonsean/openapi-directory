# BungieNetApi.DestinyDefinitionsDestinyProgressionDisplayPropertiesDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** |  | [optional] 
**displayUnitsName** | **String** | When progressions show your \&quot;experience\&quot; gained, that bar has units (i.e. \&quot;Experience\&quot;, \&quot;Bad Dudes Snuffed Out\&quot;, whatever). This is the localized string for that unit of measurement. | [optional] 
**hasIcon** | **Boolean** |  | [optional] 
**highResIcon** | **String** | If this item has a high-res icon (at least for now, many things won&#39;t), then the path to that icon will be here. | [optional] 
**icon** | **String** | Note that \&quot;icon\&quot; is sometimes misleading, and should be interpreted in the context of the entity. For instance, in Destiny 1 the DestinyRecordBookDefinition&#39;s icon was a big picture of a book.  But usually, it will be a small square image that you can use as... well, an icon.  They are currently represented as 96px x 96px images. | [optional] 
**iconSequences** | [**[DestinyDefinitionsCommonDestinyIconSequenceDefinition]**](DestinyDefinitionsCommonDestinyIconSequenceDefinition.md) |  | [optional] 
**name** | **String** |  | [optional] 


