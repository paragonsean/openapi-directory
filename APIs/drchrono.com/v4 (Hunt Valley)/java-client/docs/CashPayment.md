

# CashPayment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **BigDecimal** | Amount of cash for this payment, cannot be zero |  [optional] |
|**appointment** | **Integer** | If this is absent, the apponitment will be inferred from line item |  [optional] |
|**createdAt** | **String** |  |  [optional] [readonly] |
|**createdBy** | **String** |  |  [optional] [readonly] |
|**doctor** | **Integer** |  |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**lineItem** | **Integer** |  |  [optional] |
|**notes** | **String** |  |  [optional] |
|**patient** | **Integer** |  |  |
|**paymentMethod** | [**PaymentMethodEnum**](#PaymentMethodEnum) | &#x60;\&quot;CASH\&quot;, \&quot;CHCK\&quot; for Check, \&quot;DBIT\&quot; for Debit, \&quot;CRDT\&quot; for Credit Card, \&quot;AMEX\&quot; for American Express, \&quot;VISA\&quot;, \&quot;MSTR\&quot; for Mastercard, \&quot;DISC\&quot; for Discover, \&quot;SQR1\&quot; for Square (legacy), \&quot;SQRE\&quot; for Square, \&quot;PTPA\&quot; for Patient Payments, \&quot;ONPT\&quot; for onpatient, \&quot;OTHR\&quot; for Other&#x60; |  [optional] |
|**paymentTransactionType** | [**PaymentTransactionTypeEnum**](#PaymentTransactionTypeEnum) | &#x60;\&quot;\&quot; for Credit, \&quot;REF\&quot; for Refund, \&quot;COR\&quot; for Correction, \&quot;COPAY\&quot; for Copay, \&quot;COINSR\&quot; for Coinsurance, \&quot;OTHR\&quot; for Other&#x60; |  [optional] |
|**postedDate** | **String** |  |  [optional] [readonly] |
|**receivedDate** | **String** |  |  [optional] |
|**traceNumber** | **String** |  |  [optional] |
|**updatedAt** | **String** |  |  [optional] [readonly] |



## Enum: PaymentMethodEnum

| Name | Value |
|---- | -----|
| CASH | &quot;CASH&quot; |
| CHCK | &quot;CHCK&quot; |
| DBIT | &quot;DBIT&quot; |
| CRDT | &quot;CRDT&quot; |
| AMEX | &quot;AMEX&quot; |
| VISA | &quot;VISA&quot; |
| MSTR | &quot;MSTR&quot; |
| DISC | &quot;DISC&quot; |
| SQR1 | &quot;SQR1&quot; |
| SQRE | &quot;SQRE&quot; |
| PTPA | &quot;PTPA&quot; |
| ONPT | &quot;ONPT&quot; |
| OTHR | &quot;OTHR&quot; |



## Enum: PaymentTransactionTypeEnum

| Name | Value |
|---- | -----|
| EMPTY | &quot;&quot; |
| REF | &quot;REF&quot; |
| COR | &quot;COR&quot; |
| COPAY | &quot;COPAY&quot; |
| COINSR | &quot;COINSR&quot; |
| OTHR | &quot;OTHR&quot; |



