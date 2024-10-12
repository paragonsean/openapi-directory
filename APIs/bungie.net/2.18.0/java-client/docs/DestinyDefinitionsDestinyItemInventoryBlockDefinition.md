

# DestinyDefinitionsDestinyItemInventoryBlockDefinition

If the item can exist in an inventory - the overwhelming majority of them can and do - then this is the basic properties regarding the item's relationship with the inventory.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bucketTypeHash** | **Integer** | The hash identifier for the DestinyInventoryBucketDefinition to which this item belongs. I should have named this \&quot;bucketHash\&quot;, but too many things refer to it now. Sigh. |  [optional] |
|**expirationTooltip** | **String** | The tooltip message to show, if any, when the item expires. |  [optional] |
|**expiredInActivityMessage** | **String** | If the item expires while playing in an activity, we show a different message. |  [optional] |
|**expiredInOrbitMessage** | **String** | If the item expires in orbit, we show a... more different message. (\&quot;Consummate V&#39;s, consummate!\&quot;) |  [optional] |
|**isInstanceItem** | **Boolean** | If TRUE, this item is instanced. Otherwise, it is a generic item that merely has a quantity in a stack (like Glimmer). |  [optional] |
|**maxStackSize** | **Integer** | The maximum quantity of this item that can exist in a stack. |  [optional] |
|**recipeItemHash** | **Integer** | A reference to the associated crafting &#39;recipe&#39; item definition, if this item can be crafted. |  [optional] |
|**recoveryBucketTypeHash** | **Integer** | If the item is picked up by the lost loot queue, this is the hash identifier for the DestinyInventoryBucketDefinition into which it will be placed. Again, I should have named this recoveryBucketHash instead. |  [optional] |
|**stackUniqueLabel** | **String** | If this string is populated, you can&#39;t have more than one stack with this label in a given inventory. Note that this is different from the equipping block&#39;s unique label, which is used for equipping uniqueness. |  [optional] |
|**suppressExpirationWhenObjectivesComplete** | **Boolean** |  |  [optional] |
|**tierType** | **Integer** | The enumeration matching the tier type of the item to known values, again for convenience sake. |  [optional] |
|**tierTypeHash** | **Integer** | The hash identifier for the Tier Type of the item, use to look up its DestinyItemTierTypeDefinition if you need to show localized data for the item&#39;s tier. |  [optional] |
|**tierTypeName** | **String** | The localized name of the tier type, which is a useful shortcut so you don&#39;t have to look up the definition every time. However, it&#39;s mostly a holdover from days before we had a DestinyItemTierTypeDefinition to refer to. |  [optional] |



