# ContentApiForShopping.OrdersRefundItemRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**[OrdersCustomBatchRequestEntryRefundItemItem]**](OrdersCustomBatchRequestEntryRefundItemItem.md) | The items that are refunded. Either Item or Shipping must be provided in the request. | [optional] 
**operationId** | **String** | The ID of the operation. Unique across all operations for a given order. | [optional] 
**reason** | **String** | The reason for the refund. Acceptable values are: - \&quot;&#x60;shippingCostAdjustment&#x60;\&quot; - \&quot;&#x60;priceAdjustment&#x60;\&quot; - \&quot;&#x60;taxAdjustment&#x60;\&quot; - \&quot;&#x60;feeAdjustment&#x60;\&quot; - \&quot;&#x60;courtesyAdjustment&#x60;\&quot; - \&quot;&#x60;adjustment&#x60;\&quot; - \&quot;&#x60;customerCancelled&#x60;\&quot; - \&quot;&#x60;noInventory&#x60;\&quot; - \&quot;&#x60;productNotAsDescribed&#x60;\&quot; - \&quot;&#x60;undeliverableShippingAddress&#x60;\&quot; - \&quot;&#x60;wrongProductShipped&#x60;\&quot; - \&quot;&#x60;lateShipmentCredit&#x60;\&quot; - \&quot;&#x60;deliveredLateByCarrier&#x60;\&quot; - \&quot;&#x60;productArrivedDamaged&#x60;\&quot;  | [optional] 
**reasonText** | **String** | The explanation of the reason. | [optional] 
**shipping** | [**OrdersCustomBatchRequestEntryRefundItemShipping**](OrdersCustomBatchRequestEntryRefundItemShipping.md) |  | [optional] 


