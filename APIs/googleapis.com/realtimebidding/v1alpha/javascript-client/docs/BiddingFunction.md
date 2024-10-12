# RealTimeBiddingApi.BiddingFunction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**biddingFunction** | **String** | The raw Javascript source code of the bidding function. | [optional] 
**name** | **String** | The name of the bidding function that must follow the pattern: &#x60;bidders/{bidder_account_id}/biddingFunctions/{bidding_function_name}&#x60;. | [optional] 
**state** | **String** | Output only. The state of the bidding function. | [optional] [readonly] 
**type** | **String** | The type of the bidding function to be created. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `ARCHIVED` (value: `"ARCHIVED"`)





## Enum: TypeEnum


* `FUNCTION_TYPE_UNSPECIFIED` (value: `"FUNCTION_TYPE_UNSPECIFIED"`)

* `TURTLEDOVE_SIMULATION_BIDDING_FUNCTION` (value: `"TURTLEDOVE_SIMULATION_BIDDING_FUNCTION"`)

* `FLEDGE_BIDDING_FUNCTION` (value: `"FLEDGE_BIDDING_FUNCTION"`)




