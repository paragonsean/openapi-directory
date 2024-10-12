# CallFireApiDocumentation.NumberLease

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoRenew** | **Boolean** | Enables the auto renewal of number lease at end of each billing cycle | [optional] 
**callFeatureStatus** | **String** | A status of a call feature. Available values: DISABLED, ENABLED | [optional] 
**labels** | **[String]** | ~ | [optional] 
**leaseBegin** | **Number** | A date and time of a lease start. Timestamp, formatted in unix time milliseconds (read only). Example: 1473781817000 | [optional] 
**leaseEnd** | **Number** | A data and time of a lease finish. Timestamp, formatted in unix time milliseconds (read only). Example: 1473781817000 | [optional] 
**nationalFormat** | **String** | Formatted number with a country code | [optional] 
**number** | **String** | A phone number in E.164 format (11-digit). Example: 12132000384 | [optional] 
**region** | [**Region**](Region.md) |  | [optional] 
**sendEmailOnCreate** | **Boolean** | ~ | [optional] 
**status** | **String** | A lease status. Available values: PENDING, ACTIVE, RELEASED, UNAVAILABLE | [optional] [readonly] 
**textFeatureStatus** | **String** | A status of a text feature. Available values: DISABLED, ENABLED | [optional] 
**tollFree** | **Boolean** | A  toll-free number | [optional] 
**type** | **String** | ~ | [optional] 



## Enum: CallFeatureStatusEnum


* `UNSUPPORTED` (value: `"UNSUPPORTED"`)

* `PENDING` (value: `"PENDING"`)

* `DISABLED` (value: `"DISABLED"`)

* `ENABLED` (value: `"ENABLED"`)





## Enum: StatusEnum


* `PENDING` (value: `"PENDING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `RELEASED` (value: `"RELEASED"`)

* `UNAVAILABLE` (value: `"UNAVAILABLE"`)





## Enum: TextFeatureStatusEnum


* `UNSUPPORTED` (value: `"UNSUPPORTED"`)

* `PENDING` (value: `"PENDING"`)

* `DISABLED` (value: `"DISABLED"`)

* `ENABLED` (value: `"ENABLED"`)





## Enum: TypeEnum


* `PLAN` (value: `"PLAN"`)

* `EXTRA` (value: `"EXTRA"`)




