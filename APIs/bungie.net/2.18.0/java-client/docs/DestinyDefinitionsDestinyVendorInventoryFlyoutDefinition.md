

# DestinyDefinitionsDestinyVendorInventoryFlyoutDefinition

The definition for an \"inventory flyout\": a UI screen where we show you part of an otherwise hidden vendor inventory: like the Vault inventory buckets.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**buckets** | [**List&lt;DestinyDefinitionsDestinyVendorInventoryFlyoutBucketDefinition&gt;**](DestinyDefinitionsDestinyVendorInventoryFlyoutBucketDefinition.md) | A list of inventory buckets and other metadata to show on the screen. |  [optional] |
|**displayProperties** | [**DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition**](DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.md) | The title and other common properties of the flyout. |  [optional] |
|**equipmentSlotHash** | **Integer** | If this flyout is meant to show you the contents of the player&#39;s equipment slot, this is the slot to show. |  [optional] |
|**flyoutId** | **Integer** | An identifier for the flyout, in case anything else needs to refer to them. |  [optional] |
|**lockedDescription** | **String** | If the flyout is locked, this is the reason why. |  [optional] |
|**suppressNewness** | **Boolean** | If this is true, don&#39;t show any of the glistening \&quot;this is a new item\&quot; UI elements, like we show on the inventory items themselves in in-game UI. |  [optional] |



