# ContentApiForShopping.OrderCancellation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor** | **String** | The actor that created the cancellation. Acceptable values are: - \&quot;&#x60;customer&#x60;\&quot; - \&quot;&#x60;googleBot&#x60;\&quot; - \&quot;&#x60;googleCustomerService&#x60;\&quot; - \&quot;&#x60;googlePayments&#x60;\&quot; - \&quot;&#x60;googleSabre&#x60;\&quot; - \&quot;&#x60;merchant&#x60;\&quot;  | [optional] 
**creationDate** | **String** | Date on which the cancellation has been created, in ISO 8601 format. | [optional] 
**quantity** | **Number** | The quantity that was canceled. | [optional] 
**reason** | **String** | The reason for the cancellation. Orders that are canceled with a noInventory reason will lead to the removal of the product from Buy on Google until you make an update to that product. This will not affect your Shopping ads. Acceptable values are: - \&quot;&#x60;autoPostInternal&#x60;\&quot; - \&quot;&#x60;autoPostInvalidBillingAddress&#x60;\&quot; - \&quot;&#x60;autoPostNoInventory&#x60;\&quot; - \&quot;&#x60;autoPostPriceError&#x60;\&quot; - \&quot;&#x60;autoPostUndeliverableShippingAddress&#x60;\&quot; - \&quot;&#x60;couponAbuse&#x60;\&quot; - \&quot;&#x60;customerCanceled&#x60;\&quot; - \&quot;&#x60;customerInitiatedCancel&#x60;\&quot; - \&quot;&#x60;customerSupportRequested&#x60;\&quot; - \&quot;&#x60;failToPushOrderGoogleError&#x60;\&quot; - \&quot;&#x60;failToPushOrderMerchantError&#x60;\&quot; - \&quot;&#x60;failToPushOrderMerchantFulfillmentError&#x60;\&quot; - \&quot;&#x60;failToPushOrderToMerchant&#x60;\&quot; - \&quot;&#x60;failToPushOrderToMerchantOutOfStock&#x60;\&quot; - \&quot;&#x60;invalidCoupon&#x60;\&quot; - \&quot;&#x60;malformedShippingAddress&#x60;\&quot; - \&quot;&#x60;merchantDidNotShipOnTime&#x60;\&quot; - \&quot;&#x60;noInventory&#x60;\&quot; - \&quot;&#x60;orderTimeout&#x60;\&quot; - \&quot;&#x60;other&#x60;\&quot; - \&quot;&#x60;paymentAbuse&#x60;\&quot; - \&quot;&#x60;paymentDeclined&#x60;\&quot; - \&quot;&#x60;priceError&#x60;\&quot; - \&quot;&#x60;returnRefundAbuse&#x60;\&quot; - \&quot;&#x60;shippingPriceError&#x60;\&quot; - \&quot;&#x60;taxError&#x60;\&quot; - \&quot;&#x60;undeliverableShippingAddress&#x60;\&quot; - \&quot;&#x60;unsupportedPoBoxAddress&#x60;\&quot;  | [optional] 
**reasonText** | **String** | The explanation of the reason. | [optional] 


