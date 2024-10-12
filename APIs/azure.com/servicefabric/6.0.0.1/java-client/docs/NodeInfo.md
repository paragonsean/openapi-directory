

# NodeInfo

Information about a node in Service Fabric cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**codeVersion** | **String** | The version of Service Fabric binaries that the node is running. |  [optional] |
|**configVersion** | **String** | The version of Service Fabric cluster manifest that the node is using. |  [optional] |
|**faultDomain** | **String** | The fault domain of the node. |  [optional] |
|**healthState** | **HealthState** |  |  [optional] |
|**id** | [**NodeId**](NodeId.md) |  |  [optional] |
|**instanceId** | **String** | The id representing the node instance. While the Id of the node is deterministically generated from the node name and remains same across restarts, the InstanceId changes every time node restarts. |  [optional] |
|**ipAddressOrFQDN** | **String** | The IP address or fully qualified domain name of the node. |  [optional] |
|**isSeedNode** | **Boolean** | Indicates if the node is a seed node or not. Returns true if the node is a seed node, otherwise false. A quorum of seed nodes are required for proper operation of Service Fabric cluster. |  [optional] |
|**isStopped** | **Boolean** | Indicates if the node is stopped by calling stop node API or not. Returns true if the node is stopped, otherwise false. |  [optional] |
|**name** | **String** | The name of a Service Fabric node. |  [optional] |
|**nodeDeactivationInfo** | [**NodeDeactivationInfo**](NodeDeactivationInfo.md) |  |  [optional] |
|**nodeDownAt** | **OffsetDateTime** | Date time in UTC when the node went down. If node has never been down then this value will be zero date time. |  [optional] |
|**nodeDownTimeInSeconds** | **String** | Time in seconds since the node has been in NodeStatus Down. Value zero indicates node is not NodeStatus Down. |  [optional] |
|**nodeStatus** | **NodeStatus** |  |  [optional] |
|**nodeUpAt** | **OffsetDateTime** | Date time in UTC when the node came up. If the node has never been up then this value will be zero date time. |  [optional] |
|**nodeUpTimeInSeconds** | **String** | Time in seconds since the node has been in NodeStatus Up. Value ero indicates that the node is not Up. |  [optional] |
|**type** | **String** | The type of the node. |  [optional] |
|**upgradeDomain** | **String** | The upgrade domain of the node. |  [optional] |



