

# PerformanceGoalBidStrategy

A strategy that automatically adjusts the bid to meet or beat a specified performance goal.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customBiddingAlgorithmId** | **String** | The ID of the Custom Bidding Algorithm used by this strategy. Only applicable when performance_goal_type is set to &#x60;BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_CUSTOM_ALGO&#x60;. |  [optional] |
|**maxAverageCpmBidAmountMicros** | **String** | The maximum average CPM that may be bid, in micros of the advertiser&#39;s currency. Must be greater than or equal to a billable unit of the given currency. Not applicable when performance_goal_type is set to &#x60;BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_VIEWABLE_CPM&#x60;. For example, 1500000 represents 1.5 standard units of the currency. |  [optional] |
|**performanceGoalAmountMicros** | **String** | Required. The performance goal the bidding strategy will attempt to meet or beat, in micros of the advertiser&#39;s currency or in micro of the ROAS (Return On Advertising Spend) value which is also based on advertiser&#39;s currency. Must be greater than or equal to a billable unit of the given currency and smaller or equal to upper bounds. Each performance_goal_type has its upper bound: * when performance_goal_type is &#x60;BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_CPA&#x60;, upper bound is 10000.00 USD. * when performance_goal_type is &#x60;BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_CPC&#x60;, upper bound is 1000.00 USD. * when performance_goal_type is &#x60;BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_VIEWABLE_CPM&#x60;, upper bound is 1000.00 USD. * when performance_goal_type is &#x60;BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_CUSTOM_ALGO&#x60;, upper bound is 1000.00 and lower bound is 0.01. Example: If set to &#x60;BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_VIEWABLE_CPM&#x60;, the bid price will be based on the probability that each available impression will be viewable. For example, if viewable CPM target is $2 and an impression is 40% likely to be viewable, the bid price will be $0.80 CPM (40% of $2). For example, 1500000 represents 1.5 standard units of the currency or ROAS value. |  [optional] |
|**performanceGoalType** | [**PerformanceGoalTypeEnum**](#PerformanceGoalTypeEnum) | Required. The type of the performance goal that the bidding strategy will try to meet or beat. For line item level usage, the value must be one of: * &#x60;BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_CPA&#x60; * &#x60;BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_CPC&#x60; * &#x60;BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_VIEWABLE_CPM&#x60; * &#x60;BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_CUSTOM_ALGO&#x60;. |  [optional] |



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



