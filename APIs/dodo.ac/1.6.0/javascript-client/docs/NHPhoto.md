# Nookipedia.NHPhoto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability** | [**[NHClothingAvailabilityInner]**](NHClothingAvailabilityInner.md) | Where the photo may be obtained from (could be multiple sources). &#x60;from&#x60; is a brief description of the source; &#x60;note&#x60;, when provided, provides additional details. | [optional] 
**buy** | [**[NHClothingBuyInner]**](NHClothingBuyInner.md) | An array of prices, for when the item may be purchased with Bells, Nook Miles, etc.. | [optional] 
**category** | **String** | The category of item as shown in the player&#39;s inventory. | [optional] 
**customBodyPart** | **String** | If the item has variations, this is the name of the furniture part that changes. For example, for many bamboo items, the custom body part is \&quot;Bamboo\&quot; as the bamboo color is able to be customized. | [optional] 
**customKits** | **Number** | The number of &#x60;custom_kit_type&#x60;s (e.g. Customization Kits) that are needed to customize this item. Value is 0 if the item is not customizable. | [optional] 
**customizable** | **Boolean** | Whether or not the item is customizable via a crafting table. | [optional] 
**gridLength** | **Number** | The number of lengthwise grid spaces this item takes up. | [optional] 
**gridWidth** | **Number** | The number of widthwise grid spaces this item takes up. | [optional] 
**interactable** | **Boolean** | Whether or not the item can be interacted with. This field is true for all photos and false for all posters. | [optional] 
**name** | **String** | The name of the photo. | [optional] 
**sell** | **Number** | The number of Bells the photo can be sold to the store for. | [optional] 
**unlocked** | **Boolean** | Whether the item is available through legitimate gameplay. Some items are added to the game files in an update, but aren&#39;t actually made available until a subsequent update unlocks them. | [optional] 
**url** | **String** | Link to the respective Nookipedia article. | [optional] 
**variations** | [**[NHClothingVariationsInner]**](NHClothingVariationsInner.md) | An array of objects, each object representing a variation of the photo or poster. Items that has no variations (only one version) will have a single variation object with the image URL and colors, but the &#x60;variation&#x60; field will be empty. Items with multiple variations will have the &#x60;variation&#x60; fields defined with the name of each variation. | [optional] 
**versionAdded** | **String** | The version of *New Horizons* that the item was added. Items that were included at the game&#39;s launch have version \&quot;1.0.0\&quot;. | [optional] 



## Enum: CategoryEnum


* `Photos` (value: `"Photos"`)

* `Posters` (value: `"Posters"`)




