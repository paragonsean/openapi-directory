

# CustomBiddingModelDetails

The details of a custom bidding algorithm model for a single shared advertiser.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advertiserId** | **String** | The unique ID of the relevant advertiser. |  [optional] |
|**readinessState** | [**ReadinessStateEnum**](#ReadinessStateEnum) | The readiness state of custom bidding model. |  [optional] |
|**suspensionState** | [**SuspensionStateEnum**](#SuspensionStateEnum) | Output only. The suspension state of custom bidding model. |  [optional] [readonly] |



## Enum: ReadinessStateEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;READINESS_STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;READINESS_STATE_ACTIVE&quot; |
| INSUFFICIENT_DATA | &quot;READINESS_STATE_INSUFFICIENT_DATA&quot; |
| TRAINING | &quot;READINESS_STATE_TRAINING&quot; |
| NO_VALID_SCRIPT | &quot;READINESS_STATE_NO_VALID_SCRIPT&quot; |



## Enum: SuspensionStateEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SUSPENSION_STATE_UNSPECIFIED&quot; |
| ENABLED | &quot;SUSPENSION_STATE_ENABLED&quot; |
| DORMANT | &quot;SUSPENSION_STATE_DORMANT&quot; |
| SUSPENDED | &quot;SUSPENSION_STATE_SUSPENDED&quot; |



