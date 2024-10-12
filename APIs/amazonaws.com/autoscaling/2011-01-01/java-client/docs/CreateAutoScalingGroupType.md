

# CreateAutoScalingGroupType


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoScalingGroupName** | [**String**](String.md) |  |  |
|**launchConfigurationName** | [**String**](String.md) |  |  [optional] |
|**launchTemplate** | [**CreateAutoScalingGroupTypeLaunchTemplate**](CreateAutoScalingGroupTypeLaunchTemplate.md) |  |  [optional] |
|**mixedInstancesPolicy** | [**CreateAutoScalingGroupTypeMixedInstancesPolicy**](CreateAutoScalingGroupTypeMixedInstancesPolicy.md) |  |  [optional] |
|**instanceId** | [**String**](String.md) |  |  [optional] |
|**minSize** | [**Integer**](Integer.md) |  |  |
|**maxSize** | [**Integer**](Integer.md) |  |  |
|**desiredCapacity** | [**Integer**](Integer.md) |  |  [optional] |
|**defaultCooldown** | [**Integer**](Integer.md) |  |  [optional] |
|**availabilityZones** | [**List**](List.md) |  |  [optional] |
|**loadBalancerNames** | [**List**](List.md) |  |  [optional] |
|**targetGroupARNs** | [**List**](List.md) |  |  [optional] |
|**healthCheckType** | [**String**](String.md) |  |  [optional] |
|**healthCheckGracePeriod** | [**Integer**](Integer.md) |  |  [optional] |
|**placementGroup** | [**String**](String.md) |  |  [optional] |
|**vpCZoneIdentifier** | [**String**](String.md) |  |  [optional] |
|**terminationPolicies** | [**List**](List.md) |  |  [optional] |
|**newInstancesProtectedFromScaleIn** | [**Boolean**](Boolean.md) |  |  [optional] |
|**capacityRebalance** | [**Boolean**](Boolean.md) |  |  [optional] |
|**lifecycleHookSpecificationList** | [**List**](List.md) |  |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |
|**serviceLinkedRoleARN** | [**String**](String.md) |  |  [optional] |
|**maxInstanceLifetime** | [**Integer**](Integer.md) |  |  [optional] |
|**context** | [**String**](String.md) |  |  [optional] |
|**desiredCapacityType** | [**String**](String.md) |  |  [optional] |
|**defaultInstanceWarmup** | [**Integer**](Integer.md) |  |  [optional] |
|**trafficSources** | [**List**](List.md) |  |  [optional] |



