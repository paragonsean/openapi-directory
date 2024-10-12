# Nookipedia.NHClothing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability** | [**[NHClothingAvailabilityInner]**](NHClothingAvailabilityInner.md) | Where the clothing may be obtained from (could be multiple sources). &#x60;from&#x60; is a brief description of the source; &#x60;note&#x60;, when provided, provides additional details. | [optional] 
**buy** | [**[NHClothingBuyInner]**](NHClothingBuyInner.md) | An array of prices, for when the item may be purchased with Bells, Nook Miles, etc.. | [optional] 
**category** | **String** | The category of item as shown in the player&#39;s inventory. | [optional] 
**labelThemes** | **[String]** | The clothing&#39;s Label theme(s). This is used for completing the requested outfit theme for [Label](https://nookipedia.com/wiki/Label) when she visits the player&#39;s island. | [optional] 
**name** | **String** | The name of the clothing. | [optional] 
**notes** | **String** | Any additional miscellaneous information about the clothing, such as a name change from a past update. | [optional] 
**seasonality** | **String** | The time of the year that the clothing is available. | [optional] 
**sell** | **Number** | The number of Bells the clothing can be sold to the store for. | [optional] 
**styles** | **[String]** | The clothing&#39;s style(s). Styles are used for gifting villagers. | [optional] 
**unlocked** | **Boolean** | Whether the item is available through legitimate gameplay. Some items are added to the game files in an update, but aren&#39;t actually made available until a subsequent update unlocks them. | [optional] 
**url** | **String** | Link to the respective Nookipedia article. | [optional] 
**variationTotal** | **Number** | The total number of variations the clothing has, between 0 and 8. | [optional] 
**variations** | [**[NHClothingVariationsInner]**](NHClothingVariationsInner.md) | An array of objects, each object representing a variation of the clothing. Clothing that has no variations (only one version) will have a single variation object with the image URL and colors, but the &#x60;variation&#x60; field will be empty. Clothing with multiple variations will have the &#x60;variation&#x60; fields defined with the name of each variation. | [optional] 
**versionAdded** | **String** | The version of *New Horizons* that the item was added. Items that were included at the game&#39;s launch have version \&quot;1.0.0\&quot;. | [optional] 
**villEquip** | **Boolean** | Whether villagers may equip this item. | [optional] 



## Enum: CategoryEnum


* `Tops` (value: `"Tops"`)

* `Bottoms` (value: `"Bottoms"`)

* `Dress-up` (value: `"Dress-up"`)

* `Headwear` (value: `"Headwear"`)

* `Accessories` (value: `"Accessories"`)

* `Socks` (value: `"Socks"`)

* `Shoes` (value: `"Shoes"`)

* `Bags` (value: `"Bags"`)

* `Umbrellas` (value: `"Umbrellas"`)





## Enum: [LabelThemesEnum]


* `Comfy` (value: `"Comfy"`)

* `Everyday` (value: `"Everyday"`)

* `Fairy tale` (value: `"Fairy tale"`)

* `Formal` (value: `"Formal"`)

* `Goth` (value: `"Goth"`)

* `Outdoorsy` (value: `"Outdoorsy"`)

* `Party` (value: `"Party"`)

* `Sporty` (value: `"Sporty"`)

* `Theatrical` (value: `"Theatrical"`)

* `Vacation` (value: `"Vacation"`)

* `Work` (value: `"Work"`)





## Enum: [StylesEnum]


* `Active` (value: `"Active"`)

* `Cool` (value: `"Cool"`)

* `Cute` (value: `"Cute"`)

* `Elegant` (value: `"Elegant"`)

* `Gorgeous` (value: `"Gorgeous"`)

* `Simple` (value: `"Simple"`)





## Enum: VariationTotalEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)

* `4` (value: `4`)

* `5` (value: `5`)

* `6` (value: `6`)

* `7` (value: `7`)

* `8` (value: `8`)




