

# ScalingPolicy

<p>Represents a scaling policy to use with Application Auto Scaling.</p> <p>For more information about configuring scaling policies for a specific service, see <a href=\"https://docs.aws.amazon.com/autoscaling/application/userguide/integrated-services-list.html\">Amazon Web Services services that you can use with Application Auto Scaling</a> in the <i>Application Auto Scaling User Guide</i>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**policyARN** | [**String**](String.md) |  |  |
|**policyName** | [**String**](String.md) |  |  |
|**serviceNamespace** | [**ServiceNamespace**](ServiceNamespace.md) |  |  |
|**resourceId** | [**String**](String.md) |  |  |
|**scalableDimension** | [**ScalableDimension**](ScalableDimension.md) |  |  |
|**policyType** | [**PolicyType**](PolicyType.md) |  |  |
|**stepScalingPolicyConfiguration** | [**ScalingPolicyStepScalingPolicyConfiguration**](ScalingPolicyStepScalingPolicyConfiguration.md) |  |  [optional] |
|**targetTrackingScalingPolicyConfiguration** | [**ScalingPolicyTargetTrackingScalingPolicyConfiguration**](ScalingPolicyTargetTrackingScalingPolicyConfiguration.md) |  |  [optional] |
|**alarms** | [**List**](List.md) |  |  [optional] |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |



