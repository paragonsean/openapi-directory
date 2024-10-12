# AutoScaling.CreateAutoScalingGroupType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoScalingGroupName** | **String** |  | 
**launchConfigurationName** | **String** |  | [optional] 
**launchTemplate** | [**CreateAutoScalingGroupTypeLaunchTemplate**](CreateAutoScalingGroupTypeLaunchTemplate.md) |  | [optional] 
**mixedInstancesPolicy** | [**CreateAutoScalingGroupTypeMixedInstancesPolicy**](CreateAutoScalingGroupTypeMixedInstancesPolicy.md) |  | [optional] 
**instanceId** | **String** |  | [optional] 
**minSize** | **Number** |  | 
**maxSize** | **Number** |  | 
**desiredCapacity** | **Number** |  | [optional] 
**defaultCooldown** | **Number** |  | [optional] 
**availabilityZones** | **Array** |  | [optional] 
**loadBalancerNames** | **Array** |  | [optional] 
**targetGroupARNs** | **Array** |  | [optional] 
**healthCheckType** | **String** |  | [optional] 
**healthCheckGracePeriod** | **Number** |  | [optional] 
**placementGroup** | **String** |  | [optional] 
**vPCZoneIdentifier** | **String** |  | [optional] 
**terminationPolicies** | **Array** |  | [optional] 
**newInstancesProtectedFromScaleIn** | **Boolean** |  | [optional] 
**capacityRebalance** | **Boolean** |  | [optional] 
**lifecycleHookSpecificationList** | **Array** |  | [optional] 
**tags** | **Array** |  | [optional] 
**serviceLinkedRoleARN** | **String** |  | [optional] 
**maxInstanceLifetime** | **Number** |  | [optional] 
**context** | **String** |  | [optional] 
**desiredCapacityType** | **String** |  | [optional] 
**defaultInstanceWarmup** | **Number** |  | [optional] 
**trafficSources** | **Array** |  | [optional] 


