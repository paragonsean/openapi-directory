

# InternalSource

A Internal Source object. This field will be present in the JSON response if and only if `category` is equal to `internal_source`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Integer** | The amount in the minor unit of the transaction&#39;s currency. For dollars, for example, this is cents. |  |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transaction currency. |  |
|**reason** | [**ReasonEnum**](#ReasonEnum) |  |  |



## Enum: CurrencyEnum

| Name | Value |
|---- | -----|
| CAD | &quot;CAD&quot; |
| CHF | &quot;CHF&quot; |
| EUR | &quot;EUR&quot; |
| GBP | &quot;GBP&quot; |
| JPY | &quot;JPY&quot; |
| USD | &quot;USD&quot; |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| BANK_MIGRATION | &quot;bank_migration&quot; |
| CASHBACK | &quot;cashback&quot; |
| EMPYREAL_ADJUSTMENT | &quot;empyreal_adjustment&quot; |
| ERROR | &quot;error&quot; |
| ERROR_CORRECTION | &quot;error_correction&quot; |
| FEES | &quot;fees&quot; |
| INTEREST | &quot;interest&quot; |
| SAMPLE_FUNDS | &quot;sample_funds&quot; |
| SAMPLE_FUNDS_RETURN | &quot;sample_funds_return&quot; |



