# DisplayVideo360Api.CustomBiddingAlgorithmRules

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **Boolean** | Output only. Whether the rules resource is currently being used for scoring by the parent algorithm. | [optional] [readonly] 
**createTime** | **String** | Output only. The time when the rules resource was created. | [optional] [readonly] 
**customBiddingAlgorithmId** | **String** | Output only. The unique ID of the custom bidding algorithm that the rules resource belongs to. | [optional] [readonly] 
**customBiddingAlgorithmRulesId** | **String** | Output only. The unique ID of the rules resource. | [optional] [readonly] 
**error** | [**CustomBiddingAlgorithmRulesError**](CustomBiddingAlgorithmRulesError.md) |  | [optional] 
**name** | **String** | Output only. The resource name of the rules resource. | [optional] [readonly] 
**rules** | [**CustomBiddingAlgorithmRulesRef**](CustomBiddingAlgorithmRulesRef.md) |  | [optional] 
**state** | **String** | Output only. The state of the rules resource. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACCEPTED` (value: `"ACCEPTED"`)

* `REJECTED` (value: `"REJECTED"`)




