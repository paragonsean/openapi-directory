

# PatchRollout

Patch rollout configuration specifications. Contains details on the concurrency control when applying patch(es) to all targeted VMs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disruptionBudget** | [**FixedOrPercent**](FixedOrPercent.md) |  |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) | Mode of the patch rollout. |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| MODE_UNSPECIFIED | &quot;MODE_UNSPECIFIED&quot; |
| ZONE_BY_ZONE | &quot;ZONE_BY_ZONE&quot; |
| CONCURRENT_ZONES | &quot;CONCURRENT_ZONES&quot; |



