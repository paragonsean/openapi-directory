

# OrderRefundAdd


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**date** | **String** | Specifies an order creation date in format Y-m-d H:i:s |  [optional] |
|**feePrice** | **BigDecimal** | Specifies refund&#39;s fee price |  [optional] |
|**isOnline** | **Boolean** | Indicates whether refund type is online |  [optional] |
|**itemRestock** | **Boolean** | Boolean, whether or not to add the line items back to the store inventory. |  [optional] |
|**items** | [**List&lt;OrderRefundAddItemsInner&gt;**](OrderRefundAddItemsInner.md) | Defines items in the order that will be refunded |  [optional] |
|**message** | **String** | Refund reason, or some else message which assigned to refund. |  [optional] |
|**orderId** | **String** | Defines the order for which the refund will be created. |  [optional] |
|**sendNotifications** | **Boolean** | Send notifications to customer after refund was created |  [optional] |
|**shippingPrice** | **BigDecimal** | Defines refund shipping amount. |  [optional] |
|**totalPrice** | **BigDecimal** | Defines order refund amount. |  [optional] |



