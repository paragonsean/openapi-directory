# ServiceFabricClientApis.UpgradeDomainDeltaNodesCheckHealthEvaluation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baselineErrorCount** | **Number** | Number of upgrade domain nodes with aggregated heath state Error in the health store at the beginning of the cluster upgrade. | [optional] 
**baselineTotalCount** | **Number** | Total number of upgrade domain nodes in the health store at the beginning of the cluster upgrade. | [optional] 
**maxPercentDeltaUnhealthyNodes** | **Number** | Maximum allowed percentage of upgrade domain delta unhealthy nodes from the ClusterUpgradeHealthPolicy. | [optional] 
**totalCount** | **Number** | Total number of upgrade domain nodes in the health store. | [optional] 
**unhealthyEvaluations** | [**[HealthEvaluationWrapper]**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. | [optional] 
**upgradeDomainName** | **String** | Name of the upgrade domain where nodes health is currently evaluated. | [optional] 


