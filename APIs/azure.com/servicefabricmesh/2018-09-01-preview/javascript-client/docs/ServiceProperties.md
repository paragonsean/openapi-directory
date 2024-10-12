# SeaBreezeManagementClient.ServiceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoScalingPolicies** | [**[AutoScalingPolicy]**](AutoScalingPolicy.md) | Auto scaling policies | [optional] 
**description** | **String** | User readable description of the service. | [optional] 
**healthState** | [**HealthState**](HealthState.md) |  | [optional] 
**replicaCount** | **Number** | The number of replicas of the service to create. Defaults to 1 if not specified. | [optional] 
**status** | [**ResourceStatus**](ResourceStatus.md) |  | [optional] 
**statusDetails** | **String** | Gives additional information about the current status of the service. | [optional] [readonly] 
**unhealthyEvaluation** | **String** | When the service&#39;s health state is not &#39;Ok&#39;, this additional details from service fabric Health Manager for the user to know why the service is marked unhealthy. | [optional] [readonly] 


