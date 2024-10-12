# OpenapiJsClient.CashPayment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | Amount of cash for this payment, cannot be zero | [optional] 
**appointment** | **Number** | If this is absent, the apponitment will be inferred from line item | [optional] 
**createdAt** | **String** |  | [optional] [readonly] 
**createdBy** | **String** |  | [optional] [readonly] 
**doctor** | **Number** |  | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**lineItem** | **Number** |  | [optional] 
**notes** | **String** |  | [optional] 
**patient** | **Number** |  | 
**paymentMethod** | **String** | &#x60;\&quot;CASH\&quot;, \&quot;CHCK\&quot; for Check, \&quot;DBIT\&quot; for Debit, \&quot;CRDT\&quot; for Credit Card, \&quot;AMEX\&quot; for American Express, \&quot;VISA\&quot;, \&quot;MSTR\&quot; for Mastercard, \&quot;DISC\&quot; for Discover, \&quot;SQR1\&quot; for Square (legacy), \&quot;SQRE\&quot; for Square, \&quot;PTPA\&quot; for Patient Payments, \&quot;ONPT\&quot; for onpatient, \&quot;OTHR\&quot; for Other&#x60; | [optional] 
**paymentTransactionType** | **String** | &#x60;\&quot;\&quot; for Credit, \&quot;REF\&quot; for Refund, \&quot;COR\&quot; for Correction, \&quot;COPAY\&quot; for Copay, \&quot;COINSR\&quot; for Coinsurance, \&quot;OTHR\&quot; for Other&#x60; | [optional] 
**postedDate** | **String** |  | [optional] [readonly] 
**receivedDate** | **String** |  | [optional] 
**traceNumber** | **String** |  | [optional] 
**updatedAt** | **String** |  | [optional] [readonly] 



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





## Enum: PaymentTransactionTypeEnum


* `empty` (value: `""`)

* `REF` (value: `"REF"`)

* `COR` (value: `"COR"`)

* `COPAY` (value: `"COPAY"`)

* `COINSR` (value: `"COINSR"`)

* `OTHR` (value: `"OTHR"`)




