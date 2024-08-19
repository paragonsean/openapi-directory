# ServiceFabricManagementClient.ServiceResourceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partitionDescription** | [**PartitionSchemeDescription**](PartitionSchemeDescription.md) |  | [optional] 
**provisioningState** | **String** | The current deployment or provisioning state, which only appears in the response | [optional] [readonly] 
**serviceKind** | [**ServiceKind**](ServiceKind.md) |  | 
**servicePackageActivationMode** | **String** | The activation Mode of the service package | [optional] 
**serviceTypeName** | **String** | The name of the service type | [optional] 
**correlationScheme** | [**[ServiceCorrelationDescription]**](ServiceCorrelationDescription.md) | A list that describes the correlation of the service with other services. | [optional] 
**defaultMoveCost** | [**MoveCost**](MoveCost.md) |  | [optional] 
**placementConstraints** | **String** | The placement constraints as a string. Placement constraints are boolean expressions on node properties and allow for restricting a service to particular nodes based on the service requirements. For example, to place a service on nodes where NodeType is blue specify the following: \&quot;NodeColor &#x3D;&#x3D; blue)\&quot;. | [optional] 
**serviceLoadMetrics** | [**[ServiceLoadMetricDescription]**](ServiceLoadMetricDescription.md) | The service load metrics is given as an array of ServiceLoadMetricDescription objects. | [optional] 
**servicePlacementPolicies** | [**[ServicePlacementPolicyDescription]**](ServicePlacementPolicyDescription.md) | A list that describes the correlation of the service with other services. | [optional] 



## Enum: ServicePackageActivationModeEnum


* `SharedProcess` (value: `"SharedProcess"`)

* `ExclusiveProcess` (value: `"ExclusiveProcess"`)




