

# DestinyDefinitionsDestinyMaterialRequirementSetDefinition

Represent a set of material requirements: Items that either need to be owned or need to be consumed in order to perform an action.  A variety of other entities refer to these as gatekeepers and payments for actions that can be performed in game.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hash** | **Integer** | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to. |  [optional] |
|**index** | **Integer** | The index of the entity as it was found in the investment tables. |  [optional] |
|**materials** | [**List&lt;DestinyDefinitionsDestinyMaterialRequirement&gt;**](DestinyDefinitionsDestinyMaterialRequirement.md) | The list of all materials that are required. |  [optional] |
|**redacted** | **Boolean** | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! |  [optional] |



