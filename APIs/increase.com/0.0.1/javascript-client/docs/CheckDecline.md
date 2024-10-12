# IncreaseApi.CheckDecline

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The declined amount in the minor unit of the destination account currency. For dollars, for example, this is cents. | 
**auxiliaryOnUs** | **String** |  | 
**reason** | **String** | Why the check was declined. | 



## Enum: ReasonEnum


* `ach_route_canceled` (value: `"ach_route_canceled"`)

* `ach_route_disabled` (value: `"ach_route_disabled"`)

* `breaches_limit` (value: `"breaches_limit"`)

* `entity_not_active` (value: `"entity_not_active"`)

* `group_locked` (value: `"group_locked"`)

* `insufficient_funds` (value: `"insufficient_funds"`)

* `unable_to_locate_account` (value: `"unable_to_locate_account"`)

* `unable_to_process` (value: `"unable_to_process"`)

* `refer_to_image` (value: `"refer_to_image"`)

* `stop_payment_requested` (value: `"stop_payment_requested"`)

* `returned` (value: `"returned"`)

* `duplicate_presentment` (value: `"duplicate_presentment"`)

* `not_authorized` (value: `"not_authorized"`)




