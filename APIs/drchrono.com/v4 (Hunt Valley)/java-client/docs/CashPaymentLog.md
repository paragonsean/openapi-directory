

# CashPaymentLog


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) | &#x60;C&#x60;(Create), &#x60;U&#x60;(Update), &#x60;D&#x60;(Delete), &#x60;F&#x60;(Fill), &#x60;A&#x60;(Autofill) |  [optional] |
|**amount** | **BigDecimal** |  |  [optional] |
|**appointment** | **String** | ID of appointment associated with the payment |  [optional] [readonly] |
|**createdBy** | **String** | ID of user who created the payment |  [optional] [readonly] |
|**doctor** | **String** |  |  [optional] [readonly] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**patient** | **String** |  |  [optional] [readonly] |
|**paymentMethod** | [**PaymentMethodEnum**](#PaymentMethodEnum) | &#x60;\&quot;CASH\&quot;, \&quot;CHCK\&quot; for Check, \&quot;DBIT\&quot; for Debit, \&quot;CRDT\&quot; for Credit Card, \&quot;AMEX\&quot; for American Express, \&quot;VISA\&quot;, \&quot;MSTR\&quot; for Mastercard, \&quot;DISC\&quot; for Discover, \&quot;SQR1\&quot; for Square (legacy), \&quot;SQRE\&quot; for Square, \&quot;PTPA\&quot; for Patient Payments, \&quot;ONPT\&quot; for onpatient, \&quot;OTHR\&quot; for Other&#x60; |  [optional] |
|**source** | **String** |  |  [optional] |
|**updatedAt** | **String** |  |  [optional] |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| C | &quot;C&quot; |
| U | &quot;U&quot; |
| D | &quot;D&quot; |
| F | &quot;F&quot; |
| A | &quot;A&quot; |



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



