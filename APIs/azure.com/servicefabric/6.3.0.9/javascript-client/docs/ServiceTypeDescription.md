# ServiceFabricClientApis.ServiceTypeDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extensions** | [**[ServiceTypeExtensionDescription]**](ServiceTypeExtensionDescription.md) | List of service type extensions. | [optional] 
**isStateful** | **Boolean** | Indicates whether the service type is a stateful service type or a stateless service type. This property is true if the service type is a stateful service type, false otherwise. | [optional] 
**kind** | [**ServiceKind**](ServiceKind.md) |  | 
**loadMetrics** | [**[ServiceLoadMetricDescription]**](ServiceLoadMetricDescription.md) | The service load metrics is given as an array of ServiceLoadMetricDescription objects. | [optional] 
**placementConstraints** | **String** | The placement constraint to be used when instantiating this service in a Service Fabric cluster. | [optional] 
**servicePlacementPolicies** | [**[ServicePlacementPolicyDescription]**](ServicePlacementPolicyDescription.md) | List of service placement policy descriptions. | [optional] 
**serviceTypeName** | **String** | Name of the service type as specified in the service manifest. | [optional] 


