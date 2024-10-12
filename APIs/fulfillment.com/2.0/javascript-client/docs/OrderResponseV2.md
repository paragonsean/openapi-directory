# FulfillmentComApiv2.OrderResponseV2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currentStatus** | [**StatusEventV2**](StatusEventV2.md) |  | 
**departDate** | **Date** | DateTime order departed an FDC warehouse | [optional] 
**dispatchDate** | **Date** | DateTime order was dispatched for fulfillment by FDC | [optional] 
**id** | **Number** | FDC ID for this order | 
**merchant** | [**MerchantV2**](MerchantV2.md) |  | 
**merchantOrderId** | **String** | Merchant provided ID | 
**merchantShippingMethod** | **String** | Requested ship method | 
**originalConsignee** | [**ConsigneeV2**](ConsigneeV2.md) |  | 
**parentOrder** | [**OrderResponseV2ParentOrder**](OrderResponseV2ParentOrder.md) |  | [optional] 
**purchaseOrderNum** | **String** | Merchant provided PO# | [optional] 
**recordedOn** | **Date** | DateTime order was recorded by FDC | 
**trackingNumbers** | [**[TrackingNumberV2]**](TrackingNumberV2.md) |  | [optional] 
**validatedConsignee** | **Object** |  | 
**warehouse** | [**WarehouseV2**](WarehouseV2.md) |  | [optional] 


