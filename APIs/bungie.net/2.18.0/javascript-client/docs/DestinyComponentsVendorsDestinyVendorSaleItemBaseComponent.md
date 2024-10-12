# BungieNetApi.DestinyComponentsVendorsDestinyVendorSaleItemBaseComponent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiPurchasable** | **Boolean** | If true, this item can be purchased through the Bungie.net API. | [optional] 
**costs** | [**[DestinyDestinyItemQuantity]**](DestinyDestinyItemQuantity.md) | A summary of the current costs of the item. | [optional] 
**itemHash** | **Number** | The hash of the item being sold, as a quick shortcut for looking up the DestinyInventoryItemDefinition of the sale item. | [optional] 
**overrideNextRefreshDate** | **Date** | If this item has its own custom date where it may be removed from the Vendor&#39;s rotation, this is that date.  Note that there&#39;s not actually any guarantee that it will go away: it could be chosen again and end up still being in the Vendor&#39;s sale items! But this is the next date where that test will occur, and is also the date that the game shows for availability on things like Bounties being sold. So it&#39;s the best we can give. | [optional] 
**overrideStyleItemHash** | **Number** | If populated, this is the hash of the item whose icon (and other secondary styles, but *not* the human readable strings) should override whatever icons/styles are on the item being sold.  If you don&#39;t do this, certain items whose styles are being overridden by socketed items - such as the \&quot;Recycle Shader\&quot; item - would show whatever their default icon/style is, and it wouldn&#39;t be pretty or look accurate. | [optional] 
**quantity** | **Number** | How much of the item you&#39;ll be getting. | [optional] 
**vendorItemIndex** | **Number** | The index into the DestinyVendorDefinition.itemList property. Note that this means Vendor data *is* Content Version dependent: make sure you have the latest content before you use Vendor data, or these indexes may mismatch.   Most systems avoid this problem, but Vendors is one area where we are unable to reasonably avoid content dependency at the moment. | [optional] 


