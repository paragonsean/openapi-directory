# ContentApiForShopping.OrdersRefundOrderRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**MonetaryAmount**](MonetaryAmount.md) |  | [optional] 
**fullRefund** | **Boolean** | If true, the full order will be refunded, including shipping. If this is true, amount shouldn&#39;t be provided and will be ignored. | [optional] 
**operationId** | **String** | The ID of the operation. Unique across all operations for a given order. | [optional] 
**reason** | **String** | The reason for the refund. Acceptable values are: - \&quot;&#x60;courtesyAdjustment&#x60;\&quot; - \&quot;&#x60;other&#x60;\&quot;  | [optional] 
**reasonText** | **String** | The explanation of the reason. | [optional] 


