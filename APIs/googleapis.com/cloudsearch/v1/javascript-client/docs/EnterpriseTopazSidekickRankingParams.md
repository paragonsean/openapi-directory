# CloudSearchApi.EnterpriseTopazSidekickRankingParams

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTimeMs** | **String** | The end-time that this object will expect to occur. If the type is marked as FIXED, then this end-time will persist after bidding. If the type is marked as FLEXIBLE, this field is NOT expected to be filled and will be filled in after it has won a bid. Expected to be set when type is set to FIXED. | [optional] 
**priority** | **String** | The priority to determine between objects that have the same start_time_ms The lower-value of priority &#x3D;&#x3D; ranked higher. Max-priority &#x3D; 0. Expected to be set for all types. | [optional] 
**score** | **Number** | The score of the card to be used to break priority-ties | [optional] 
**spanMs** | **String** | The span that this card will take in the stream Expected to be set when type is set to FLEXIBLE. | [optional] 
**startTimeMs** | **String** | The start-time that this object will bid-for If the type is marked as FIXED, then this start-time will persist after bidding. If the type is marked as FLEXIBLE, then it will occur at the given time or sometime after the requested time. Expected to be set for all types. | [optional] 
**type** | **String** | The packing type of this object. | [optional] 



## Enum: PriorityEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `CRITICAL` (value: `"CRITICAL"`)

* `IMPORTANT` (value: `"IMPORTANT"`)

* `HIGH` (value: `"HIGH"`)

* `NORMAL` (value: `"NORMAL"`)

* `BEST_EFFORT` (value: `"BEST_EFFORT"`)





## Enum: TypeEnum


* `FIXED` (value: `"FIXED"`)

* `FLEXIBLE` (value: `"FLEXIBLE"`)




