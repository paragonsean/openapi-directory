

# PlaceOrderFromExistingOrderFormRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**interestValue** | **Integer** | Interest rate to be used in case it applies. |  |
|**optinNewsLetter** | **Boolean** | True if the shopper opted to receive the newsletter. |  [optional] |
|**referenceId** | **String** | ID of the &#x60;orderForm&#x60; corresponding to the cart from which to place the order. This is the same as the &#x60;orderFormId&#x60; parameter. |  |
|**referenceValue** | **Integer** | Reference value of the order for calculating interest if that is the case. Can be equal to the total value and does not separate cents. For example, $24.99 is represented &#x60;2499&#x60;. |  |
|**savePersonalData** | **Boolean** | &#x60;true&#x60; if the shopper&#39;s data provided during checkout should be saved for future reference. |  [optional] |
|**value** | **Integer** | Total value of the order without separating cents. For example, $24.99 is represented &#x60;2499&#x60;. |  |



