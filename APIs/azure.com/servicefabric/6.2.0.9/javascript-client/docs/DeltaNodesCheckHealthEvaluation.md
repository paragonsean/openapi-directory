# ServiceFabricClientApis.DeltaNodesCheckHealthEvaluation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baselineErrorCount** | **Number** | Number of nodes with aggregated heath state Error in the health store at the beginning of the cluster upgrade. | [optional] 
**baselineTotalCount** | **Number** | Total number of nodes in the health store at the beginning of the cluster upgrade. | [optional] 
**maxPercentDeltaUnhealthyNodes** | **Number** | Maximum allowed percentage of delta unhealthy nodes from the ClusterUpgradeHealthPolicy. | [optional] 
**totalCount** | **Number** | Total number of nodes in the health store. | [optional] 
**unhealthyEvaluations** | [**[HealthEvaluationWrapper]**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. | [optional] 


