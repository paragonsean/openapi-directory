# RebillyRestApi.SubscriptionCancellationState

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancelCategory** | **String** | Cancel category. | [optional] [readonly] 
**cancelDescription** | **String** | Cancel reason description in free form. | [optional] [readonly] 
**canceledBy** | **String** | Canceled by. | [optional] [readonly] 
**canceledTime** | **Date** | Subscription order canceled time. | [optional] [readonly] 



## Enum: CancelCategoryEnum


* `billing-failure` (value: `"billing-failure"`)

* `did-not-use` (value: `"did-not-use"`)

* `did-not-want` (value: `"did-not-want"`)

* `missing-features` (value: `"missing-features"`)

* `bugs-or-problems` (value: `"bugs-or-problems"`)

* `do-not-remember` (value: `"do-not-remember"`)

* `risk-warning` (value: `"risk-warning"`)

* `contract-expired` (value: `"contract-expired"`)

* `too-expensive` (value: `"too-expensive"`)

* `never-started` (value: `"never-started"`)

* `switched-plan` (value: `"switched-plan"`)

* `other` (value: `"other"`)





## Enum: CanceledByEnum


* `merchant` (value: `"merchant"`)

* `customer` (value: `"customer"`)

* `rebilly` (value: `"rebilly"`)




