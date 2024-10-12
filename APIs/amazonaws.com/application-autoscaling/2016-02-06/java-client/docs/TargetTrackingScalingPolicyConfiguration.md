

# TargetTrackingScalingPolicyConfiguration

<p>Represents a target tracking scaling policy configuration to use with Application Auto Scaling.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html\">Target tracking scaling policies</a> in the <i>Application Auto Scaling User Guide</i>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**targetValue** | [**Double**](Double.md) |  |  |
|**predefinedMetricSpecification** | [**TargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification**](TargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification.md) |  |  [optional] |
|**customizedMetricSpecification** | [**TargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification**](TargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification.md) |  |  [optional] |
|**scaleOutCooldown** | [**Integer**](Integer.md) |  |  [optional] |
|**scaleInCooldown** | [**Integer**](Integer.md) |  |  [optional] |
|**disableScaleIn** | [**Boolean**](Boolean.md) |  |  [optional] |



