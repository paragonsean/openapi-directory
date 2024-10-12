

# ManagementEventAggregationCondition

How the data that is collected should be combined over time.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**operator** | **ConditionOperator** |  |  [optional] |
|**threshold** | **Double** | The threshold value that activates the alert. |  [optional] |
|**windowSize** | **String** | the period of time (in ISO 8601 duration format) that is used to monitor alert activity based on the threshold. If specified then it must be between 5 minutes and 1 day. |  [optional] |



