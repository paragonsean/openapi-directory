

# FeePayment

A Fee Payment object. This field will be present in the JSON response if and only if `category` is equal to `fee_payment`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Integer** | The amount in the minor unit of the transaction&#39;s currency. For dollars, for example, this is cents. |  |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transaction currency. |  |



## Enum: CurrencyEnum

| Name | Value |
|---- | -----|
| CAD | &quot;CAD&quot; |
| CHF | &quot;CHF&quot; |
| EUR | &quot;EUR&quot; |
| GBP | &quot;GBP&quot; |
| JPY | &quot;JPY&quot; |
| USD | &quot;USD&quot; |



