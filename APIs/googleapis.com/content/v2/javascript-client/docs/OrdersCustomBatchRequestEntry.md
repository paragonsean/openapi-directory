# ContentApiForShopping.OrdersCustomBatchRequestEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batchId** | **Number** | An entry ID, unique within the batch request. | [optional] 
**cancel** | [**OrdersCustomBatchRequestEntryCancel**](OrdersCustomBatchRequestEntryCancel.md) |  | [optional] 
**cancelLineItem** | [**OrdersCustomBatchRequestEntryCancelLineItem**](OrdersCustomBatchRequestEntryCancelLineItem.md) |  | [optional] 
**inStoreRefundLineItem** | [**OrdersCustomBatchRequestEntryInStoreRefundLineItem**](OrdersCustomBatchRequestEntryInStoreRefundLineItem.md) |  | [optional] 
**merchantId** | **String** | The ID of the managing account. | [optional] 
**merchantOrderId** | **String** | The merchant order ID. Required for &#x60;updateMerchantOrderId&#x60; and &#x60;getByMerchantOrderId&#x60; methods. | [optional] 
**method** | **String** | The method of the batch entry. Acceptable values are: - \&quot;&#x60;acknowledge&#x60;\&quot; - \&quot;&#x60;cancel&#x60;\&quot; - \&quot;&#x60;cancelLineItem&#x60;\&quot; - \&quot;&#x60;get&#x60;\&quot; - \&quot;&#x60;getByMerchantOrderId&#x60;\&quot; - \&quot;&#x60;inStoreRefundLineItem&#x60;\&quot; - \&quot;&#x60;refund&#x60;\&quot; - \&quot;&#x60;rejectReturnLineItem&#x60;\&quot; - \&quot;&#x60;returnLineItem&#x60;\&quot; - \&quot;&#x60;returnRefundLineItem&#x60;\&quot; - \&quot;&#x60;setLineItemMetadata&#x60;\&quot; - \&quot;&#x60;shipLineItems&#x60;\&quot; - \&quot;&#x60;updateLineItemShippingDetails&#x60;\&quot; - \&quot;&#x60;updateMerchantOrderId&#x60;\&quot; - \&quot;&#x60;updateShipment&#x60;\&quot;  | [optional] 
**operationId** | **String** | The ID of the operation. Unique across all operations for a given order. Required for all methods beside &#x60;get&#x60; and &#x60;getByMerchantOrderId&#x60;. | [optional] 
**orderId** | **String** | The ID of the order. Required for all methods beside &#x60;getByMerchantOrderId&#x60;. | [optional] 
**refund** | [**OrdersCustomBatchRequestEntryRefund**](OrdersCustomBatchRequestEntryRefund.md) |  | [optional] 
**rejectReturnLineItem** | [**OrdersCustomBatchRequestEntryRejectReturnLineItem**](OrdersCustomBatchRequestEntryRejectReturnLineItem.md) |  | [optional] 
**returnLineItem** | [**OrdersCustomBatchRequestEntryReturnLineItem**](OrdersCustomBatchRequestEntryReturnLineItem.md) |  | [optional] 
**returnRefundLineItem** | [**OrdersCustomBatchRequestEntryReturnRefundLineItem**](OrdersCustomBatchRequestEntryReturnRefundLineItem.md) |  | [optional] 
**setLineItemMetadata** | [**OrdersCustomBatchRequestEntrySetLineItemMetadata**](OrdersCustomBatchRequestEntrySetLineItemMetadata.md) |  | [optional] 
**shipLineItems** | [**OrdersCustomBatchRequestEntryShipLineItems**](OrdersCustomBatchRequestEntryShipLineItems.md) |  | [optional] 
**updateLineItemShippingDetails** | [**OrdersCustomBatchRequestEntryUpdateLineItemShippingDetails**](OrdersCustomBatchRequestEntryUpdateLineItemShippingDetails.md) |  | [optional] 
**updateShipment** | [**OrdersCustomBatchRequestEntryUpdateShipment**](OrdersCustomBatchRequestEntryUpdateShipment.md) |  | [optional] 


