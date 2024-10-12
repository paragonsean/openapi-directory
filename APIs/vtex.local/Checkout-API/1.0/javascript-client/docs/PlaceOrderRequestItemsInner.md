# CheckoutApi.PlaceOrderRequestItemsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | **[String]** | Array containing information on attachments. | [optional] 
**bundleItems** | [**[PlaceOrderRequestItemsInnerBundleItemsInner]**](PlaceOrderRequestItemsInnerBundleItemsInner.md) | Information on services sold along with the SKU. Example: a gift package. | [optional] 
**commission** | **Number** | Comission. | [optional] 
**freightCommission** | **Number** | Freight comission | [optional] 
**id** | **String** | The SKU ID. | 
**isGift** | **Boolean** | Indicates whether the order is a gift. | [optional] [default to false]
**itemAttachment** | [**PlaceOrderRequestItemsInnerItemAttachment**](PlaceOrderRequestItemsInnerItemAttachment.md) |  | [optional] 
**measurementUnit** | **String** | SKU measurement unit. | [optional] [default to &#39;g&#39;]
**price** | **Number** | Item price within the context of the order without separating cents. For example, $24.99 is represented &#x60;2499&#x60;. | [optional] 
**priceTags** | [**[PlaceOrderRequestItemsInnerPriceTagsInner]**](PlaceOrderRequestItemsInnerPriceTagsInner.md) | Array of price tags, each of which, modifies the price in some way, like discounts or rates that apply to the item in the context of the order. | [optional] 
**quantity** | **Number** | The quantity of items of this specific SKU in the cart to be simulated. | 
**seller** | **String** | The ID of the seller responsible for this SKU. This ID can be found in your VTEX Admin. | 
**unitMultiplier** | **Number** | SKU unit multiplier. | [optional] [default to 1]


