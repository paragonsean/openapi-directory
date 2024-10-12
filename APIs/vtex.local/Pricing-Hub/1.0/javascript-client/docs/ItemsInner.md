# PricingHub.ItemsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brandId** | **String** | This is the brand ID for the item | [default to &#39;2000000&#39;]
**categoriesIds** | **[String]** | ID of the categories that will be used to compute the price | 
**index** | **Number** | This is the index of the item at Checkout&#39;s cart. It has to be unique in the items array | [default to 0]
**priceTableIds** | **[String]** | IDs of the price tables that will be used to compute the price. More than one price table might be passed to the array. The final price rule might be more complex than the lowest or the highest price | 
**quantity** | **Number** | This is the amount of items that will be priced. It is possible to have a volume discount for many repeated items. Hence, the price may not be the quantity of the item multiplied by the unitary price | [default to 1]
**sellerId** | **String** | This is the seller ID for the item | [default to &#39;1&#39;]
**skuId** | **String** | This is the sku id of the item that will be priced | [default to &#39;13&#39;]


