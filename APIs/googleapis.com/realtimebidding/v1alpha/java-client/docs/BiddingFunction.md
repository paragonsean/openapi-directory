

# BiddingFunction

The bidding function to be executed as part of the TURTLEDOVE simulation experiment bidding flow.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**biddingFunction** | **String** | The raw Javascript source code of the bidding function. |  [optional] |
|**name** | **String** | The name of the bidding function that must follow the pattern: &#x60;bidders/{bidder_account_id}/biddingFunctions/{bidding_function_name}&#x60;. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of the bidding function. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the bidding function to be created. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| ARCHIVED | &quot;ARCHIVED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| FUNCTION_TYPE_UNSPECIFIED | &quot;FUNCTION_TYPE_UNSPECIFIED&quot; |
| TURTLEDOVE_SIMULATION_BIDDING_FUNCTION | &quot;TURTLEDOVE_SIMULATION_BIDDING_FUNCTION&quot; |
| FLEDGE_BIDDING_FUNCTION | &quot;FLEDGE_BIDDING_FUNCTION&quot; |



