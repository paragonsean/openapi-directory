

# CardRevenuePayment

A Card Revenue Payment object. This field will be present in the JSON response if and only if `category` is equal to `card_revenue_payment`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Integer** | The amount in the minor unit of the transaction&#39;s currency. For dollars, for example, this is cents. |  |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transaction currency. |  |
|**periodEnd** | **OffsetDateTime** | The end of the period for which this transaction paid interest. |  |
|**periodStart** | **OffsetDateTime** | The start of the period for which this transaction paid interest. |  |
|**transactedOnAccountId** | **String** | The account the card belonged to. |  |



## Enum: CurrencyEnum

| Name | Value |
|---- | -----|
| CAD | &quot;CAD&quot; |
| CHF | &quot;CHF&quot; |
| EUR | &quot;EUR&quot; |
| GBP | &quot;GBP&quot; |
| JPY | &quot;JPY&quot; |
| USD | &quot;USD&quot; |



