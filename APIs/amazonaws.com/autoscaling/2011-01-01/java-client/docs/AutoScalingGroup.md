

# AutoScalingGroup

Describes an Auto Scaling group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoScalingGroupName** | [**String**](String.md) |  |  |
|**autoScalingGroupARN** | [**String**](String.md) |  |  [optional] |
|**launchConfigurationName** | [**String**](String.md) |  |  [optional] |
|**launchTemplate** | [**AutoScalingGroupLaunchTemplate**](AutoScalingGroupLaunchTemplate.md) |  |  [optional] |
|**mixedInstancesPolicy** | [**AutoScalingGroupMixedInstancesPolicy**](AutoScalingGroupMixedInstancesPolicy.md) |  |  [optional] |
|**minSize** | [**Integer**](Integer.md) |  |  |
|**maxSize** | [**Integer**](Integer.md) |  |  |
|**desiredCapacity** | [**Integer**](Integer.md) |  |  |
|**predictedCapacity** | [**Integer**](Integer.md) |  |  [optional] |
|**defaultCooldown** | [**Integer**](Integer.md) |  |  |
|**availabilityZones** | [**List**](List.md) |  |  |
|**loadBalancerNames** | [**List**](List.md) |  |  [optional] |
|**targetGroupARNs** | [**List**](List.md) |  |  [optional] |
|**healthCheckType** | [**String**](String.md) |  |  |
|**healthCheckGracePeriod** | [**Integer**](Integer.md) |  |  [optional] |
|**instances** | [**List**](List.md) |  |  [optional] |
|**createdTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**suspendedProcesses** | [**List**](List.md) |  |  [optional] |
|**placementGroup** | [**String**](String.md) |  |  [optional] |
|**vpCZoneIdentifier** | [**String**](String.md) |  |  [optional] |
|**enabledMetrics** | [**List**](List.md) |  |  [optional] |
|**status** | [**String**](String.md) |  |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |
|**terminationPolicies** | [**List**](List.md) |  |  [optional] |
|**newInstancesProtectedFromScaleIn** | [**Boolean**](Boolean.md) |  |  [optional] |
|**serviceLinkedRoleARN** | [**String**](String.md) |  |  [optional] |
|**maxInstanceLifetime** | [**Integer**](Integer.md) |  |  [optional] |
|**capacityRebalance** | [**Boolean**](Boolean.md) |  |  [optional] |
|**warmPoolConfiguration** | [**AutoScalingGroupWarmPoolConfiguration**](AutoScalingGroupWarmPoolConfiguration.md) |  |  [optional] |
|**warmPoolSize** | [**Integer**](Integer.md) |  |  [optional] |
|**context** | [**String**](String.md) |  |  [optional] |
|**desiredCapacityType** | [**String**](String.md) |  |  [optional] |
|**defaultInstanceWarmup** | [**Integer**](Integer.md) |  |  [optional] |
|**trafficSources** | [**List**](List.md) |  |  [optional] |



