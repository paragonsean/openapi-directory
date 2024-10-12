# ContentApiForShopping.OrdersCancelRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operationId** | **String** | The ID of the operation. Unique across all operations for a given order. | [optional] 
**reason** | **String** | The reason for the cancellation. Acceptable values are: - \&quot;&#x60;customerInitiatedCancel&#x60;\&quot; - \&quot;&#x60;invalidCoupon&#x60;\&quot; - \&quot;&#x60;malformedShippingAddress&#x60;\&quot; - \&quot;&#x60;noInventory&#x60;\&quot; - \&quot;&#x60;other&#x60;\&quot; - \&quot;&#x60;priceError&#x60;\&quot; - \&quot;&#x60;shippingPriceError&#x60;\&quot; - \&quot;&#x60;taxError&#x60;\&quot; - \&quot;&#x60;undeliverableShippingAddress&#x60;\&quot; - \&quot;&#x60;unsupportedPoBoxAddress&#x60;\&quot; - \&quot;&#x60;failedToCaptureFunds&#x60;\&quot;  | [optional] 
**reasonText** | **String** | The explanation of the reason. | [optional] 


