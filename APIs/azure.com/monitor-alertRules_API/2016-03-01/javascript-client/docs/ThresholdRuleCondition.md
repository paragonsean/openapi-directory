# MonitorManagementClient.ThresholdRuleCondition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | [**ConditionOperator**](ConditionOperator.md) |  | 
**threshold** | **Number** | the threshold value that activates the alert. | 
**timeAggregation** | [**TimeAggregationOperator**](TimeAggregationOperator.md) |  | [optional] 
**windowSize** | **String** | the period of time (in ISO 8601 duration format) that is used to monitor alert activity based on the threshold. If specified then it must be between 5 minutes and 1 day. | [optional] 


