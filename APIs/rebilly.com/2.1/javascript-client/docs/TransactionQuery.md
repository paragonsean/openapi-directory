# RebillyRestApi.TransactionQuery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The transaction&#39;s amount. | [optional] [readonly] 
**currency** | **String** | ISO 4217 alphabetic currency code. | [optional] [readonly] 
**result** | **String** | Transaction result. | [optional] [readonly] 
**status** | **String** | Transaction status. | [optional] [readonly] 



## Enum: ResultEnum


* `abandoned` (value: `"abandoned"`)

* `approved` (value: `"approved"`)

* `canceled` (value: `"canceled"`)

* `declined` (value: `"declined"`)

* `unknown` (value: `"unknown"`)





## Enum: StatusEnum


* `completed` (value: `"completed"`)

* `conn-error` (value: `"conn-error"`)

* `disputed` (value: `"disputed"`)

* `never-sent` (value: `"never-sent"`)

* `offsite` (value: `"offsite"`)

* `partially-refunded` (value: `"partially-refunded"`)

* `pending` (value: `"pending"`)

* `refunded` (value: `"refunded"`)

* `sending` (value: `"sending"`)

* `suspended` (value: `"suspended"`)

* `timeout` (value: `"timeout"`)

* `voided` (value: `"voided"`)

* `waiting-approval` (value: `"waiting-approval"`)

* `waiting-capture` (value: `"waiting-capture"`)

* `waiting-gateway` (value: `"waiting-gateway"`)

* `waiting-refund` (value: `"waiting-refund"`)




