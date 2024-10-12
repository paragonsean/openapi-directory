

# VmResourceBasedCud

Specifies a resource-based committed use discount (CUD).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**guestAccelerator** | [**GuestAccelerator**](GuestAccelerator.md) |  |  [optional] |
|**machineSeries** | **String** | The machine series for CUD. For example: \&quot;n1\&quot; for general purpose N1 machine type commitments. \&quot;n2\&quot; for general purpose N2 machine type commitments. \&quot;e2\&quot; for general purpose E2 machine type commitments. \&quot;n2d\&quot; for general purpose N2D machine type commitments. \&quot;t2d\&quot; for general purpose T2D machine type commitments. \&quot;c2\&quot;/\&quot;c2d\&quot; for compute-optimized commitments. \&quot;m1\&quot;/\&quot;m2\&quot; for the memory-optimized commitments. \&quot;a2&#39; for the accelerator-optimized commitments. |  [optional] |
|**memorySizeGb** | **Double** | Memory size of the VM in GB (2^30 bytes). Must be an increment of 0.25 (256 MB). |  [optional] |
|**plan** | [**PlanEnum**](#PlanEnum) | Commitment usage plan. |  [optional] |
|**region** | **String** | The region where the VM runs. For example: \&quot;us-central1\&quot; |  [optional] |
|**virtualCpuCount** | **String** | The number of vCPUs. The number of vCPUs must be an integer of 0 or more and can be even or odd. |  [optional] |



## Enum: PlanEnum

| Name | Value |
|---- | -----|
| COMMITMENT_PLAN_UNSPECIFIED | &quot;COMMITMENT_PLAN_UNSPECIFIED&quot; |
| TWELVE_MONTH | &quot;TWELVE_MONTH&quot; |
| THIRTY_SIX_MONTH | &quot;THIRTY_SIX_MONTH&quot; |



