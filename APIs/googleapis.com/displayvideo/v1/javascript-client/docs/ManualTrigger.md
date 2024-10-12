# DisplayVideo360Api.ManualTrigger

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activationDurationMinutes** | **String** | Required. The maximum duration of each activation in minutes. Must be between 1 and 360 inclusive. After this duration, the trigger will be automatically deactivated. | [optional] 
**advertiserId** | **String** | Required. Immutable. The unique ID of the advertiser that the manual trigger belongs to. | [optional] 
**displayName** | **String** | Required. The display name of the manual trigger. Must be UTF-8 encoded with a maximum size of 240 bytes. | [optional] 
**latestActivationTime** | **String** | Output only. The timestamp of the trigger&#39;s latest activation. | [optional] [readonly] 
**name** | **String** | Output only. The resource name of the manual trigger. | [optional] [readonly] 
**state** | **String** | Output only. The state of the manual trigger. Will be set to the &#x60;INACTIVE&#x60; state upon creation. | [optional] [readonly] 
**triggerId** | **String** | Output only. The unique ID of the manual trigger. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `INACTIVE` (value: `"INACTIVE"`)

* `ACTIVE` (value: `"ACTIVE"`)




