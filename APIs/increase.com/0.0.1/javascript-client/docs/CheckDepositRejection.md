# IncreaseApi.CheckDepositRejection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The rejected amount in the minor unit of check&#39;s currency. For dollars, for example, this is cents. | 
**currency** | **String** | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the check&#39;s currency. | 
**reason** | **String** | Why the check deposit was rejected. | 
**rejectedAt** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the check deposit was rejected. | 



## Enum: CurrencyEnum


* `CAD` (value: `"CAD"`)

* `CHF` (value: `"CHF"`)

* `EUR` (value: `"EUR"`)

* `GBP` (value: `"GBP"`)

* `JPY` (value: `"JPY"`)

* `USD` (value: `"USD"`)





## Enum: ReasonEnum


* `incomplete_image` (value: `"incomplete_image"`)

* `duplicate` (value: `"duplicate"`)

* `poor_image_quality` (value: `"poor_image_quality"`)

* `incorrect_amount` (value: `"incorrect_amount"`)

* `incorrect_recipient` (value: `"incorrect_recipient"`)

* `not_eligible_for_mobile_deposit` (value: `"not_eligible_for_mobile_deposit"`)

* `unknown` (value: `"unknown"`)




