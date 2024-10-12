# ServiceFabricManagementClient.NodeTypeDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationPorts** | [**EndpointRangeDescription**](EndpointRangeDescription.md) |  | [optional] 
**capacities** | **{String: String}** | The capacity tags applied to the nodes in the node type, the cluster resource manager uses these tags to understand how much resource a node has. | [optional] 
**clientConnectionEndpointPort** | **Number** | The TCP cluster management endpoint port. | 
**durabilityLevel** | [**DurabilityLevel**](DurabilityLevel.md) |  | [optional] 
**ephemeralPorts** | [**EndpointRangeDescription**](EndpointRangeDescription.md) |  | [optional] 
**httpGatewayEndpointPort** | **Number** | The HTTP cluster management endpoint port. | 
**isPrimary** | **Boolean** | The node type on which system services will run. Only one node type should be marked as primary. Primary node type cannot be deleted or changed for existing clusters. | 
**name** | **String** | The name of the node type. | 
**placementProperties** | **{String: String}** | The placement tags applied to nodes in the node type, which can be used to indicate where certain services (workload) should run. | [optional] 
**reverseProxyEndpointPort** | **Number** | The endpoint used by reverse proxy. | [optional] 
**vmInstanceCount** | **Number** | The number of nodes in the node type. This count should match the capacity property in the corresponding VirtualMachineScaleSet resource. | 


