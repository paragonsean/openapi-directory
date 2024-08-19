

# OrderResponseV2


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentStatus** | [**StatusEventV2**](StatusEventV2.md) |  |  |
|**departDate** | **OffsetDateTime** | DateTime order departed an FDC warehouse |  [optional] |
|**dispatchDate** | **OffsetDateTime** | DateTime order was dispatched for fulfillment by FDC |  [optional] |
|**id** | **Integer** | FDC ID for this order |  |
|**merchant** | [**MerchantV2**](MerchantV2.md) |  |  |
|**merchantOrderId** | **String** | Merchant provided ID |  |
|**merchantShippingMethod** | **String** | Requested ship method |  |
|**originalConsignee** | [**ConsigneeV2**](ConsigneeV2.md) |  |  |
|**parentOrder** | [**OrderResponseV2ParentOrder**](OrderResponseV2ParentOrder.md) |  |  [optional] |
|**purchaseOrderNum** | **String** | Merchant provided PO# |  [optional] |
|**recordedOn** | **OffsetDateTime** | DateTime order was recorded by FDC |  |
|**trackingNumbers** | [**List&lt;TrackingNumberV2&gt;**](TrackingNumberV2.md) |  |  [optional] |
|**validatedConsignee** | **Object** |  |  |
|**warehouse** | [**WarehouseV2**](WarehouseV2.md) |  |  [optional] |



