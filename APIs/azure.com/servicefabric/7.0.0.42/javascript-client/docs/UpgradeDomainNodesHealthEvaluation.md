# ServiceFabricClientApis.UpgradeDomainNodesHealthEvaluation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxPercentUnhealthyNodes** | **Number** | Maximum allowed percentage of unhealthy nodes from the ClusterHealthPolicy. | [optional] 
**totalCount** | **Number** | Total number of nodes in the current upgrade domain. | [optional] 
**unhealthyEvaluations** | [**[HealthEvaluationWrapper]**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. | [optional] 
**upgradeDomainName** | **String** | Name of the upgrade domain where nodes health is currently evaluated. | [optional] 


