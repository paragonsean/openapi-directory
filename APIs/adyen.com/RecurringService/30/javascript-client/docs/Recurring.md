# AdyenRecurringApi.Recurring

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract** | **String** | The type of recurring contract to be used. Possible values: * &#x60;ONECLICK&#x60; – Payment details can be used to initiate a one-click payment, where the shopper enters the [card security code (CVC/CVV)](https://docs.adyen.com/payments-fundamentals/payment-glossary#card-security-code-cvc-cvv-cid). * &#x60;RECURRING&#x60; – Payment details can be used without the card security code to initiate [card-not-present transactions](https://docs.adyen.com/payments-fundamentals/payment-glossary#card-not-present-cnp). * &#x60;ONECLICK,RECURRING&#x60; – Payment details can be used regardless of whether the shopper is on your site or not. * &#x60;PAYOUT&#x60; – Payment details can be used to [make a payout](https://docs.adyen.com/online-payments/online-payouts). | [optional] 
**recurringDetailName** | **String** | A descriptive name for this detail. | [optional] 
**tokenService** | **String** | The name of the token service. | [optional] 



## Enum: ContractEnum


* `ONECLICK` (value: `"ONECLICK"`)

* `RECURRING` (value: `"RECURRING"`)

* `PAYOUT` (value: `"PAYOUT"`)





## Enum: TokenServiceEnum


* `VISATOKENSERVICE` (value: `"VISATOKENSERVICE"`)

* `MCTOKENSERVICE` (value: `"MCTOKENSERVICE"`)

* `AMEXTOKENSERVICE` (value: `"AMEXTOKENSERVICE"`)

* `TOKEN_SHARING` (value: `"TOKEN_SHARING"`)




