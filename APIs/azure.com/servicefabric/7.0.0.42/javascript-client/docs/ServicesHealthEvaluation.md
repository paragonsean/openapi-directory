# ServiceFabricClientApis.ServicesHealthEvaluation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxPercentUnhealthyServices** | **Number** | Maximum allowed percentage of unhealthy services from the ServiceTypeHealthPolicy. | [optional] 
**serviceTypeName** | **String** | Name of the service type of the services. | [optional] 
**totalCount** | **Number** | Total number of services of the current service type in the application from the health store. | [optional] 
**unhealthyEvaluations** | [**[HealthEvaluationWrapper]**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. | [optional] 


