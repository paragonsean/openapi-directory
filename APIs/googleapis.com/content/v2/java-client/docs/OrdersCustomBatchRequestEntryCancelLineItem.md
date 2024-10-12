

# OrdersCustomBatchRequestEntryCancelLineItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | [**Price**](Price.md) |  |  [optional] |
|**amountPretax** | [**Price**](Price.md) |  |  [optional] |
|**amountTax** | [**Price**](Price.md) |  |  [optional] |
|**lineItemId** | **String** | The ID of the line item to cancel. Either lineItemId or productId is required. |  [optional] |
|**productId** | **String** | The ID of the product to cancel. This is the REST ID used in the products service. Either lineItemId or productId is required. |  [optional] |
|**quantity** | **Integer** | The quantity to cancel. |  [optional] |
|**reason** | **String** | The reason for the cancellation. Acceptable values are: - \&quot;&#x60;customerInitiatedCancel&#x60;\&quot; - \&quot;&#x60;invalidCoupon&#x60;\&quot; - \&quot;&#x60;malformedShippingAddress&#x60;\&quot; - \&quot;&#x60;noInventory&#x60;\&quot; - \&quot;&#x60;other&#x60;\&quot; - \&quot;&#x60;priceError&#x60;\&quot; - \&quot;&#x60;shippingPriceError&#x60;\&quot; - \&quot;&#x60;taxError&#x60;\&quot; - \&quot;&#x60;undeliverableShippingAddress&#x60;\&quot; - \&quot;&#x60;unsupportedPoBoxAddress&#x60;\&quot;  |  [optional] |
|**reasonText** | **String** | The explanation of the reason. |  [optional] |



