# BungieNetApi.DestinyDefinitionsMilestonesDestinyMilestoneQuestRewardItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hasConditionalVisibility** | **Boolean** | Indicates that this item quantity may be conditionally shown or hidden, based on various sources of state. For example: server flags, account state, or character progress. | [optional] 
**itemHash** | **Number** | The hash identifier for the item in question. Use it to look up the item&#39;s DestinyInventoryItemDefinition. | [optional] 
**itemInstanceId** | **Number** | If this quantity is referring to a specific instance of an item, this will have the item&#39;s instance ID. Normally, this will be null. | [optional] 
**quantity** | **Number** | The amount of the item needed/available depending on the context of where DestinyItemQuantity is being used. | [optional] 
**vendorHash** | **Number** | The quest reward item *may* be associated with a vendor. If so, this is that vendor. Use this hash to look up the DestinyVendorDefinition. | [optional] 
**vendorItemIndex** | **Number** | The quest reward item *may* be associated with a vendor. If so, this is the index of the item being sold, which we can use at runtime to find instanced item information for the reward item. | [optional] 


