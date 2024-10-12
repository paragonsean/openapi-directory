

# NodeTypeDescription

Describes a node type in the cluster, each node type represents sub set of nodes in the cluster

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationPorts** | [**EndpointRangeDescription**](EndpointRangeDescription.md) |  |  [optional] |
|**capacities** | **Map&lt;String, String&gt;** | The capacity tags applied to the nodes in the node type, the cluster resource manager uses these tags to understand how much of a resource a node has |  [optional] |
|**clientConnectionEndpointPort** | **Integer** | The TCP cluster management endpoint port |  |
|**durabilityLevel** | [**DurabilityLevelEnum**](#DurabilityLevelEnum) | Node type durability Level |  [optional] |
|**ephemeralPorts** | [**EndpointRangeDescription**](EndpointRangeDescription.md) |  |  [optional] |
|**httpGatewayEndpointPort** | **Integer** | The HTTP cluster management endpoint port |  |
|**isPrimary** | **Boolean** | Mark this as the primary node type |  |
|**name** | **String** | Name of the node type |  |
|**placementProperties** | **Map&lt;String, String&gt;** | The placement tags applied to nodes in the node type, which can be used to indicate where certain services (workload) should run |  [optional] |
|**reverseProxyEndpointPort** | **Integer** | Endpoint used by reverse proxy |  [optional] |
|**vmInstanceCount** | **Integer** | The number of node instances in the node type |  |



## Enum: DurabilityLevelEnum

| Name | Value |
|---- | -----|
| BRONZE | &quot;Bronze&quot; |
| SILVER | &quot;Silver&quot; |
| GOLD | &quot;Gold&quot; |



