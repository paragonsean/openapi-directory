

# SpokeStateReasonCount

The number of spokes in the hub that are inactive for this reason.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **String** | Output only. The total number of spokes that are inactive for a particular reason and associated with a given hub. |  [optional] [readonly] |
|**stateReasonCode** | [**StateReasonCodeEnum**](#StateReasonCodeEnum) | Output only. The reason that a spoke is inactive. |  [optional] [readonly] |



## Enum: StateReasonCodeEnum

| Name | Value |
|---- | -----|
| CODE_UNSPECIFIED | &quot;CODE_UNSPECIFIED&quot; |
| PENDING_REVIEW | &quot;PENDING_REVIEW&quot; |
| REJECTED | &quot;REJECTED&quot; |
| PAUSED | &quot;PAUSED&quot; |
| FAILED | &quot;FAILED&quot; |



