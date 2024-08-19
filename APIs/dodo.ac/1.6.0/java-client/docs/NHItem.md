

# NHItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availability** | [**List&lt;NHClothingAvailabilityInner&gt;**](NHClothingAvailabilityInner.md) | Where the clothing may be obtained from (could be multiple sources). &#x60;from&#x60; is a brief description of the source; &#x60;note&#x60;, when provided, provides additional details. |  [optional] |
|**buy** | [**List&lt;NHClothingBuyInner&gt;**](NHClothingBuyInner.md) | An array of prices, for when the interior may be purchased with Bells, Nook Miles, etc.. |  [optional] |
|**edible** | **Boolean** | Whether the item is edible or not. |  [optional] |
|**hhaBase** | **Integer** | The base value that the item provides to a player&#39;s Happy Home Academy score when placed in their home. |  [optional] |
|**imageUrl** | **String** | Image of the interior. |  [optional] |
|**isFence** | **Boolean** | Whether or not the item is a fence or not. |  [optional] |
|**materialNameSort** | **Integer** | (WIP) |  [optional] |
|**materialSeasonality** | **String** | (WIP) |  [optional] |
|**materialSeasonalitySort** | **Integer** | (WIP) |  [optional] |
|**materialSort** | **Integer** | (WIP) |  [optional] |
|**materialType** | [**MaterialTypeEnum**](#MaterialTypeEnum) | (WIP) |  [optional] |
|**name** | **String** | The name of the item. |  [optional] |
|**notes** | **String** | Any additional miscellaneous information about the item, such as a name change from a past update. |  [optional] |
|**plantType** | [**PlantTypeEnum**](#PlantTypeEnum) | (WIP) |  [optional] |
|**sell** | **Integer** | The number of bells the item can be sold to Nook&#39;s store for. |  [optional] |
|**stack** | **Integer** | How much the item can stack up to in a single inventory slot. |  [optional] |
|**unlocked** | **Boolean** | Whether the item is available through legitimate gameplay. Some items are added to the game files in an update, but aren&#39;t actually made available until a subsequent update unlocks them. |  [optional] |
|**url** | **String** | Link to the respective Nookipedia article. |  [optional] |
|**versionAdded** | **String** | The version of *New Horizons* that the item was added. Items that were included at the game&#39;s launch have version \&quot;1.0.0\&quot;. |  [optional] |



## Enum: MaterialTypeEnum

| Name | Value |
|---- | -----|
| EMPTY | &quot;&quot; |
| BAMBOO | &quot;Bamboo&quot; |
| MUSHROOM | &quot;Mushroom&quot; |
| TRASH | &quot;Trash&quot; |
| WOOD | &quot;Wood&quot; |
| ORE | &quot;Ore&quot; |
| SNOWFLAKE | &quot;Snowflake&quot; |
| TREE | &quot;Tree&quot; |
| ORNAMENT | &quot;Ornament&quot; |
| FRUIT | &quot;Fruit&quot; |
| UNDERWATER | &quot;Underwater&quot; |
| OTHER | &quot;Other&quot; |
| LEAF | &quot;Leaf&quot; |
| SHELL | &quot;Shell&quot; |
| FLOWER | &quot;Flower&quot; |
| STAR_FRAGMENT | &quot;Star Fragment&quot; |
| FEATHER | &quot;Feather&quot; |
| EGG | &quot;Egg&quot; |
| PLANT | &quot;Plant&quot; |



## Enum: PlantTypeEnum

| Name | Value |
|---- | -----|
| EMPTY | &quot;&quot; |
| PUMPKIN | &quot;Pumpkin&quot; |
| FLOWER | &quot;Flower&quot; |
| BUSH | &quot;Bush&quot; |
| TREE | &quot;Tree&quot; |



