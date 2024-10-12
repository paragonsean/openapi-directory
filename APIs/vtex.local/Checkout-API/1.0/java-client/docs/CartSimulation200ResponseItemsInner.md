

# CartSimulation200ResponseItemsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availability** | **String** | Availability. |  [optional] |
|**id** | **String** | ID of the item. |  [optional] |
|**listPrice** | **Integer** | List price in cents. |  [optional] |
|**measurementUnit** | **String** | Measurement unit. |  [optional] |
|**offerings** | **List&lt;Object&gt;** | Array containing offering information. |  [optional] |
|**parentAssemblyBinding** | **String** | Parent assembly binding. |  [optional] |
|**parentItemIndex** | **Integer** | Parent item index. |  [optional] |
|**price** | **Integer** | Price in cents. |  [optional] |
|**priceDefinition** | [**AddCoupons200ResponseItemsInnerPriceDefinition**](AddCoupons200ResponseItemsInnerPriceDefinition.md) |  |  [optional] |
|**priceTags** | [**List&lt;CartSimulation200ResponseItemsInnerPriceTagsInner&gt;**](CartSimulation200ResponseItemsInnerPriceTagsInner.md) | Array of price tags, each of which, modifies the price in some way, like discounts or rates that apply to the item in the context of the order. |  [optional] |
|**priceValidUntil** | **String** | Price expiration date and time. |  [optional] |
|**quantity** | **Integer** | The quantity of the item the cart. |  [optional] |
|**requestIndex** | **Integer** | Request index information. |  [optional] |
|**rewardValue** | **Integer** | Reward value in cents. |  [optional] |
|**seller** | **String** | The seller responsible for the SKU. |  [optional] |
|**sellerChain** | **List&lt;String&gt;** | Sellers involved in the chain. The list should contain only one seller, unless it is a [Multilevel Omnichannel Inventory](https://help.vtex.com/en/tutorial/multilevel-omnichannel-inventory--7M1xyCZWUyCB7PcjNtOyw4) order. |  [optional] |
|**sellingPrice** | **Integer** | Selling price in cents. Note that this field may be subject to rounding discrepancies. We recommend retrieving data from the &#x60;priceDefinition&#x60; data structure instead. |  [optional] |
|**tax** | **Integer** | Tax value in cents. |  [optional] |
|**unitMultiplier** | **Integer** | Unit multiplier. |  [optional] |



