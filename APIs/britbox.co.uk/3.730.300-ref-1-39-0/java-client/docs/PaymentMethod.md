

# PaymentMethod


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**balance** | **Float** | The balance of the wallet if the payment method is a wallet. |  [optional] |
|**brand** | [**BrandEnum**](#BrandEnum) | The brand of the card if the payment method is a card. |  [optional] |
|**currency** | **String** | The currency code of the wallet if the payment method is a wallet. |  [optional] |
|**description** | **String** | A short description of a payment method.  If the payment method is of type &#x60;Wallet&#x60; this will be \&quot;My Wallet\&quot;  For &#x60;Card&#x60; type payment methods the format of this description may differ depending on the payment gateway in use. In the case of Stripe, this will be in the format \&quot;Visa (**** 4242, exp 08/19)\&quot;  |  |
|**expiryMonth** | **BigDecimal** | The expiry month of the card if the payment method is a card. |  [optional] |
|**expiryYear** | **BigDecimal** | The expiry year of the card if the payment method is a card. |  [optional] |
|**id** | **String** | The unique identifier of a payment method. |  |
|**lastDigits** | **BigDecimal** | The last digits of the card if the payment method is a card. Depending on the payment gateway in use this value may be undefined.  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of payment method. |  |



## Enum: BrandEnum

| Name | Value |
|---- | -----|
| VISA | &quot;Visa&quot; |
| MASTER_CARD | &quot;MasterCard&quot; |
| AMERICAN_EXPRESS | &quot;AmericanExpress&quot; |
| OTHER | &quot;Other&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CARD | &quot;Card&quot; |
| WALLET | &quot;Wallet&quot; |



