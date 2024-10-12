# Nookipedia.NHInterior

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability** | [**[NHClothingAvailabilityInner]**](NHClothingAvailabilityInner.md) | Where the clothing may be obtained from (could be multiple sources). &#x60;from&#x60; is a brief description of the source; &#x60;note&#x60;, when provided, provides additional details. | [optional] 
**buy** | [**[NHClothingBuyInner]**](NHClothingBuyInner.md) | An array of prices, for when the interior may be purchased with Bells, Nook Miles, etc.. | [optional] 
**category** | **String** | The category of item as shown in the player&#39;s inventory. | [optional] 
**colors** | **String** | (WIP) | [optional] 
**gridLength** | **Number** | The number of lengthwise grid spaces this item takes up. | [optional] 
**gridWidth** | **Number** | The number of widthwise grid spaces this item takes up. | [optional] 
**hhaBase** | **Number** | The base value that the item provides to a player&#39;s Happy Home Academy score when placed in their home. | [optional] 
**hhaCategory** | **String** | The HHA category the item is a part of, if any. If the item does not have an HHA category, this will be an empty string. | [optional] 
**imageUrl** | **String** | Image of the interior. | [optional] 
**itemSeries** | **String** | The [furniture series](https://nookipedia.com/wiki/Series_(furniture)) the item is a part of, if any. A series is a collection of furniture and interior items, all with the same theme. If the item is not part of a series, this will be an empty string. | [optional] 
**itemSet** | **String** | The [furniture set](https://nookipedia.com/wiki/Set) the item is a part of, if any. A set is a smaller collection of related furniture items. If the item is not part of a set, this will be an empty string. | [optional] 
**name** | **String** | The name of the interior. | [optional] 
**notes** | **String** | Any additional miscellaneous information about the item, such as a name change from a past update. | [optional] 
**sell** | **Number** | The number of Bells the interior can be sold to Nook&#39;s store for. | [optional] 
**tag** | **String** | The tag of an item, if any, which denotes a specific use or relation to an event. Tags are determined by Nintendo. Examples include \&quot;Chair\&quot;, \&quot;Musical Instrument\&quot;, and \&quot;Mario\&quot;. If the item does not have a tag, this will be an empty string. | [optional] 
**themes** | **[String]** | A list of [themes](https://nookipedia.com/wiki/Theme_(furniture)) (if any) that the item belongs to. | [optional] 
**unlocked** | **Boolean** | Whether the item is available through legitimate gameplay. Some items are added to the game files in an update, but aren&#39;t actually made available until a subsequent update unlocks them. | [optional] 
**url** | **String** | Link to the respective Nookipedia article. | [optional] 
**versionAdded** | **String** | The version of *New Horizons* that the item was added. Items that were included at the game&#39;s launch have version \&quot;1.0.0\&quot;. | [optional] 



## Enum: CategoryEnum


* `Floors` (value: `"Floors"`)

* `Wallpaper` (value: `"Wallpaper"`)

* `Rugs` (value: `"Rugs"`)





## Enum: ColorsEnum


* `Aqua` (value: `"Aqua"`)

* `Beige` (value: `"Beige"`)

* `Black` (value: `"Black"`)

* `Blue` (value: `"Blue"`)

* `Brown` (value: `"Brown"`)

* `Colorful` (value: `"Colorful"`)

* `Gray` (value: `"Gray"`)

* `Green` (value: `"Green"`)

* `Orange` (value: `"Orange"`)

* `Pink` (value: `"Pink"`)

* `Purple` (value: `"Purple"`)

* `Red` (value: `"Red"`)

* `White` (value: `"White"`)

* `Yellow` (value: `"Yellow"`)




