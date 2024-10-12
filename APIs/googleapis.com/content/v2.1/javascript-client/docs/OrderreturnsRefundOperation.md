# ContentApiForShopping.OrderreturnsRefundOperation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fullRefund** | **Boolean** | If true, the item will be fully refunded. Allowed only when payment_type is FOP. Merchant can choose this refund option to indicate the full remaining amount of corresponding object to be refunded to the customer through FOP. | [optional] 
**partialRefund** | [**OrderreturnsPartialRefund**](OrderreturnsPartialRefund.md) |  | [optional] 
**paymentType** | **String** | The payment way of issuing refund. Default value is ORIGINAL_FOP if not set. | [optional] 
**reasonText** | **String** | The explanation of the reason. | [optional] 
**returnRefundReason** | **String** | Code of the refund reason. | [optional] 


