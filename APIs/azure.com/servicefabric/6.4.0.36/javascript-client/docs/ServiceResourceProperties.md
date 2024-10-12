# ServiceFabricClientApis.ServiceResourceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codePackages** | [**[ContainerCodePackageProperties]**](ContainerCodePackageProperties.md) | Describes the set of code packages that forms the service. A code package describes the container and the properties for running it. All the code packages are started together on the same host and share the same context (network, process etc.). | 
**diagnostics** | [**DiagnosticsRef**](DiagnosticsRef.md) |  | [optional] 
**networkRefs** | [**[NetworkRef]**](NetworkRef.md) | The names of the private networks that this service needs to be part of. | [optional] 
**osType** | [**OperatingSystemType**](OperatingSystemType.md) |  | 
**autoScalingPolicies** | [**[AutoScalingPolicy]**](AutoScalingPolicy.md) | Auto scaling policies | [optional] 
**description** | **String** | User readable description of the service. | [optional] 
**healthState** | [**HealthState**](HealthState.md) |  | [optional] 
**replicaCount** | **Number** | The number of replicas of the service to create. Defaults to 1 if not specified. | [optional] 
**status** | [**ResourceStatus**](ResourceStatus.md) |  | [optional] 
**statusDetails** | **String** | Gives additional information about the current status of the service. | [optional] [readonly] 
**unhealthyEvaluation** | **String** | When the service&#39;s health state is not &#39;Ok&#39;, this additional details from service fabric Health Manager for the user to know why the service is marked unhealthy. | [optional] [readonly] 


