

# ScalingPolicy

Rule that controls how a fleet is scaled. Scaling policies are uniquely identified by the combination of name and fleet ID.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fleetId** | [**String**](String.md) |  |  [optional] |
|**fleetArn** | [**String**](String.md) |  |  [optional] |
|**name** | [**String**](String.md) |  |  [optional] |
|**status** | [**ScalingStatusType**](ScalingStatusType.md) |  |  [optional] |
|**scalingAdjustment** | [**Integer**](Integer.md) |  |  [optional] |
|**scalingAdjustmentType** | [**ScalingAdjustmentType**](ScalingAdjustmentType.md) |  |  [optional] |
|**comparisonOperator** | [**ComparisonOperatorType**](ComparisonOperatorType.md) |  |  [optional] |
|**threshold** | [**Double**](Double.md) |  |  [optional] |
|**evaluationPeriods** | [**Integer**](Integer.md) |  |  [optional] |
|**metricName** | [**MetricName**](MetricName.md) |  |  [optional] |
|**policyType** | [**PolicyType**](PolicyType.md) |  |  [optional] |
|**targetConfiguration** | [**PutScalingPolicyInputTargetConfiguration**](PutScalingPolicyInputTargetConfiguration.md) |  |  [optional] |
|**updateStatus** | [**LocationUpdateStatus**](LocationUpdateStatus.md) |  |  [optional] |
|**location** | [**String**](String.md) |  |  [optional] |



