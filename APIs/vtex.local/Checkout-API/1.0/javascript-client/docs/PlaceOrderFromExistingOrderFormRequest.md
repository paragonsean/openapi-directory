# CheckoutApi.PlaceOrderFromExistingOrderFormRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interestValue** | **Number** | Interest rate to be used in case it applies. | [default to 0]
**optinNewsLetter** | **Boolean** | True if the shopper opted to receive the newsletter. | [optional] [default to false]
**referenceId** | **String** | ID of the &#x60;orderForm&#x60; corresponding to the cart from which to place the order. This is the same as the &#x60;orderFormId&#x60; parameter. | [default to &#39;41a22925298a4ddca95318131a25b000&#39;]
**referenceValue** | **Number** | Reference value of the order for calculating interest if that is the case. Can be equal to the total value and does not separate cents. For example, $24.99 is represented &#x60;2499&#x60;. | [default to 6800]
**savePersonalData** | **Boolean** | &#x60;true&#x60; if the shopper&#39;s data provided during checkout should be saved for future reference. | [optional] [default to false]
**value** | **Number** | Total value of the order without separating cents. For example, $24.99 is represented &#x60;2499&#x60;. | [default to 6800]


