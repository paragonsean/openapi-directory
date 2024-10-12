# BigQueryReservationApi.CapacityCommitment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commitmentEndTime** | **String** | Output only. The end of the current commitment period. It is applicable only for ACTIVE capacity commitments. | [optional] [readonly] 
**commitmentStartTime** | **String** | Output only. The start of the current commitment period. It is applicable only for ACTIVE capacity commitments. | [optional] [readonly] 
**edition** | **String** | Edition of the capacity commitment. | [optional] 
**failureStatus** | [**Status**](Status.md) |  | [optional] 
**isFlatRate** | **Boolean** | Output only. If true, the commitment is a flat-rate commitment, otherwise, it&#39;s an edition commitment. | [optional] [readonly] 
**multiRegionAuxiliary** | **Boolean** | Applicable only for commitments located within one of the BigQuery multi-regions (US or EU). If set to true, this commitment is placed in the organization&#39;s secondary region which is designated for disaster recovery purposes. If false, this commitment is placed in the organization&#39;s default region. NOTE: this is a preview feature. Project must be allow-listed in order to set this field. | [optional] 
**name** | **String** | Output only. The resource name of the capacity commitment, e.g., &#x60;projects/myproject/locations/US/capacityCommitments/123&#x60; The commitment_id must only contain lower case alphanumeric characters or dashes. It must start with a letter and must not end with a dash. Its maximum length is 64 characters. | [optional] [readonly] 
**plan** | **String** | Capacity commitment commitment plan. | [optional] 
**renewalPlan** | **String** | The plan this capacity commitment is converted to after commitment_end_time passes. Once the plan is changed, committed period is extended according to commitment plan. Only applicable for ANNUAL and TRIAL commitments. | [optional] 
**slotCount** | **String** | Number of slots in this commitment. | [optional] 
**state** | **String** | Output only. State of the commitment. | [optional] [readonly] 



## Enum: EditionEnum


* `EDITION_UNSPECIFIED` (value: `"EDITION_UNSPECIFIED"`)

* `STANDARD` (value: `"STANDARD"`)

* `ENTERPRISE` (value: `"ENTERPRISE"`)

* `ENTERPRISE_PLUS` (value: `"ENTERPRISE_PLUS"`)





## Enum: PlanEnum


* `COMMITMENT_PLAN_UNSPECIFIED` (value: `"COMMITMENT_PLAN_UNSPECIFIED"`)

* `FLEX` (value: `"FLEX"`)

* `FLEX_FLAT_RATE` (value: `"FLEX_FLAT_RATE"`)

* `TRIAL` (value: `"TRIAL"`)

* `MONTHLY` (value: `"MONTHLY"`)

* `MONTHLY_FLAT_RATE` (value: `"MONTHLY_FLAT_RATE"`)

* `ANNUAL` (value: `"ANNUAL"`)

* `ANNUAL_FLAT_RATE` (value: `"ANNUAL_FLAT_RATE"`)

* `THREE_YEAR` (value: `"THREE_YEAR"`)

* `NONE` (value: `"NONE"`)





## Enum: RenewalPlanEnum


* `COMMITMENT_PLAN_UNSPECIFIED` (value: `"COMMITMENT_PLAN_UNSPECIFIED"`)

* `FLEX` (value: `"FLEX"`)

* `FLEX_FLAT_RATE` (value: `"FLEX_FLAT_RATE"`)

* `TRIAL` (value: `"TRIAL"`)

* `MONTHLY` (value: `"MONTHLY"`)

* `MONTHLY_FLAT_RATE` (value: `"MONTHLY_FLAT_RATE"`)

* `ANNUAL` (value: `"ANNUAL"`)

* `ANNUAL_FLAT_RATE` (value: `"ANNUAL_FLAT_RATE"`)

* `THREE_YEAR` (value: `"THREE_YEAR"`)

* `NONE` (value: `"NONE"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `FAILED` (value: `"FAILED"`)




