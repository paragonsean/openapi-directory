# ServiceFabricClientApis.LoadMetricInformation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | The current action being taken with regard to this metric | [optional] 
**activityThreshold** | **Number** | The Activity Threshold specified for this metric in the system Cluster Manifest. | [optional] 
**balancingThreshold** | **Number** | The balancing threshold for a certain metric. | [optional] 
**bufferedClusterCapacityRemaining** | **Number** | Remaining capacity in the cluster excluding the reserved space. | [optional] 
**clusterBufferedCapacity** | **String** | Remaining capacity in the cluster excluding the reserved space. In future releases of Service Fabric this parameter will be deprecated in favor of BufferedClusterCapacityRemaining. | [optional] 
**clusterCapacity** | **String** | The total cluster capacity for a given metric | [optional] 
**clusterCapacityRemaining** | **String** | The remaining capacity for the metric in the cluster. | [optional] 
**clusterLoad** | **String** | The total cluster load. In future releases of Service Fabric this parameter will be deprecated in favor of CurrentClusterLoad. | [optional] 
**clusterRemainingBufferedCapacity** | **String** | The remaining percentage of cluster total capacity for this metric. | [optional] 
**clusterRemainingCapacity** | **String** | The remaining capacity for the metric in the cluster. In future releases of Service Fabric this parameter will be deprecated in favor of ClusterCapacityRemaining. | [optional] 
**currentClusterLoad** | **Number** | The total cluster load. | [optional] 
**deviationAfter** | **Number** | The standard average deviation of the metrics after resource balancer run. | [optional] 
**deviationBefore** | **Number** | The standard average deviation of the metrics before resource balancer run. | [optional] 
**isBalancedAfter** | **Boolean** | Value that indicates whether the metrics is balanced or not after resource balancer run. | [optional] 
**isBalancedBefore** | **Boolean** | Value that indicates whether the metrics is balanced or not before resource balancer run | [optional] 
**isClusterCapacityViolation** | **Boolean** | Indicates that the metric is currently over capacity in the cluster. | [optional] 
**maxNodeLoadNodeId** | [**NodeId**](NodeId.md) |  | [optional] 
**maxNodeLoadValue** | **String** | The maximum load on any node for this metric. In future releases of Service Fabric this parameter will be deprecated in favor of MaximumNodeLoad. | [optional] 
**maximumNodeLoad** | **Number** | The maximum load on any node for this metric. | [optional] 
**minNodeLoadNodeId** | [**NodeId**](NodeId.md) |  | [optional] 
**minNodeLoadValue** | **String** | The minimum load on any node for this metric. In future releases of Service Fabric this parameter will be deprecated in favor of MinimumNodeLoad. | [optional] 
**minimumNodeLoad** | **Number** | The minimum load on any node for this metric. | [optional] 
**name** | **String** | Name of the metric for which this load information is provided. | [optional] 
**nodeBufferPercentage** | **Number** | The reserved percentage of total node capacity for this metric. | [optional] 
**plannedLoadRemoval** | **Number** | This value represents the load of the replicas that are planned to be removed in the future within the cluster. This kind of load is reported for replicas that are currently being moving to other nodes and for replicas that are currently being dropped but still use the load on the source node. | [optional] 


