

# UpdateAutoScalingGroupType


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoScalingGroupName** | [**String**](String.md) |  |  |
|**launchConfigurationName** | [**String**](String.md) |  |  [optional] |
|**launchTemplate** | [**UpdateAutoScalingGroupTypeLaunchTemplate**](UpdateAutoScalingGroupTypeLaunchTemplate.md) |  |  [optional] |
|**mixedInstancesPolicy** | [**CreateAutoScalingGroupTypeMixedInstancesPolicy**](CreateAutoScalingGroupTypeMixedInstancesPolicy.md) |  |  [optional] |
|**minSize** | [**Integer**](Integer.md) |  |  [optional] |
|**maxSize** | [**Integer**](Integer.md) |  |  [optional] |
|**desiredCapacity** | [**Integer**](Integer.md) |  |  [optional] |
|**defaultCooldown** | [**Integer**](Integer.md) |  |  [optional] |
|**availabilityZones** | [**List**](List.md) |  |  [optional] |
|**healthCheckType** | [**String**](String.md) |  |  [optional] |
|**healthCheckGracePeriod** | [**Integer**](Integer.md) |  |  [optional] |
|**placementGroup** | [**String**](String.md) |  |  [optional] |
|**vpCZoneIdentifier** | [**String**](String.md) |  |  [optional] |
|**terminationPolicies** | [**List**](List.md) |  |  [optional] |
|**newInstancesProtectedFromScaleIn** | [**Boolean**](Boolean.md) |  |  [optional] |
|**serviceLinkedRoleARN** | [**String**](String.md) |  |  [optional] |
|**maxInstanceLifetime** | [**Integer**](Integer.md) |  |  [optional] |
|**capacityRebalance** | [**Boolean**](Boolean.md) |  |  [optional] |
|**context** | [**String**](String.md) |  |  [optional] |
|**desiredCapacityType** | [**String**](String.md) |  |  [optional] |
|**defaultInstanceWarmup** | [**Integer**](Integer.md) |  |  [optional] |



