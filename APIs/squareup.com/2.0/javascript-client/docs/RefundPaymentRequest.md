# SquareConnectApi.RefundPaymentRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amountMoney** | [**Money**](Money.md) |  | 
**appFeeMoney** | [**Money**](Money.md) |  | [optional] 
**idempotencyKey** | **String** |  A unique string that identifies this &#x60;RefundPayment&#x60; request. The key can be any valid string but must be unique for every &#x60;RefundPayment&#x60; request.  For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency). | 
**paymentId** | **String** | The unique ID of the payment being refunded. | 
**reason** | **String** | A description of the reason for the refund. | [optional] 


