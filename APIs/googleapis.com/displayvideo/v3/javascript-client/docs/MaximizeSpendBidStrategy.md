# DisplayVideo360Api.MaximizeSpendBidStrategy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customBiddingAlgorithmId** | **String** | The ID of the Custom Bidding Algorithm used by this strategy. Only applicable when performance_goal_type is set to &#x60;BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_CUSTOM_ALGO&#x60;. | [optional] 
**maxAverageCpmBidAmountMicros** | **String** | The maximum average CPM that may be bid, in micros of the advertiser&#39;s currency. Must be greater than or equal to a billable unit of the given currency. For example, 1500000 represents 1.5 standard units of the currency. | [optional] 
**performanceGoalType** | **String** | Required. The type of the performance goal that the bidding strategy tries to minimize while spending the full budget. &#x60;BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_VIEWABLE_CPM&#x60; is not supported for this strategy. | [optional] 
**raiseBidForDeals** | **Boolean** | Whether the strategy takes deal floor prices into account. | [optional] 



## Enum: PerformanceGoalTypeEnum


* `UNSPECIFIED` (value: `"BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_UNSPECIFIED"`)

* `CPA` (value: `"BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_CPA"`)

* `CPC` (value: `"BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_CPC"`)

* `VIEWABLE_CPM` (value: `"BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_VIEWABLE_CPM"`)

* `CUSTOM_ALGO` (value: `"BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_CUSTOM_ALGO"`)

* `CIVA` (value: `"BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_CIVA"`)

* `IVO_TEN` (value: `"BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_IVO_TEN"`)

* `AV_VIEWED` (value: `"BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_AV_VIEWED"`)




