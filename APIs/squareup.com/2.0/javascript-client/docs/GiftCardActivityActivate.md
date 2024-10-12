# SquareConnectApi.GiftCardActivityActivate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amountMoney** | [**Money**](Money.md) |  | [optional] 
**buyerPaymentInstrumentIds** | **[String]** | Required if your application does not use the Square Orders API.  This is a list of client-provided payment instrument IDs.  Square uses this information to perform compliance checks. If you use the Square Orders API, Square has the necessary instrument IDs to perform necessary  compliance checks. | [optional] 
**lineItemUid** | **String** | The &#x60;line_item_uid&#x60; of the gift card line item in an order.  This is required if your application uses the Square Orders API. | [optional] 
**orderId** | **String** | The ID of the order associated with the activity.  This is required if your application uses the Square Orders API. | [optional] 
**referenceId** | **String** | If your application does not use the Square Orders API, you can optionally use this field  to associate the gift card activity with a client-side entity. | [optional] 


