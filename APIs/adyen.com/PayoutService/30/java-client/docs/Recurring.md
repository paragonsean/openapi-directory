

# Recurring


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contract** | [**ContractEnum**](#ContractEnum) | The type of recurring contract to be used. Possible values: * &#x60;ONECLICK&#x60; – Payment details can be used to initiate a one-click payment, where the shopper enters the [card security code (CVC/CVV)](https://docs.adyen.com/payments-fundamentals/payment-glossary#card-security-code-cvc-cvv-cid). * &#x60;RECURRING&#x60; – Payment details can be used without the card security code to initiate [card-not-present transactions](https://docs.adyen.com/payments-fundamentals/payment-glossary#card-not-present-cnp). * &#x60;ONECLICK,RECURRING&#x60; – Payment details can be used regardless of whether the shopper is on your site or not. * &#x60;PAYOUT&#x60; – Payment details can be used to [make a payout](https://docs.adyen.com/online-payments/online-payouts). |  [optional] |
|**recurringDetailName** | **String** | A descriptive name for this detail. |  [optional] |
|**tokenService** | [**TokenServiceEnum**](#TokenServiceEnum) | The name of the token service. |  [optional] |



## Enum: ContractEnum

| Name | Value |
|---- | -----|
| ONECLICK | &quot;ONECLICK&quot; |
| RECURRING | &quot;RECURRING&quot; |
| PAYOUT | &quot;PAYOUT&quot; |



## Enum: TokenServiceEnum

| Name | Value |
|---- | -----|
| VISATOKENSERVICE | &quot;VISATOKENSERVICE&quot; |
| MCTOKENSERVICE | &quot;MCTOKENSERVICE&quot; |
| AMEXTOKENSERVICE | &quot;AMEXTOKENSERVICE&quot; |
| TOKEN_SHARING | &quot;TOKEN_SHARING&quot; |



