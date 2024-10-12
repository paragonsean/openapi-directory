

# MaximizeSpendBidStrategy

A strategy that automatically adjusts the bid to optimize a specified performance goal while spending the full budget.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customBiddingAlgorithmId** | **String** | The ID of the Custom Bidding Algorithm used by this strategy. Only applicable when performance_goal_type is set to &#x60;BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_CUSTOM_ALGO&#x60;. |  [optional] |
|**maxAverageCpmBidAmountMicros** | **String** | The maximum average CPM that may be bid, in micros of the advertiser&#39;s currency. Must be greater than or equal to a billable unit of the given currency. For example, 1500000 represents 1.5 standard units of the currency. |  [optional] |
|**performanceGoalType** | [**PerformanceGoalTypeEnum**](#PerformanceGoalTypeEnum) | Required. The type of the performance goal that the bidding strategy tries to minimize while spending the full budget. &#x60;BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_VIEWABLE_CPM&#x60; is not supported for this strategy. |  [optional] |
|**raiseBidForDeals** | **Boolean** | Whether the strategy takes deal floor prices into account. |  [optional] |



## Enum: PerformanceGoalTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_UNSPECIFIED&quot; |
| CPA | &quot;BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_CPA&quot; |
| CPC | &quot;BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_CPC&quot; |
| VIEWABLE_CPM | &quot;BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_VIEWABLE_CPM&quot; |
| CUSTOM_ALGO | &quot;BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_CUSTOM_ALGO&quot; |
| CIVA | &quot;BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_CIVA&quot; |
| IVO_TEN | &quot;BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_IVO_TEN&quot; |
| AV_VIEWED | &quot;BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_AV_VIEWED&quot; |



