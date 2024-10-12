# ServiceFabricClientApis.NodeLoadMetricInformation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bufferedNodeCapacityRemaining** | **Number** | The remaining capacity which is not reserved by NodeBufferPercentage for this metric on the node. | [optional] 
**currentNodeLoad** | **Number** | Current load on the node for this metric. | [optional] 
**isCapacityViolation** | **Boolean** | Indicates if there is a capacity violation for this metric on the node. | [optional] 
**name** | **String** | Name of the metric for which this load information is provided. | [optional] 
**nodeBufferedCapacity** | **String** | The value that indicates the reserved capacity for this metric on the node. | [optional] 
**nodeCapacity** | **String** | Total capacity on the node for this metric. | [optional] 
**nodeCapacityRemaining** | **Number** | The remaining capacity on the node for the metric. | [optional] 
**nodeLoad** | **String** | Current load on the node for this metric. In future releases of Service Fabric this parameter will be deprecated in favor of CurrentNodeLoad. | [optional] 
**nodeRemainingBufferedCapacity** | **String** | The remaining reserved capacity for this metric on the node. In future releases of Service Fabric this parameter will be deprecated in favor of BufferedNodeCapacityRemaining. | [optional] 
**nodeRemainingCapacity** | **String** | The remaining capacity on the node for this metric. In future releases of Service Fabric this parameter will be deprecated in favor of NodeCapacityRemaining. | [optional] 
**plannedNodeLoadRemoval** | **Number** | This value represents the load of the replicas that are planned to be removed in the future. This kind of load is reported for replicas that are currently being moving to other nodes and for replicas that are currently being dropped but still use the load on the source node. | [optional] 


