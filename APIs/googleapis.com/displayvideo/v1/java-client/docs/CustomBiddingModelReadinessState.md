

# CustomBiddingModelReadinessState

The custom bidding algorithm model readiness state for a single shared advertiser.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advertiserId** | **String** | The unique ID of the relevant advertiser. |  [optional] |
|**readinessState** | [**ReadinessStateEnum**](#ReadinessStateEnum) | The readiness state of custom bidding model. |  [optional] |



## Enum: ReadinessStateEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;READINESS_STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;READINESS_STATE_ACTIVE&quot; |
| INSUFFICIENT_DATA | &quot;READINESS_STATE_INSUFFICIENT_DATA&quot; |
| TRAINING | &quot;READINESS_STATE_TRAINING&quot; |
| NO_VALID_SCRIPT | &quot;READINESS_STATE_NO_VALID_SCRIPT&quot; |



