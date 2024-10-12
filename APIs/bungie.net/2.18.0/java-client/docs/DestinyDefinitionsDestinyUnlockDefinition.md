

# DestinyDefinitionsDestinyUnlockDefinition

Unlock Flags are small bits (literally, a bit, as in a boolean value) that the game server uses for an extremely wide range of state checks, progress storage, and other interesting tidbits of information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayProperties** | [**DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition**](DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.md) | Sometimes, but not frequently, these unlock flags also have human readable information: usually when they are being directly tested for some requirement, in which case the string is a localized description of why the requirement check failed. |  [optional] |
|**hash** | **Integer** | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to. |  [optional] |
|**index** | **Integer** | The index of the entity as it was found in the investment tables. |  [optional] |
|**redacted** | **Boolean** | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! |  [optional] |



