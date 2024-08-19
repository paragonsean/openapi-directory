# Nookipedia.NHItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability** | [**[NHClothingAvailabilityInner]**](NHClothingAvailabilityInner.md) | Where the clothing may be obtained from (could be multiple sources). &#x60;from&#x60; is a brief description of the source; &#x60;note&#x60;, when provided, provides additional details. | [optional] 
**buy** | [**[NHClothingBuyInner]**](NHClothingBuyInner.md) | An array of prices, for when the interior may be purchased with Bells, Nook Miles, etc.. | [optional] 
**edible** | **Boolean** | Whether the item is edible or not. | [optional] 
**hhaBase** | **Number** | The base value that the item provides to a player&#39;s Happy Home Academy score when placed in their home. | [optional] 
**imageUrl** | **String** | Image of the interior. | [optional] 
**isFence** | **Boolean** | Whether or not the item is a fence or not. | [optional] 
**materialNameSort** | **Number** | (WIP) | [optional] 
**materialSeasonality** | **String** | (WIP) | [optional] 
**materialSeasonalitySort** | **Number** | (WIP) | [optional] 
**materialSort** | **Number** | (WIP) | [optional] 
**materialType** | **String** | (WIP) | [optional] 
**name** | **String** | The name of the item. | [optional] 
**notes** | **String** | Any additional miscellaneous information about the item, such as a name change from a past update. | [optional] 
**plantType** | **String** | (WIP) | [optional] 
**sell** | **Number** | The number of bells the item can be sold to Nook&#39;s store for. | [optional] 
**stack** | **Number** | How much the item can stack up to in a single inventory slot. | [optional] 
**unlocked** | **Boolean** | Whether the item is available through legitimate gameplay. Some items are added to the game files in an update, but aren&#39;t actually made available until a subsequent update unlocks them. | [optional] 
**url** | **String** | Link to the respective Nookipedia article. | [optional] 
**versionAdded** | **String** | The version of *New Horizons* that the item was added. Items that were included at the game&#39;s launch have version \&quot;1.0.0\&quot;. | [optional] 



## Enum: MaterialTypeEnum


* `empty` (value: `""`)

* `Bamboo` (value: `"Bamboo"`)

* `Mushroom` (value: `"Mushroom"`)

* `Trash` (value: `"Trash"`)

* `Wood` (value: `"Wood"`)

* `Ore` (value: `"Ore"`)

* `Snowflake` (value: `"Snowflake"`)

* `Tree` (value: `"Tree"`)

* `Ornament` (value: `"Ornament"`)

* `Fruit` (value: `"Fruit"`)

* `Underwater` (value: `"Underwater"`)

* `Other` (value: `"Other"`)

* `Leaf` (value: `"Leaf"`)

* `Shell` (value: `"Shell"`)

* `Flower` (value: `"Flower"`)

* `Star Fragment` (value: `"Star Fragment"`)

* `Feather` (value: `"Feather"`)

* `Egg` (value: `"Egg"`)

* `Plant` (value: `"Plant"`)





## Enum: PlantTypeEnum


* `empty` (value: `""`)

* `Pumpkin` (value: `"Pumpkin"`)

* `Flower` (value: `"Flower"`)

* `Bush` (value: `"Bush"`)

* `Tree` (value: `"Tree"`)




