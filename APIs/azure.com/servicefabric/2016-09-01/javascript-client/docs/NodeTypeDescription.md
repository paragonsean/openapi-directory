# ServiceFabricManagementClient.NodeTypeDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationPorts** | [**EndpointRangeDescription**](EndpointRangeDescription.md) |  | [optional] 
**capacities** | **{String: String}** | The capacity tags applied to the nodes in the node type, the cluster resource manager uses these tags to understand how much of a resource a node has | [optional] 
**clientConnectionEndpointPort** | **Number** | The TCP cluster management endpoint port | 
**durabilityLevel** | **String** | Node type durability Level | [optional] 
**ephemeralPorts** | [**EndpointRangeDescription**](EndpointRangeDescription.md) |  | [optional] 
**httpGatewayEndpointPort** | **Number** | The HTTP cluster management endpoint port | 
**isPrimary** | **Boolean** | Mark this as the primary node type | 
**name** | **String** | Name of the node type | 
**placementProperties** | **{String: String}** | The placement tags applied to nodes in the node type, which can be used to indicate where certain services (workload) should run | [optional] 
**reverseProxyEndpointPort** | **Number** | Endpoint used by reverse proxy | [optional] 
**vmInstanceCount** | **Number** | The number of node instances in the node type | 



## Enum: DurabilityLevelEnum


* `Bronze` (value: `"Bronze"`)

* `Silver` (value: `"Silver"`)

* `Gold` (value: `"Gold"`)




