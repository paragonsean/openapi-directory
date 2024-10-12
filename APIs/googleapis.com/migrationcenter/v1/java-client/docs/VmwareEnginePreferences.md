

# VmwareEnginePreferences

The user preferences relating to Google Cloud VMware Engine target platform.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commitmentPlan** | [**CommitmentPlanEnum**](#CommitmentPlanEnum) | Commitment plan to consider when calculating costs for virtual machine insights and recommendations. If you are unsure which value to set, a 3 year commitment plan is often a good value to start with. |  [optional] |
|**cpuOvercommitRatio** | **Double** | CPU overcommit ratio. Acceptable values are between 1.0 and 8.0, with 0.1 increment. |  [optional] |
|**memoryOvercommitRatio** | **Double** | Memory overcommit ratio. Acceptable values are 1.0, 1.25, 1.5, 1.75 and 2.0. |  [optional] |
|**storageDeduplicationCompressionRatio** | **Double** | The Deduplication and Compression ratio is based on the logical (Used Before) space required to store data before applying deduplication and compression, in relation to the physical (Used After) space required after applying deduplication and compression. Specifically, the ratio is the Used Before space divided by the Used After space. For example, if the Used Before space is 3 GB, but the physical Used After space is 1 GB, the deduplication and compression ratio is 3x. Acceptable values are between 1.0 and 4.0. |  [optional] |



## Enum: CommitmentPlanEnum

| Name | Value |
|---- | -----|
| COMMITMENT_PLAN_UNSPECIFIED | &quot;COMMITMENT_PLAN_UNSPECIFIED&quot; |
| ON_DEMAND | &quot;ON_DEMAND&quot; |
| COMMITMENT_1_YEAR_MONTHLY_PAYMENTS | &quot;COMMITMENT_1_YEAR_MONTHLY_PAYMENTS&quot; |
| COMMITMENT_3_YEAR_MONTHLY_PAYMENTS | &quot;COMMITMENT_3_YEAR_MONTHLY_PAYMENTS&quot; |
| COMMITMENT_1_YEAR_UPFRONT_PAYMENT | &quot;COMMITMENT_1_YEAR_UPFRONT_PAYMENT&quot; |
| COMMITMENT_3_YEAR_UPFRONT_PAYMENT | &quot;COMMITMENT_3_YEAR_UPFRONT_PAYMENT&quot; |



