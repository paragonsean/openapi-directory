

# DestinyDefinitionsDestinyItemActionRequiredItemDefinition

The definition of an item and quantity required in a character's inventory in order to perform an action.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **Integer** | The minimum quantity of the item you have to have. |  [optional] |
|**deleteOnAction** | **Boolean** | If true, the item/quantity will be deleted from your inventory when the action is performed. Otherwise, you&#39;ll retain these required items after the action is complete. |  [optional] |
|**itemHash** | **Integer** | The hash identifier of the item you need to have. Use it to look up the DestinyInventoryItemDefinition for more info. |  [optional] |



