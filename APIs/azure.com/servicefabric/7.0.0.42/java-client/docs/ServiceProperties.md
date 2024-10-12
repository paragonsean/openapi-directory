

# ServiceProperties

Describes properties of a service resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoScalingPolicies** | [**List&lt;AutoScalingPolicy&gt;**](AutoScalingPolicy.md) | Auto scaling policies |  [optional] |
|**description** | **String** | User readable description of the service. |  [optional] |
|**dnsName** | **String** | Dns name of the service. |  [optional] |
|**executionPolicy** | [**ExecutionPolicy**](ExecutionPolicy.md) |  |  [optional] |
|**healthState** | **HealthState** |  |  [optional] |
|**identityRefs** | [**List&lt;ServiceIdentity&gt;**](ServiceIdentity.md) | The service identity list. |  [optional] |
|**replicaCount** | **Integer** | The number of replicas of the service to create. Defaults to 1 if not specified. |  [optional] |
|**status** | **ResourceStatus** |  |  [optional] |
|**statusDetails** | **String** | Gives additional information about the current status of the service. |  [optional] [readonly] |
|**unhealthyEvaluation** | **String** | When the service&#39;s health state is not &#39;Ok&#39;, this additional details from service fabric Health Manager for the user to know why the service is marked unhealthy. |  [optional] [readonly] |



