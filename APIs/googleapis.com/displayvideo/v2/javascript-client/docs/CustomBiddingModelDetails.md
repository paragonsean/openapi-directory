# DisplayVideo360Api.CustomBiddingModelDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiserId** | **String** | The unique ID of the relevant advertiser. | [optional] 
**readinessState** | **String** | The readiness state of custom bidding model. | [optional] 
**suspensionState** | **String** | Output only. The suspension state of custom bidding model. | [optional] [readonly] 



## Enum: ReadinessStateEnum


* `UNSPECIFIED` (value: `"READINESS_STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"READINESS_STATE_ACTIVE"`)

* `INSUFFICIENT_DATA` (value: `"READINESS_STATE_INSUFFICIENT_DATA"`)

* `TRAINING` (value: `"READINESS_STATE_TRAINING"`)

* `NO_VALID_SCRIPT` (value: `"READINESS_STATE_NO_VALID_SCRIPT"`)





## Enum: SuspensionStateEnum


* `UNSPECIFIED` (value: `"SUSPENSION_STATE_UNSPECIFIED"`)

* `ENABLED` (value: `"SUSPENSION_STATE_ENABLED"`)

* `DORMANT` (value: `"SUSPENSION_STATE_DORMANT"`)

* `SUSPENDED` (value: `"SUSPENSION_STATE_SUSPENDED"`)




