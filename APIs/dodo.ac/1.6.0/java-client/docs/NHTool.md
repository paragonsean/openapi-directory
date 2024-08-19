

# NHTool


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availability** | [**List&lt;NHClothingAvailabilityInner&gt;**](NHClothingAvailabilityInner.md) | Where the tool may be obtained from (could be multiple sources). &#x60;from&#x60; is a brief description of the source; &#x60;note&#x60;, when provided, provides additional details. |  [optional] |
|**buy** | [**List&lt;NHClothingBuyInner&gt;**](NHClothingBuyInner.md) | An array of prices, for when the item may be purchased with Bells, Nook Miles, etc.. |  [optional] |
|**customBodyPart** | **String** | If the item has variations, this is the name of the furniture part that changes. For example, for many bamboo items, the custom body part is \&quot;Bamboo\&quot; as the bamboo color is able to be customized. |  [optional] |
|**customKits** | **Integer** | The number of &#x60;custom_kit_type&#x60;s (e.g. Customization Kits) that are needed to customize this item. Value is 0 if the item is not customizable. |  [optional] |
|**customizable** | **Boolean** | Whether or not the item is customizable via a crafting table. |  [optional] |
|**hhaBase** | **Integer** | The base value that the item provides to a player&#39;s Happy Home Academy score when placed in their home. |  [optional] |
|**name** | **String** | The name of the tool. |  [optional] |
|**notes** | **String** | Any additional miscellaneous information about the item, such as a name change from a past update. |  [optional] |
|**sell** | **Integer** | The number of bells the tool can be sold to the store for. |  [optional] |
|**unlocked** | **Boolean** | Whether the item is available through legitimate gameplay. Some items are added to the game files in an update, but aren&#39;t actually made available until a subsequent update unlocks them. |  [optional] |
|**url** | **String** | Link the the respective Nookipedia article. |  [optional] |
|**uses** | **Integer** | How many times the tool can be used before breaking. |  [optional] |
|**variations** | [**List&lt;NHToolVariationsInner&gt;**](NHToolVariationsInner.md) | An array of objects, each object representing a variation of the tool. Tools that has no variations (only one version) will have a single variation object with the image URL and colors, but the &#x60;variation&#x60; field will be empty. Tools with multiple variations will have the &#x60;variation&#x60; fields defined with the name of each variation. |  [optional] |
|**versionAdded** | **String** | The version of *New Horizons* that the item was added. Items that were included at the game&#39;s launch have version \&quot;1.0.0\&quot;. |  [optional] |



