# AutoScaling.UpdateAutoScalingGroupType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoScalingGroupName** | **String** |  | 
**launchConfigurationName** | **String** |  | [optional] 
**launchTemplate** | [**UpdateAutoScalingGroupTypeLaunchTemplate**](UpdateAutoScalingGroupTypeLaunchTemplate.md) |  | [optional] 
**mixedInstancesPolicy** | [**CreateAutoScalingGroupTypeMixedInstancesPolicy**](CreateAutoScalingGroupTypeMixedInstancesPolicy.md) |  | [optional] 
**minSize** | **Number** |  | [optional] 
**maxSize** | **Number** |  | [optional] 
**desiredCapacity** | **Number** |  | [optional] 
**defaultCooldown** | **Number** |  | [optional] 
**availabilityZones** | **Array** |  | [optional] 
**healthCheckType** | **String** |  | [optional] 
**healthCheckGracePeriod** | **Number** |  | [optional] 
**placementGroup** | **String** |  | [optional] 
**vPCZoneIdentifier** | **String** |  | [optional] 
**terminationPolicies** | **Array** |  | [optional] 
**newInstancesProtectedFromScaleIn** | **Boolean** |  | [optional] 
**serviceLinkedRoleARN** | **String** |  | [optional] 
**maxInstanceLifetime** | **Number** |  | [optional] 
**capacityRebalance** | **Boolean** |  | [optional] 
**context** | **String** |  | [optional] 
**desiredCapacityType** | **String** |  | [optional] 
**defaultInstanceWarmup** | **Number** |  | [optional] 


