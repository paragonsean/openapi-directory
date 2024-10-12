

# DeployedApplicationsHealthEvaluation

Represents health evaluation for deployed applications, containing health evaluations for each unhealthy deployed application that impacted current aggregated health state. Can be returned when evaluating application health and the aggregated health state is either Error or Warning.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxPercentUnhealthyDeployedApplications** | **Integer** | Maximum allowed percentage of unhealthy deployed applications from the ApplicationHealthPolicy. |  [optional] |
|**totalCount** | **Long** | Total number of deployed applications of the application in the health store. |  [optional] |
|**unhealthyEvaluations** | [**List&lt;HealthEvaluationWrapper&gt;**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. |  [optional] |



