# SquareConnectApi.GiftCardActivityRefund

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amountMoney** | [**Money**](Money.md) |  | [optional] 
**paymentId** | **String** | When the Square Payments API is used, Refund is not called on the Gift Cards API. However, when Square reads a Refund activity from the Gift Cards API, the developer needs to know the ID of the payment (made using this gift card) that is being refunded. | [optional] 
**redeemActivityId** | **String** | The ID for the Redeem activity that needs to be refunded. Hence, the activity it refers to has to be of the REDEEM type. | 
**referenceId** | **String** | A client-specified ID to associate an entity, in another system, with this gift card activity. This can be used to track the order or payment related information when the Square Orders API is not being used. | [optional] 


