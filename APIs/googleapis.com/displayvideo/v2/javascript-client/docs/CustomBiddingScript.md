# DisplayVideo360Api.CustomBiddingScript

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **Boolean** | Output only. Whether the script is currently being used for scoring by the parent algorithm. | [optional] [readonly] 
**createTime** | **String** | Output only. The time when the script was created. | [optional] [readonly] 
**customBiddingAlgorithmId** | **String** | Output only. The unique ID of the custom bidding algorithm the script belongs to. | [optional] [readonly] 
**customBiddingScriptId** | **String** | Output only. The unique ID of the custom bidding script. | [optional] [readonly] 
**errors** | [**[ScriptError]**](ScriptError.md) | Output only. Error details of a rejected custom bidding script. This field will only be populated when state is REJECTED. | [optional] [readonly] 
**name** | **String** | Output only. The resource name of the custom bidding script. | [optional] [readonly] 
**script** | [**CustomBiddingScriptRef**](CustomBiddingScriptRef.md) |  | [optional] 
**state** | **String** | Output only. The state of the custom bidding script. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACCEPTED` (value: `"ACCEPTED"`)

* `REJECTED` (value: `"REJECTED"`)

* `PENDING` (value: `"PENDING"`)




