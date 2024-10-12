# ContentApiForShopping.OrdersRefundRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Price**](Price.md) |  | [optional] 
**amountPretax** | [**Price**](Price.md) |  | [optional] 
**amountTax** | [**Price**](Price.md) |  | [optional] 
**operationId** | **String** | The ID of the operation. Unique across all operations for a given order. | [optional] 
**reason** | **String** | The reason for the refund. Acceptable values are: - \&quot;&#x60;adjustment&#x60;\&quot; - \&quot;&#x60;courtesyAdjustment&#x60;\&quot; - \&quot;&#x60;customerCanceled&#x60;\&quot; - \&quot;&#x60;customerDiscretionaryReturn&#x60;\&quot; - \&quot;&#x60;deliveredLateByCarrier&#x60;\&quot; - \&quot;&#x60;feeAdjustment&#x60;\&quot; - \&quot;&#x60;lateShipmentCredit&#x60;\&quot; - \&quot;&#x60;noInventory&#x60;\&quot; - \&quot;&#x60;other&#x60;\&quot; - \&quot;&#x60;priceError&#x60;\&quot; - \&quot;&#x60;productArrivedDamaged&#x60;\&quot; - \&quot;&#x60;productNotAsDescribed&#x60;\&quot; - \&quot;&#x60;shippingCostAdjustment&#x60;\&quot; - \&quot;&#x60;taxAdjustment&#x60;\&quot; - \&quot;&#x60;undeliverableShippingAddress&#x60;\&quot; - \&quot;&#x60;wrongProductShipped&#x60;\&quot;  | [optional] 
**reasonText** | **String** | The explanation of the reason. | [optional] 


