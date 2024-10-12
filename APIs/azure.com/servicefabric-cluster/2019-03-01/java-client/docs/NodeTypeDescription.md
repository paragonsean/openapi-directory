

# NodeTypeDescription

Describes a node type in the cluster, each node type represents sub set of nodes in the cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationPorts** | [**EndpointRangeDescription**](EndpointRangeDescription.md) |  |  [optional] |
|**capacities** | **Map&lt;String, String&gt;** | The capacity tags applied to the nodes in the node type, the cluster resource manager uses these tags to understand how much resource a node has. |  [optional] |
|**clientConnectionEndpointPort** | **Integer** | The TCP cluster management endpoint port. |  |
|**durabilityLevel** | **DurabilityLevel** |  |  [optional] |
|**ephemeralPorts** | [**EndpointRangeDescription**](EndpointRangeDescription.md) |  |  [optional] |
|**httpGatewayEndpointPort** | **Integer** | The HTTP cluster management endpoint port. |  |
|**isPrimary** | **Boolean** | The node type on which system services will run. Only one node type should be marked as primary. Primary node type cannot be deleted or changed for existing clusters. |  |
|**name** | **String** | The name of the node type. |  |
|**placementProperties** | **Map&lt;String, String&gt;** | The placement tags applied to nodes in the node type, which can be used to indicate where certain services (workload) should run. |  [optional] |
|**reverseProxyEndpointPort** | **Integer** | The endpoint used by reverse proxy. |  [optional] |
|**vmInstanceCount** | **Integer** | The number of nodes in the node type. This count should match the capacity property in the corresponding VirtualMachineScaleSet resource. |  |



