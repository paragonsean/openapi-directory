

# ReversalRequest

It conveys Information related to the reversal of a previous payment or a loyalty transaction. Content of the Reversal Request message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customerOrder** | [**CustomerOrder**](CustomerOrder.md) |  |  [optional] |
|**originalPOITransaction** | [**OriginalPOITransaction**](OriginalPOITransaction.md) |  |  |
|**reversalReason** | **ReversalReason** |  |  |
|**reversedAmount** | **BigDecimal** | ReversedAmount is implicitely the AuthorizedAmount if absent. |  [optional] |
|**saleData** | [**SaleData**](SaleData.md) |  |  [optional] |



