

# CapacityCommitment

Capacity commitment is a way to purchase compute capacity for BigQuery jobs (in the form of slots) with some committed period of usage. Annual commitments renew by default. Commitments can be removed after their commitment end time passes. In order to remove annual commitment, its plan needs to be changed to monthly or flex first. A capacity commitment resource exists as a child resource of the admin project.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commitmentEndTime** | **String** | Output only. The end of the current commitment period. It is applicable only for ACTIVE capacity commitments. |  [optional] [readonly] |
|**commitmentStartTime** | **String** | Output only. The start of the current commitment period. It is applicable only for ACTIVE capacity commitments. |  [optional] [readonly] |
|**failureStatus** | [**Status**](Status.md) |  |  [optional] |
|**multiRegionAuxiliary** | **Boolean** | Applicable only for commitments located within one of the BigQuery multi-regions (US or EU). If set to true, this commitment is placed in the organization&#39;s secondary region which is designated for disaster recovery purposes. If false, this commitment is placed in the organization&#39;s default region. |  [optional] |
|**name** | **String** | Output only. The resource name of the capacity commitment, e.g., &#x60;projects/myproject/locations/US/capacityCommitments/123&#x60; The commitment_id must only contain lower case alphanumeric characters or dashes. It must start with a letter and must not end with a dash. Its maximum length is 64 characters. |  [optional] [readonly] |
|**plan** | [**PlanEnum**](#PlanEnum) | Capacity commitment commitment plan. |  [optional] |
|**renewalPlan** | [**RenewalPlanEnum**](#RenewalPlanEnum) | The plan this capacity commitment is converted to after commitment_end_time passes. Once the plan is changed, committed period is extended according to commitment plan. Only applicable for ANNUAL commitments. |  [optional] |
|**slotCount** | **String** | Number of slots in this commitment. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the commitment. |  [optional] [readonly] |



## Enum: PlanEnum

| Name | Value |
|---- | -----|
| COMMITMENT_PLAN_UNSPECIFIED | &quot;COMMITMENT_PLAN_UNSPECIFIED&quot; |
| FLEX | &quot;FLEX&quot; |
| TRIAL | &quot;TRIAL&quot; |
| MONTHLY | &quot;MONTHLY&quot; |
| ANNUAL | &quot;ANNUAL&quot; |



## Enum: RenewalPlanEnum

| Name | Value |
|---- | -----|
| COMMITMENT_PLAN_UNSPECIFIED | &quot;COMMITMENT_PLAN_UNSPECIFIED&quot; |
| FLEX | &quot;FLEX&quot; |
| TRIAL | &quot;TRIAL&quot; |
| MONTHLY | &quot;MONTHLY&quot; |
| ANNUAL | &quot;ANNUAL&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| FAILED | &quot;FAILED&quot; |



