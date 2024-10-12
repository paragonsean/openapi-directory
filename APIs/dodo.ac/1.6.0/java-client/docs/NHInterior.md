

# NHInterior


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availability** | [**List&lt;NHClothingAvailabilityInner&gt;**](NHClothingAvailabilityInner.md) | Where the clothing may be obtained from (could be multiple sources). &#x60;from&#x60; is a brief description of the source; &#x60;note&#x60;, when provided, provides additional details. |  [optional] |
|**buy** | [**List&lt;NHClothingBuyInner&gt;**](NHClothingBuyInner.md) | An array of prices, for when the interior may be purchased with Bells, Nook Miles, etc.. |  [optional] |
|**category** | [**CategoryEnum**](#CategoryEnum) | The category of item as shown in the player&#39;s inventory. |  [optional] |
|**colors** | [**ColorsEnum**](#ColorsEnum) | (WIP) |  [optional] |
|**gridLength** | **Float** | The number of lengthwise grid spaces this item takes up. |  [optional] |
|**gridWidth** | **Float** | The number of widthwise grid spaces this item takes up. |  [optional] |
|**hhaBase** | **Integer** | The base value that the item provides to a player&#39;s Happy Home Academy score when placed in their home. |  [optional] |
|**hhaCategory** | **String** | The HHA category the item is a part of, if any. If the item does not have an HHA category, this will be an empty string. |  [optional] |
|**imageUrl** | **String** | Image of the interior. |  [optional] |
|**itemSeries** | **String** | The [furniture series](https://nookipedia.com/wiki/Series_(furniture)) the item is a part of, if any. A series is a collection of furniture and interior items, all with the same theme. If the item is not part of a series, this will be an empty string. |  [optional] |
|**itemSet** | **String** | The [furniture set](https://nookipedia.com/wiki/Set) the item is a part of, if any. A set is a smaller collection of related furniture items. If the item is not part of a set, this will be an empty string. |  [optional] |
|**name** | **String** | The name of the interior. |  [optional] |
|**notes** | **String** | Any additional miscellaneous information about the item, such as a name change from a past update. |  [optional] |
|**sell** | **Integer** | The number of Bells the interior can be sold to Nook&#39;s store for. |  [optional] |
|**tag** | **String** | The tag of an item, if any, which denotes a specific use or relation to an event. Tags are determined by Nintendo. Examples include \&quot;Chair\&quot;, \&quot;Musical Instrument\&quot;, and \&quot;Mario\&quot;. If the item does not have a tag, this will be an empty string. |  [optional] |
|**themes** | **List&lt;String&gt;** | A list of [themes](https://nookipedia.com/wiki/Theme_(furniture)) (if any) that the item belongs to. |  [optional] |
|**unlocked** | **Boolean** | Whether the item is available through legitimate gameplay. Some items are added to the game files in an update, but aren&#39;t actually made available until a subsequent update unlocks them. |  [optional] |
|**url** | **String** | Link to the respective Nookipedia article. |  [optional] |
|**versionAdded** | **String** | The version of *New Horizons* that the item was added. Items that were included at the game&#39;s launch have version \&quot;1.0.0\&quot;. |  [optional] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| FLOORS | &quot;Floors&quot; |
| WALLPAPER | &quot;Wallpaper&quot; |
| RUGS | &quot;Rugs&quot; |



## Enum: ColorsEnum

| Name | Value |
|---- | -----|
| AQUA | &quot;Aqua&quot; |
| BEIGE | &quot;Beige&quot; |
| BLACK | &quot;Black&quot; |
| BLUE | &quot;Blue&quot; |
| BROWN | &quot;Brown&quot; |
| COLORFUL | &quot;Colorful&quot; |
| GRAY | &quot;Gray&quot; |
| GREEN | &quot;Green&quot; |
| ORANGE | &quot;Orange&quot; |
| PINK | &quot;Pink&quot; |
| PURPLE | &quot;Purple&quot; |
| RED | &quot;Red&quot; |
| WHITE | &quot;White&quot; |
| YELLOW | &quot;Yellow&quot; |



