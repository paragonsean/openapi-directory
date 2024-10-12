# ServiceFabricClientApis.ReplicasHealthEvaluation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxPercentUnhealthyReplicasPerPartition** | **Number** | Maximum allowed percentage of unhealthy replicas per partition from the ApplicationHealthPolicy. | [optional] 
**totalCount** | **Number** | Total number of replicas in the partition from the health store. | [optional] 
**unhealthyEvaluations** | [**[HealthEvaluationWrapper]**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. | [optional] 


