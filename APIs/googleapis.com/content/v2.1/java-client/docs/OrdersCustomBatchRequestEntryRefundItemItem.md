

# OrdersCustomBatchRequestEntryRefundItemItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | [**MonetaryAmount**](MonetaryAmount.md) |  |  [optional] |
|**fullRefund** | **Boolean** | If true, the full item will be refunded. If this is true, amount shouldn&#39;t be provided and will be ignored. |  [optional] |
|**lineItemId** | **String** | The ID of the line item. Either lineItemId or productId is required. |  [optional] |
|**productId** | **String** | The ID of the product. This is the REST ID used in the products service. Either lineItemId or productId is required. |  [optional] |
|**quantity** | **Integer** | The number of products that are refunded. |  [optional] |



