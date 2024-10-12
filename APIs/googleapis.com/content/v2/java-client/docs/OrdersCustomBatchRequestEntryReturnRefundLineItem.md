

# OrdersCustomBatchRequestEntryReturnRefundLineItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amountPretax** | [**Price**](Price.md) |  |  [optional] |
|**amountTax** | [**Price**](Price.md) |  |  [optional] |
|**lineItemId** | **String** | The ID of the line item to return. Either lineItemId or productId is required. |  [optional] |
|**productId** | **String** | The ID of the product to return. This is the REST ID used in the products service. Either lineItemId or productId is required. |  [optional] |
|**quantity** | **Integer** | The quantity to return and refund. |  [optional] |
|**reason** | **String** | The reason for the return. Acceptable values are: - \&quot;&#x60;customerDiscretionaryReturn&#x60;\&quot; - \&quot;&#x60;customerInitiatedMerchantCancel&#x60;\&quot; - \&quot;&#x60;deliveredTooLate&#x60;\&quot; - \&quot;&#x60;expiredItem&#x60;\&quot; - \&quot;&#x60;invalidCoupon&#x60;\&quot; - \&quot;&#x60;malformedShippingAddress&#x60;\&quot; - \&quot;&#x60;other&#x60;\&quot; - \&quot;&#x60;productArrivedDamaged&#x60;\&quot; - \&quot;&#x60;productNotAsDescribed&#x60;\&quot; - \&quot;&#x60;qualityNotAsExpected&#x60;\&quot; - \&quot;&#x60;undeliverableShippingAddress&#x60;\&quot; - \&quot;&#x60;unsupportedPoBoxAddress&#x60;\&quot; - \&quot;&#x60;wrongProductShipped&#x60;\&quot;  |  [optional] |
|**reasonText** | **String** | The explanation of the reason. |  [optional] |



