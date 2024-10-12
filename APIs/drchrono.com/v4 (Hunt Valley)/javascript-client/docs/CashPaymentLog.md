# OpenapiJsClient.CashPaymentLog

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | &#x60;C&#x60;(Create), &#x60;U&#x60;(Update), &#x60;D&#x60;(Delete), &#x60;F&#x60;(Fill), &#x60;A&#x60;(Autofill) | [optional] 
**amount** | **Number** |  | [optional] 
**appointment** | **String** | ID of appointment associated with the payment | [optional] [readonly] 
**createdBy** | **String** | ID of user who created the payment | [optional] [readonly] 
**doctor** | **String** |  | [optional] [readonly] 
**id** | **Number** |  | [optional] [readonly] 
**patient** | **String** |  | [optional] [readonly] 
**paymentMethod** | **String** | &#x60;\&quot;CASH\&quot;, \&quot;CHCK\&quot; for Check, \&quot;DBIT\&quot; for Debit, \&quot;CRDT\&quot; for Credit Card, \&quot;AMEX\&quot; for American Express, \&quot;VISA\&quot;, \&quot;MSTR\&quot; for Mastercard, \&quot;DISC\&quot; for Discover, \&quot;SQR1\&quot; for Square (legacy), \&quot;SQRE\&quot; for Square, \&quot;PTPA\&quot; for Patient Payments, \&quot;ONPT\&quot; for onpatient, \&quot;OTHR\&quot; for Other&#x60; | [optional] 
**source** | **String** |  | [optional] 
**updatedAt** | **String** |  | [optional] 



## Enum: ActionEnum


* `C` (value: `"C"`)

* `U` (value: `"U"`)

* `D` (value: `"D"`)

* `F` (value: `"F"`)

* `A` (value: `"A"`)





## Enum: PaymentMethodEnum


* `CASH` (value: `"CASH"`)

* `CHCK` (value: `"CHCK"`)

* `DBIT` (value: `"DBIT"`)

* `CRDT` (value: `"CRDT"`)

* `AMEX` (value: `"AMEX"`)

* `VISA` (value: `"VISA"`)

* `MSTR` (value: `"MSTR"`)

* `DISC` (value: `"DISC"`)

* `SQR1` (value: `"SQR1"`)

* `SQRE` (value: `"SQRE"`)

* `PTPA` (value: `"PTPA"`)

* `ONPT` (value: `"ONPT"`)

* `OTHR` (value: `"OTHR"`)




