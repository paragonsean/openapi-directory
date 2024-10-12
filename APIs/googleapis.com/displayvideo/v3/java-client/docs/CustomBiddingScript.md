

# CustomBiddingScript

A single custom bidding script.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** | Output only. Whether the script is currently being used for scoring by the parent algorithm. |  [optional] [readonly] |
|**createTime** | **String** | Output only. The time when the script was created. |  [optional] [readonly] |
|**customBiddingAlgorithmId** | **String** | Output only. The unique ID of the custom bidding algorithm the script belongs to. |  [optional] [readonly] |
|**customBiddingScriptId** | **String** | Output only. The unique ID of the custom bidding script. |  [optional] [readonly] |
|**errors** | [**List&lt;ScriptError&gt;**](ScriptError.md) | Output only. Error details of a rejected custom bidding script. This field will only be populated when state is REJECTED. |  [optional] [readonly] |
|**name** | **String** | Output only. The resource name of the custom bidding script. |  [optional] [readonly] |
|**script** | [**CustomBiddingScriptRef**](CustomBiddingScriptRef.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of the custom bidding script. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACCEPTED | &quot;ACCEPTED&quot; |
| REJECTED | &quot;REJECTED&quot; |
| PENDING | &quot;PENDING&quot; |



