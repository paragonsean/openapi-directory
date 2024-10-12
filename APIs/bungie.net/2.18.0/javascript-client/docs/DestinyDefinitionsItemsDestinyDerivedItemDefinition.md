# BungieNetApi.DestinyDefinitionsItemsDestinyDerivedItemDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iconPath** | **String** | An icon for the item. | [optional] 
**itemDescription** | **String** | A brief description of the item. | [optional] 
**itemDetail** | **String** | Additional details about the derived item, in addition to the description. | [optional] 
**itemHash** | **Number** | The hash for the DestinyInventoryItemDefinition of this derived item, if there is one. Sometimes we are given this information as a manual override, in which case there won&#39;t be an actual DestinyInventoryItemDefinition for what we display, but you can still show the strings from this object itself. | [optional] 
**itemName** | **String** | The name of the derived item. | [optional] 
**vendorItemIndex** | **Number** | If the item was derived from a \&quot;Preview Vendor\&quot;, this will be an index into the DestinyVendorDefinition&#39;s itemList property. Otherwise, -1. | [optional] 


