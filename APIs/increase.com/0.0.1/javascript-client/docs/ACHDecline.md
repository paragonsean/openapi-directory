# IncreaseApi.ACHDecline

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The declined amount in the minor unit of the destination account currency. For dollars, for example, this is cents. | 
**originatorCompanyDescriptiveDate** | **String** |  | 
**originatorCompanyDiscretionaryData** | **String** |  | 
**originatorCompanyId** | **String** |  | 
**originatorCompanyName** | **String** |  | 
**reason** | **String** | Why the ACH transfer was declined. | 
**receiverIdNumber** | **String** |  | 
**receiverName** | **String** |  | 
**traceNumber** | **String** |  | 



## Enum: ReasonEnum


* `ach_route_canceled` (value: `"ach_route_canceled"`)

* `ach_route_disabled` (value: `"ach_route_disabled"`)

* `breaches_limit` (value: `"breaches_limit"`)

* `credit_entry_refused_by_receiver` (value: `"credit_entry_refused_by_receiver"`)

* `duplicate_return` (value: `"duplicate_return"`)

* `entity_not_active` (value: `"entity_not_active"`)

* `group_locked` (value: `"group_locked"`)

* `insufficient_funds` (value: `"insufficient_funds"`)

* `misrouted_return` (value: `"misrouted_return"`)

* `no_ach_route` (value: `"no_ach_route"`)

* `originator_request` (value: `"originator_request"`)

* `transaction_not_allowed` (value: `"transaction_not_allowed"`)




