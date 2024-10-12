# BungieNetApi.DestinyDefinitionsDestinyRewardSourceDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **Number** | Sources are grouped into categories: common ways that items are provided. I hope to see this expand in Destiny 2 once we have time to generate accurate reward source data. | [optional] 
**displayProperties** | [**DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition**](DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.md) |  | [optional] 
**hash** | **Number** | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to. | [optional] 
**index** | **Number** | The index of the entity as it was found in the investment tables. | [optional] 
**redacted** | **Boolean** | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | [optional] 


