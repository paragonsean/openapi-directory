

# NHRecipe


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availability** | [**List&lt;NHClothingAvailabilityInner&gt;**](NHClothingAvailabilityInner.md) | Where the recipe may be obtained from. &#x60;from&#x60; is a brief description of the source; &#x60;note&#x60;, when provided, provides additional details. |  [optional] |
|**buy** | [**List&lt;NHClothingBuyInner&gt;**](NHClothingBuyInner.md) | An array of prices, for when the recipe may be purchased with Bells, Nook Miles, etc. The majority of recipes cannot be bought (in which case this array will be empty). |  [optional] |
|**imageUrl** | **String** | Image of the item the recipe crafts. |  [optional] |
|**materials** | [**List&lt;NHRecipeMaterialsInner&gt;**](NHRecipeMaterialsInner.md) | The list of materials required to craft the item. |  [optional] |
|**name** | **String** | The name of the recipe. |  [optional] |
|**recipesToUnlock** | **Integer** | How many recipes the player has to have learned to unlock this one. |  [optional] |
|**sell** | **Integer** | The number of Bells the sea creature can be sold to Nook&#39;s store for. |  [optional] |
|**serialId** | **Integer** | The unique in-game ID of the recipe. |  [optional] |
|**url** | **String** | Link to the respective Nookipedia article. |  [optional] |



