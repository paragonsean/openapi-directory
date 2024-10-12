

# NHClothing


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availability** | [**List&lt;NHClothingAvailabilityInner&gt;**](NHClothingAvailabilityInner.md) | Where the clothing may be obtained from (could be multiple sources). &#x60;from&#x60; is a brief description of the source; &#x60;note&#x60;, when provided, provides additional details. |  [optional] |
|**buy** | [**List&lt;NHClothingBuyInner&gt;**](NHClothingBuyInner.md) | An array of prices, for when the item may be purchased with Bells, Nook Miles, etc.. |  [optional] |
|**category** | [**CategoryEnum**](#CategoryEnum) | The category of item as shown in the player&#39;s inventory. |  [optional] |
|**labelThemes** | [**List&lt;LabelThemesEnum&gt;**](#List&lt;LabelThemesEnum&gt;) | The clothing&#39;s Label theme(s). This is used for completing the requested outfit theme for [Label](https://nookipedia.com/wiki/Label) when she visits the player&#39;s island. |  [optional] |
|**name** | **String** | The name of the clothing. |  [optional] |
|**notes** | **String** | Any additional miscellaneous information about the clothing, such as a name change from a past update. |  [optional] |
|**seasonality** | **String** | The time of the year that the clothing is available. |  [optional] |
|**sell** | **Integer** | The number of Bells the clothing can be sold to the store for. |  [optional] |
|**styles** | [**List&lt;StylesEnum&gt;**](#List&lt;StylesEnum&gt;) | The clothing&#39;s style(s). Styles are used for gifting villagers. |  [optional] |
|**unlocked** | **Boolean** | Whether the item is available through legitimate gameplay. Some items are added to the game files in an update, but aren&#39;t actually made available until a subsequent update unlocks them. |  [optional] |
|**url** | **String** | Link to the respective Nookipedia article. |  [optional] |
|**variationTotal** | [**VariationTotalEnum**](#VariationTotalEnum) | The total number of variations the clothing has, between 0 and 8. |  [optional] |
|**variations** | [**List&lt;NHClothingVariationsInner&gt;**](NHClothingVariationsInner.md) | An array of objects, each object representing a variation of the clothing. Clothing that has no variations (only one version) will have a single variation object with the image URL and colors, but the &#x60;variation&#x60; field will be empty. Clothing with multiple variations will have the &#x60;variation&#x60; fields defined with the name of each variation. |  [optional] |
|**versionAdded** | **String** | The version of *New Horizons* that the item was added. Items that were included at the game&#39;s launch have version \&quot;1.0.0\&quot;. |  [optional] |
|**villEquip** | **Boolean** | Whether villagers may equip this item. |  [optional] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| TOPS | &quot;Tops&quot; |
| BOTTOMS | &quot;Bottoms&quot; |
| DRESS_UP | &quot;Dress-up&quot; |
| HEADWEAR | &quot;Headwear&quot; |
| ACCESSORIES | &quot;Accessories&quot; |
| SOCKS | &quot;Socks&quot; |
| SHOES | &quot;Shoes&quot; |
| BAGS | &quot;Bags&quot; |
| UMBRELLAS | &quot;Umbrellas&quot; |



## Enum: List&lt;LabelThemesEnum&gt;

| Name | Value |
|---- | -----|
| COMFY | &quot;Comfy&quot; |
| EVERYDAY | &quot;Everyday&quot; |
| FAIRY_TALE | &quot;Fairy tale&quot; |
| FORMAL | &quot;Formal&quot; |
| GOTH | &quot;Goth&quot; |
| OUTDOORSY | &quot;Outdoorsy&quot; |
| PARTY | &quot;Party&quot; |
| SPORTY | &quot;Sporty&quot; |
| THEATRICAL | &quot;Theatrical&quot; |
| VACATION | &quot;Vacation&quot; |
| WORK | &quot;Work&quot; |



## Enum: List&lt;StylesEnum&gt;

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| COOL | &quot;Cool&quot; |
| CUTE | &quot;Cute&quot; |
| ELEGANT | &quot;Elegant&quot; |
| GORGEOUS | &quot;Gorgeous&quot; |
| SIMPLE | &quot;Simple&quot; |



## Enum: VariationTotalEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |
| NUMBER_5 | 5 |
| NUMBER_6 | 6 |
| NUMBER_7 | 7 |
| NUMBER_8 | 8 |



