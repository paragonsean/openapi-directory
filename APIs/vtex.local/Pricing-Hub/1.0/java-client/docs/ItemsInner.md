

# ItemsInner

Each item to be priced by Pricing Hub

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**brandId** | **String** | This is the brand ID for the item |  |
|**categoriesIds** | **List&lt;String&gt;** | ID of the categories that will be used to compute the price |  |
|**index** | **Integer** | This is the index of the item at Checkout&#39;s cart. It has to be unique in the items array |  |
|**priceTableIds** | **List&lt;String&gt;** | IDs of the price tables that will be used to compute the price. More than one price table might be passed to the array. The final price rule might be more complex than the lowest or the highest price |  |
|**quantity** | **Integer** | This is the amount of items that will be priced. It is possible to have a volume discount for many repeated items. Hence, the price may not be the quantity of the item multiplied by the unitary price |  |
|**sellerId** | **String** | This is the seller ID for the item |  |
|**skuId** | **String** | This is the sku id of the item that will be priced |  |



