# AutoScaling.AutoScalingGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoScalingGroupName** | **String** |  | 
**autoScalingGroupARN** | **String** |  | [optional] 
**launchConfigurationName** | **String** |  | [optional] 
**launchTemplate** | [**AutoScalingGroupLaunchTemplate**](AutoScalingGroupLaunchTemplate.md) |  | [optional] 
**mixedInstancesPolicy** | [**AutoScalingGroupMixedInstancesPolicy**](AutoScalingGroupMixedInstancesPolicy.md) |  | [optional] 
**minSize** | **Number** |  | 
**maxSize** | **Number** |  | 
**desiredCapacity** | **Number** |  | 
**predictedCapacity** | **Number** |  | [optional] 
**defaultCooldown** | **Number** |  | 
**availabilityZones** | **Array** |  | 
**loadBalancerNames** | **Array** |  | [optional] 
**targetGroupARNs** | **Array** |  | [optional] 
**healthCheckType** | **String** |  | 
**healthCheckGracePeriod** | **Number** |  | [optional] 
**instances** | **Array** |  | [optional] 
**createdTime** | **Date** |  | 
**suspendedProcesses** | **Array** |  | [optional] 
**placementGroup** | **String** |  | [optional] 
**vPCZoneIdentifier** | **String** |  | [optional] 
**enabledMetrics** | **Array** |  | [optional] 
**status** | **String** |  | [optional] 
**tags** | **Array** |  | [optional] 
**terminationPolicies** | **Array** |  | [optional] 
**newInstancesProtectedFromScaleIn** | **Boolean** |  | [optional] 
**serviceLinkedRoleARN** | **String** |  | [optional] 
**maxInstanceLifetime** | **Number** |  | [optional] 
**capacityRebalance** | **Boolean** |  | [optional] 
**warmPoolConfiguration** | [**AutoScalingGroupWarmPoolConfiguration**](AutoScalingGroupWarmPoolConfiguration.md) |  | [optional] 
**warmPoolSize** | **Number** |  | [optional] 
**context** | **String** |  | [optional] 
**desiredCapacityType** | **String** |  | [optional] 
**defaultInstanceWarmup** | **Number** |  | [optional] 
**trafficSources** | **Array** |  | [optional] 


