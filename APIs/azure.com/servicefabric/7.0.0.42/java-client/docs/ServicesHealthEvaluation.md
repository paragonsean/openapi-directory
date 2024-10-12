

# ServicesHealthEvaluation

Represents health evaluation for services of a certain service type belonging to an application, containing health evaluations for each unhealthy service that impacted current aggregated health state. Can be returned when evaluating application health and the aggregated health state is either Error or Warning.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxPercentUnhealthyServices** | **Integer** | Maximum allowed percentage of unhealthy services from the ServiceTypeHealthPolicy. |  [optional] |
|**serviceTypeName** | **String** | Name of the service type of the services. |  [optional] |
|**totalCount** | **Long** | Total number of services of the current service type in the application from the health store. |  [optional] |
|**unhealthyEvaluations** | [**List&lt;HealthEvaluationWrapper&gt;**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. |  [optional] |



