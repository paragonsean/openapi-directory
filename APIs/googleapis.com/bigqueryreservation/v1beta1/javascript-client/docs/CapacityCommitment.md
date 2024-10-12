# BigQueryReservationApi.CapacityCommitment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commitmentEndTime** | **String** | Output only. The end of the current commitment period. It is applicable only for ACTIVE capacity commitments. | [optional] [readonly] 
**commitmentStartTime** | **String** | Output only. The start of the current commitment period. It is applicable only for ACTIVE capacity commitments. | [optional] [readonly] 
**failureStatus** | [**Status**](Status.md) |  | [optional] 
**multiRegionAuxiliary** | **Boolean** | Applicable only for commitments located within one of the BigQuery multi-regions (US or EU). If set to true, this commitment is placed in the organization&#39;s secondary region which is designated for disaster recovery purposes. If false, this commitment is placed in the organization&#39;s default region. | [optional] 
**name** | **String** | Output only. The resource name of the capacity commitment, e.g., &#x60;projects/myproject/locations/US/capacityCommitments/123&#x60; The commitment_id must only contain lower case alphanumeric characters or dashes. It must start with a letter and must not end with a dash. Its maximum length is 64 characters. | [optional] [readonly] 
**plan** | **String** | Capacity commitment commitment plan. | [optional] 
**renewalPlan** | **String** | The plan this capacity commitment is converted to after commitment_end_time passes. Once the plan is changed, committed period is extended according to commitment plan. Only applicable for ANNUAL commitments. | [optional] 
**slotCount** | **String** | Number of slots in this commitment. | [optional] 
**state** | **String** | Output only. State of the commitment. | [optional] [readonly] 



## Enum: PlanEnum


* `COMMITMENT_PLAN_UNSPECIFIED` (value: `"COMMITMENT_PLAN_UNSPECIFIED"`)

* `FLEX` (value: `"FLEX"`)

* `TRIAL` (value: `"TRIAL"`)

* `MONTHLY` (value: `"MONTHLY"`)

* `ANNUAL` (value: `"ANNUAL"`)





## Enum: RenewalPlanEnum


* `COMMITMENT_PLAN_UNSPECIFIED` (value: `"COMMITMENT_PLAN_UNSPECIFIED"`)

* `FLEX` (value: `"FLEX"`)

* `TRIAL` (value: `"TRIAL"`)

* `MONTHLY` (value: `"MONTHLY"`)

* `ANNUAL` (value: `"ANNUAL"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `FAILED` (value: `"FAILED"`)




