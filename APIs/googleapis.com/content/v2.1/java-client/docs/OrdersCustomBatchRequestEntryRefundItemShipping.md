

# OrdersCustomBatchRequestEntryRefundItemShipping


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | [**Price**](Price.md) |  |  [optional] |
|**fullRefund** | **Boolean** | If set to true, all shipping costs for the order will be refunded. If this is true, amount shouldn&#39;t be provided and will be ignored. If set to false, submit the amount of the partial shipping refund, excluding the shipping tax. The shipping tax is calculated and handled on Google&#39;s side. |  [optional] |



