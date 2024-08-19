# RocketServices.PaymentMethod

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **Number** | The balance of the wallet if the payment method is a wallet. | [optional] 
**brand** | **String** | The brand of the card if the payment method is a card. | [optional] 
**currency** | **String** | The currency code of the wallet if the payment method is a wallet. | [optional] 
**description** | **String** | A short description of a payment method.  If the payment method is of type &#x60;Wallet&#x60; this will be \&quot;My Wallet\&quot;  For &#x60;Card&#x60; type payment methods the format of this description may differ depending on the payment gateway in use. In the case of Stripe, this will be in the format \&quot;Visa (**** 4242, exp 08/19)\&quot;  | 
**expiryMonth** | **Number** | The expiry month of the card if the payment method is a card. | [optional] 
**expiryYear** | **Number** | The expiry year of the card if the payment method is a card. | [optional] 
**id** | **String** | The unique identifier of a payment method. | 
**lastDigits** | **Number** | The last digits of the card if the payment method is a card. Depending on the payment gateway in use this value may be undefined.  | [optional] 
**type** | **String** | The type of payment method. | 



## Enum: BrandEnum


* `Visa` (value: `"Visa"`)

* `MasterCard` (value: `"MasterCard"`)

* `AmericanExpress` (value: `"AmericanExpress"`)

* `Other` (value: `"Other"`)





## Enum: TypeEnum


* `Card` (value: `"Card"`)

* `Wallet` (value: `"Wallet"`)




