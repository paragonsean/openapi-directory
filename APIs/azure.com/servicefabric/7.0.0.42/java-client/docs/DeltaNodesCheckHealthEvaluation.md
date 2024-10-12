

# DeltaNodesCheckHealthEvaluation

Represents health evaluation for delta nodes, containing health evaluations for each unhealthy node that impacted current aggregated health state. Can be returned during cluster upgrade when the aggregated health state of the cluster is Warning or Error.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**baselineErrorCount** | **Long** | Number of nodes with aggregated heath state Error in the health store at the beginning of the cluster upgrade. |  [optional] |
|**baselineTotalCount** | **Long** | Total number of nodes in the health store at the beginning of the cluster upgrade. |  [optional] |
|**maxPercentDeltaUnhealthyNodes** | **Integer** | Maximum allowed percentage of delta unhealthy nodes from the ClusterUpgradeHealthPolicy. |  [optional] |
|**totalCount** | **Long** | Total number of nodes in the health store. |  [optional] |
|**unhealthyEvaluations** | [**List&lt;HealthEvaluationWrapper&gt;**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. |  [optional] |



