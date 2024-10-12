# BungieNetApi.DestinyDefinitionsDestinyVendorInventoryFlyoutDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buckets** | [**[DestinyDefinitionsDestinyVendorInventoryFlyoutBucketDefinition]**](DestinyDefinitionsDestinyVendorInventoryFlyoutBucketDefinition.md) | A list of inventory buckets and other metadata to show on the screen. | [optional] 
**displayProperties** | [**DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition**](DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.md) | The title and other common properties of the flyout. | [optional] 
**equipmentSlotHash** | **Number** | If this flyout is meant to show you the contents of the player&#39;s equipment slot, this is the slot to show. | [optional] 
**flyoutId** | **Number** | An identifier for the flyout, in case anything else needs to refer to them. | [optional] 
**lockedDescription** | **String** | If the flyout is locked, this is the reason why. | [optional] 
**suppressNewness** | **Boolean** | If this is true, don&#39;t show any of the glistening \&quot;this is a new item\&quot; UI elements, like we show on the inventory items themselves in in-game UI. | [optional] 


