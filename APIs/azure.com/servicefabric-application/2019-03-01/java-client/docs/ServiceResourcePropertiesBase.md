

# ServiceResourcePropertiesBase

The common service resource properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**correlationScheme** | [**List&lt;ServiceCorrelationDescription&gt;**](ServiceCorrelationDescription.md) | A list that describes the correlation of the service with other services. |  [optional] |
|**defaultMoveCost** | **MoveCost** |  |  [optional] |
|**placementConstraints** | **String** | The placement constraints as a string. Placement constraints are boolean expressions on node properties and allow for restricting a service to particular nodes based on the service requirements. For example, to place a service on nodes where NodeType is blue specify the following: \&quot;NodeColor &#x3D;&#x3D; blue)\&quot;. |  [optional] |
|**serviceLoadMetrics** | [**List&lt;ServiceLoadMetricDescription&gt;**](ServiceLoadMetricDescription.md) | The service load metrics is given as an array of ServiceLoadMetricDescription objects. |  [optional] |
|**servicePlacementPolicies** | [**List&lt;ServicePlacementPolicyDescription&gt;**](ServicePlacementPolicyDescription.md) | A list that describes the correlation of the service with other services. |  [optional] |



