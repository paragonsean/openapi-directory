

# RuleCondition

The condition that results in the alert rule being activated.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSource** | [**RuleDataSource**](RuleDataSource.md) |  |  [optional] |
|**odataType** | **String** | specifies the type of condition. This can be one of three types: ManagementEventRuleCondition (occurrences of management events), LocationThresholdRuleCondition (based on the number of failures of a web test), and ThresholdRuleCondition (based on the threshold of a metric). |  |



