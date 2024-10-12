

# GetOrder2200ResponseItemsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalInfo** | [**GetOrder2200ResponseItemsInnerAdditionalInfo**](GetOrder2200ResponseItemsInnerAdditionalInfo.md) |  |  [optional] |
|**attachments** | **List&lt;String&gt;** | Array containing information on attachments. |  [optional] |
|**availability** | **String** | Availability |  [optional] |
|**bundleItems** | [**List&lt;GetOrder2200ResponseItemsInnerBundleItemsInner&gt;**](GetOrder2200ResponseItemsInnerBundleItemsInner.md) | Information on services sold along with the SKU. Example: a gift package. |  [optional] |
|**detailUrl** | **String** | Detail URL. |  [optional] |
|**ean** | **String** | European Article Number. |  [optional] |
|**id** | **String** | ID. |  [optional] |
|**imageUrl** | **String** | Image URL. |  [optional] |
|**isGift** | **Boolean** | Indicates whether item is a gift. |  [optional] |
|**listPrice** | **Integer** | List price in cents. |  [optional] |
|**manualPrice** | **Integer** | Manual price in cents. |  [optional] |
|**manualPriceAppliedBy** | **String** | User that applied the manual price, if that is the case. |  [optional] |
|**manufacturerCode** | **String** | Manufacturer code. |  [optional] |
|**measurementUnit** | **String** | Measurement unit |  [optional] |
|**modalType** | **String** | Modal type. |  [optional] |
|**name** | **String** | Name. |  [optional] |
|**parentAssemblyBinding** | **String** | Parent assembly binding. |  [optional] |
|**parentItemIndex** | **Integer** | Parent item index. |  [optional] |
|**preSaleDate** | **String** | Presale date. |  [optional] |
|**price** | **Integer** | Price in cents. |  [optional] |
|**priceDefinition** | [**GetOrder2200ResponseItemsInnerPriceDefinition**](GetOrder2200ResponseItemsInnerPriceDefinition.md) |  |  [optional] |
|**priceTags** | [**List&lt;GetOrder2200ResponseItemsInnerPriceTagsInner&gt;**](GetOrder2200ResponseItemsInnerPriceTagsInner.md) | Array of price tags, each of which, modifies the price in some way, like discounts or rates that apply to the item in the context of the order. |  [optional] |
|**priceValidUntil** | **String** | Price expiration date and time. |  [optional] |
|**productCategories** | [**GetOrder2200ResponseItemsInnerProductCategories**](GetOrder2200ResponseItemsInnerProductCategories.md) |  |  [optional] |
|**productCategoryIds** | **String** | Product category IDs. |  [optional] |
|**productId** | **String** | Product ID. |  [optional] |
|**productRefId** | **String** | Product Ref ID. |  [optional] |
|**quantity** | **Integer** | Quantity. |  [optional] |
|**refId** | **String** | Ref ID. |  [optional] |
|**rewardValue** | **Integer** | Reward value in cents. |  [optional] |
|**seller** | **String** | Seller. |  [optional] |
|**sellerChain** | **List&lt;String&gt;** | Sellers involved in the chain. The list should contain only one seller, unless it is a [Multilevel Omnichannel Inventory](https://help.vtex.com/pt/tutorial/multilevel-omnichannel-inventory--7M1xyCZWUyCB7PcjNtOyw4) order. |  [optional] |
|**sellingPrice** | **Integer** | Selling price in cents. Note that this field may be subject to rounding discrepancies. We recommend retrieving data from the &#x60;priceDefinition&#x60; data structure instead. |  [optional] |
|**skuName** | **String** | SKU name. |  [optional] |
|**tax** | **Integer** | Tax value in cents. |  [optional] |
|**uniqueId** | **String** | Order&#39;s item unique ID. |  [optional] |
|**unitMultiplier** | **Integer** | Unit multiplier |  [optional] |



