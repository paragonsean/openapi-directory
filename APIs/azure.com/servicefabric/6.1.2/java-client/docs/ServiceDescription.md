

# ServiceDescription

A ServiceDescription contains all of the information necessary to create a service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationName** | **String** | The name of the application, including the &#39;fabric:&#39; URI scheme. |  [optional] |
|**correlationScheme** | [**List&lt;ServiceCorrelationDescription&gt;**](ServiceCorrelationDescription.md) | A list that describes the correlation of the service with other services. |  [optional] |
|**defaultMoveCost** | **MoveCost** |  |  [optional] |
|**initializationData** | **List&lt;Integer&gt;** | Array of bytes to be sent as an integer array. Each element of array is a number between 0 and 255. |  [optional] |
|**isDefaultMoveCostSpecified** | **Boolean** | Indicates if the DefaultMoveCost property is specified. |  [optional] |
|**partitionDescription** | [**PartitionSchemeDescription**](PartitionSchemeDescription.md) |  |  |
|**placementConstraints** | **String** | The placement constraints as a string. Placement constraints are boolean expressions on node properties and allow for restricting a service to particular nodes based on the service requirements. For example, to place a service on nodes where NodeType is blue specify the following: \&quot;NodeColor &#x3D;&#x3D; blue)\&quot;. |  [optional] |
|**serviceDnsName** | **String** | The DNS name of the service. It requires the DNS system service to be enabled in Service Fabric cluster. |  [optional] |
|**serviceKind** | **ServiceKind** |  |  |
|**serviceLoadMetrics** | [**List&lt;ServiceLoadMetricDescription&gt;**](ServiceLoadMetricDescription.md) | The service load metrics is given as an array of ServiceLoadMetricDescription objects. |  [optional] |
|**serviceName** | **String** | The full name of the service with &#39;fabric:&#39; URI scheme. |  |
|**servicePackageActivationMode** | **ServicePackageActivationMode** |  |  [optional] |
|**servicePlacementPolicies** | [**List&lt;ServicePlacementPolicyDescription&gt;**](ServicePlacementPolicyDescription.md) | A list that describes the correlation of the service with other services. |  [optional] |
|**serviceTypeName** | **String** | Name of the service type as specified in the service manifest. |  |



