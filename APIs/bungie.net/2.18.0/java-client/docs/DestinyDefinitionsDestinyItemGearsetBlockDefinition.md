

# DestinyDefinitionsDestinyItemGearsetBlockDefinition

If an item has a related gearset, this is the list of items in that set, and an unlock expression that evaluates to a number representing the progress toward gearset completion (a very rare use for unlock expressions!)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**itemList** | **List&lt;Integer&gt;** | The list of hashes for items in the gearset. Use them to look up DestinyInventoryItemDefinition entries for the items in the set. |  [optional] |
|**trackingValueMax** | **Integer** | The maximum possible number of items that can be collected. |  [optional] |



