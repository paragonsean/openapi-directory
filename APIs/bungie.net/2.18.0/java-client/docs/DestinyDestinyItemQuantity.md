

# DestinyDestinyItemQuantity

Used in a number of Destiny contracts to return data about an item stack and its quantity. Can optionally return an itemInstanceId if the item is instanced - in which case, the quantity returned will be 1. If it's not... uh, let me know okay? Thanks.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hasConditionalVisibility** | **Boolean** | Indicates that this item quantity may be conditionally shown or hidden, based on various sources of state. For example: server flags, account state, or character progress. |  [optional] |
|**itemHash** | **Integer** | The hash identifier for the item in question. Use it to look up the item&#39;s DestinyInventoryItemDefinition. |  [optional] |
|**itemInstanceId** | **Long** | If this quantity is referring to a specific instance of an item, this will have the item&#39;s instance ID. Normally, this will be null. |  [optional] |
|**quantity** | **Integer** | The amount of the item needed/available depending on the context of where DestinyItemQuantity is being used. |  [optional] |



