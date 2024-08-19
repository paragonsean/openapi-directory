# IncreaseApi.CheckDepositReturn

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The amount in the minor unit of the transaction&#39;s currency. For dollars, for example, this is cents. | 
**checkDepositId** | **String** | The identifier of the Check Deposit that was returned. | 
**currency** | **String** | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transaction&#39;s currency. | 
**returnReason** | **String** |  | 
**returnedAt** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the check deposit was returned. | 
**transactionId** | **String** | The identifier of the transaction that reversed the original check deposit transaction. | 



## Enum: CurrencyEnum


* `CAD` (value: `"CAD"`)

* `CHF` (value: `"CHF"`)

* `EUR` (value: `"EUR"`)

* `GBP` (value: `"GBP"`)

* `JPY` (value: `"JPY"`)

* `USD` (value: `"USD"`)





## Enum: ReturnReasonEnum


* `ach_conversion_not_supported` (value: `"ach_conversion_not_supported"`)

* `closed_account` (value: `"closed_account"`)

* `duplicate_submission` (value: `"duplicate_submission"`)

* `insufficient_funds` (value: `"insufficient_funds"`)

* `no_account` (value: `"no_account"`)

* `not_authorized` (value: `"not_authorized"`)

* `stale_dated` (value: `"stale_dated"`)

* `stop_payment` (value: `"stop_payment"`)

* `unknown_reason` (value: `"unknown_reason"`)

* `unmatched_details` (value: `"unmatched_details"`)

* `unreadable_image` (value: `"unreadable_image"`)




