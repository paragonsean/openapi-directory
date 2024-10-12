

# ScalingPolicy

Describes a scaling policy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoScalingGroupName** | [**String**](String.md) |  |  [optional] |
|**policyName** | [**String**](String.md) |  |  [optional] |
|**policyARN** | [**String**](String.md) |  |  [optional] |
|**policyType** | [**String**](String.md) |  |  [optional] |
|**adjustmentType** | [**String**](String.md) |  |  [optional] |
|**minAdjustmentStep** | [**Integer**](Integer.md) |  |  [optional] |
|**minAdjustmentMagnitude** | [**Integer**](Integer.md) |  |  [optional] |
|**scalingAdjustment** | [**Integer**](Integer.md) |  |  [optional] |
|**cooldown** | [**Integer**](Integer.md) |  |  [optional] |
|**stepAdjustments** | [**List**](List.md) |  |  [optional] |
|**metricAggregationType** | [**String**](String.md) |  |  [optional] |
|**estimatedInstanceWarmup** | [**Integer**](Integer.md) |  |  [optional] |
|**alarms** | [**List**](List.md) |  |  [optional] |
|**targetTrackingConfiguration** | [**ScalingPolicyTargetTrackingConfiguration**](ScalingPolicyTargetTrackingConfiguration.md) |  |  [optional] |
|**enabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**predictiveScalingConfiguration** | [**ScalingPolicyPredictiveScalingConfiguration**](ScalingPolicyPredictiveScalingConfiguration.md) |  |  [optional] |



