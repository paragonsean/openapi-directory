

# MerchantOrderReturnItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customerReturnReason** | [**CustomerReturnReason**](CustomerReturnReason.md) |  |  [optional] |
|**itemId** | **String** | Product level item ID. If the returned items are of the same product, they will have the same ID. |  [optional] |
|**merchantReturnReason** | [**RefundReason**](RefundReason.md) |  |  [optional] |
|**product** | [**OrderLineItemProduct**](OrderLineItemProduct.md) |  |  [optional] |
|**returnShipmentIds** | **List&lt;String&gt;** | IDs of the return shipments that this return item belongs to. |  [optional] |
|**state** | **String** | State of the item. Acceptable values are: - \&quot;&#x60;canceled&#x60;\&quot; - \&quot;&#x60;new&#x60;\&quot; - \&quot;&#x60;received&#x60;\&quot; - \&quot;&#x60;refunded&#x60;\&quot; - \&quot;&#x60;rejected&#x60;\&quot;  |  [optional] |



