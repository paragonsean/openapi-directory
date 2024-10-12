

# DestinyDefinitionsDestinyItemSetBlockEntryDefinition

Defines a particular entry in an ItemSet (AKA a particular Quest Step in a Quest)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**itemHash** | **Integer** | This is the hash identifier for a DestinyInventoryItemDefinition representing this quest step. |  [optional] |
|**trackingValue** | **Integer** | Used for tracking which step a user reached. These values will be populated in the user&#39;s internal state, which we expose externally as a more usable DestinyQuestStatus object. If this item has been obtained, this value will be set in trackingUnlockValueHash. |  [optional] |



