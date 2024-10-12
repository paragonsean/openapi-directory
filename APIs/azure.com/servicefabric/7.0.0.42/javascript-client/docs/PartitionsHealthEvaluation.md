# ServiceFabricClientApis.PartitionsHealthEvaluation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxPercentUnhealthyPartitionsPerService** | **Number** | Maximum allowed percentage of unhealthy partitions per service from the ServiceTypeHealthPolicy. | [optional] 
**totalCount** | **Number** | Total number of partitions of the service from the health store. | [optional] 
**unhealthyEvaluations** | [**[HealthEvaluationWrapper]**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. | [optional] 


