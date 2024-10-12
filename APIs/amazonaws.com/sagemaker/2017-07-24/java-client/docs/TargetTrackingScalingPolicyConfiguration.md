

# TargetTrackingScalingPolicyConfiguration

<p>A target tracking scaling policy. Includes support for predefined or customized metrics.</p> <p>When using the <a href=\"https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PutScalingPolicy.html\">PutScalingPolicy</a> API, this parameter is required when you are creating a policy with the policy type <code>TargetTrackingScaling</code>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metricSpecification** | [**TargetTrackingScalingPolicyConfigurationMetricSpecification**](TargetTrackingScalingPolicyConfigurationMetricSpecification.md) |  |  [optional] |
|**targetValue** | [**Double**](Double.md) |  |  [optional] |



