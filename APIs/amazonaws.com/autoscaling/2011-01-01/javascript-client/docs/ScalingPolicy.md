# AutoScaling.ScalingPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoScalingGroupName** | **String** |  | [optional] 
**policyName** | **String** |  | [optional] 
**policyARN** | **String** |  | [optional] 
**policyType** | **String** |  | [optional] 
**adjustmentType** | **String** |  | [optional] 
**minAdjustmentStep** | **Number** |  | [optional] 
**minAdjustmentMagnitude** | **Number** |  | [optional] 
**scalingAdjustment** | **Number** |  | [optional] 
**cooldown** | **Number** |  | [optional] 
**stepAdjustments** | **Array** |  | [optional] 
**metricAggregationType** | **String** |  | [optional] 
**estimatedInstanceWarmup** | **Number** |  | [optional] 
**alarms** | **Array** |  | [optional] 
**targetTrackingConfiguration** | [**ScalingPolicyTargetTrackingConfiguration**](ScalingPolicyTargetTrackingConfiguration.md) |  | [optional] 
**enabled** | **Boolean** |  | [optional] 
**predictiveScalingConfiguration** | [**ScalingPolicyPredictiveScalingConfiguration**](ScalingPolicyPredictiveScalingConfiguration.md) |  | [optional] 


