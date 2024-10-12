# Nookipedia.NHFurniture

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability** | [**[NHClothingAvailabilityInner]**](NHClothingAvailabilityInner.md) | Where the furniture may be obtained from (could be multiple sources). &#x60;from&#x60; is a brief description of the source; &#x60;note&#x60;, when provided, provides additional details. | [optional] 
**buy** | [**[NHClothingBuyInner]**](NHClothingBuyInner.md) | An array of prices, for when the item may be purchased with Bells, Nook Miles, etc.. | [optional] 
**category** | **String** | The category of item as shown in the player&#39;s inventory. | [optional] 
**customBodyPart** | **String** | If the item has variations, this is the name of the furniture part that changes. For example, for many bamboo items, the custom body part is \&quot;Bamboo\&quot; as the bamboo color is able to be customized. | [optional] 
**customKitType** | **String** | The item that needs to be consumed to customize this item. The vast majority are \&quot;Customization Kit\&quot;, but a small selection of items will require a different item, such as items in the Spooky Series requireing pumpkins. | [optional] 
**customKits** | **Number** | The number of &#x60;custom_kit_type&#x60;s (e.g. Customization Kits) that are needed to customize this item. Value is 0 if the item is not customizable. | [optional] 
**customPatternPart** | **String** | If the item&#39;s pattern can be customized, this is the name of the furniture part that can have a pattern applied to it. For example, for the Baby Chair, the custom pattern part is \&quot;Cushion\&quot; as the cushion on the chair may have a pattern applied. | [optional] 
**customizable** | **Boolean** | Whether or not the item is customizable via a crafting table. | [optional] 
**doorDecor** | **Boolean** | Whether this item may be placed on the exterior door of the player&#39;s house. | [optional] 
**functions** | **[String]** | A list of functionalities (if any) that the item has. For example, furniture that items can be placed on topof will have \&quot;Table\&quot; as a function.. | [optional] 
**gridLength** | **Number** | The number of lengthwise grid spaces this item takes up. | [optional] 
**gridWidth** | **Number** | The number of widthwise grid spaces this item takes up. | [optional] 
**height** | **Number** | The height of the object. One in-game block is 10 units tall, while the player is 15.1324 units tall. | [optional] 
**hhaBase** | **Number** | The base value that the item provides to a player&#39;s Happy Home Academy score when placed in their home. | [optional] 
**hhaCategory** | **String** | The HHA category the item is a part of, if any. If the item does not have an HHA category, this will be an empty string. | [optional] 
**itemSeries** | **String** | The [furniture series](https://nookipedia.com/wiki/Series_(furniture)) the item is a part of, if any. A series is a collection of furniture and interior items, all with the same theme. If the item is not part of a series, this will be an empty string. | [optional] 
**itemSet** | **String** | The [furniture set](https://nookipedia.com/wiki/Set) the item is a part of, if any. A set is a smaller collection of related furniture items. If the item is not part of a set, this will be an empty string. | [optional] 
**lucky** | **Boolean** | Whether or not the item is lucky. Lucky items give a 777-point HHA bonus. Some items are only counted as lucky in certain seasons, as indicated by the &#x60;lucky_season&#x60; field. | [optional] 
**luckySeason** | **String** | The season in which the item is lucky (or \&quot;All year\&quot; if lucky throughout the entire year). Items that are not lucky will have this field as an empty string. | [optional] 
**name** | **String** | The name of the furniture. | [optional] 
**notes** | **String** | Any additional miscellaneous information about the item, such as a name change from a past update. | [optional] 
**patternTotal** | **Number** | The number of default patterns available to customize the item with, between 0 and 8. For items with customizable patterns, the player may also customize with patterns of their own. | [optional] 
**sell** | **Number** | The number of Bells the item can be sold to Nook&#39;s store for. | [optional] 
**tag** | **String** | The tag of an item, if any, which denotes a specific use or relation to an event. Tags are determined by Nintendo. Examples include \&quot;Chair\&quot;, \&quot;Musical Instrument\&quot;, and \&quot;Mario\&quot;. If the item does not have a tag, this will be an empty string. | [optional] 
**themes** | **[String]** | A list of [themes](https://nookipedia.com/wiki/Theme_(furniture)) (if any) that the item belongs to. | [optional] 
**unlocked** | **Boolean** | Whether the item is available through legitimate gameplay. Some items are added to the game files in an update, but aren&#39;t actually made available until a subsequent update unlocks them. | [optional] 
**url** | **String** | Link to the respective Nookipedia article. | [optional] 
**variationTotal** | **Number** | The number of variations, between 0 and 8. | [optional] 
**variations** | [**[NHFurnitureVariationsInner]**](NHFurnitureVariationsInner.md) | An array of objects, each object representing a variation of the furniture. Furniture that has no variations (only one version) will have a single variation object with the image URL and colors, but the &#x60;variation&#x60; or &#x60;pattern&#x60; fields will be empty strings. Furniture with multiple variations will have the &#x60;variation&#x60; and/or &#x60;pattern&#x60; fields defined depending on whether the furniture varies by body variety, pattern, or both. | [optional] 
**versionAdded** | **String** | The version of *New Horizons* that the item was added. Items that were included at the game&#39;s launch have version \&quot;1.0.0\&quot;. | [optional] 



## Enum: CategoryEnum


* `Housewares` (value: `"Housewares"`)

* `Miscellaneous` (value: `"Miscellaneous"`)

* `Wall-mounted` (value: `"Wall-mounted"`)





## Enum: [FunctionsEnum]


* `Trash` (value: `"Trash"`)

* `Toilet` (value: `"Toilet"`)

* `Table` (value: `"Table"`)

* `Storage` (value: `"Storage"`)

* `Stereo` (value: `"Stereo"`)

* `Seating` (value: `"Seating"`)

* `Lighting` (value: `"Lighting"`)

* `Instrument` (value: `"Instrument"`)

* `Dresser` (value: `"Dresser"`)

* `Bed` (value: `"Bed"`)

* `Audio` (value: `"Audio"`)





## Enum: LuckySeasonEnum


* `empty` (value: `""`)

* `All year` (value: `"All year"`)

* `Spring` (value: `"Spring"`)

* `Summer` (value: `"Summer"`)

* `Autumn` (value: `"Autumn"`)

* `Winter` (value: `"Winter"`)





## Enum: PatternTotalEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)

* `4` (value: `4`)

* `5` (value: `5`)

* `6` (value: `6`)

* `7` (value: `7`)

* `8` (value: `8`)





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




