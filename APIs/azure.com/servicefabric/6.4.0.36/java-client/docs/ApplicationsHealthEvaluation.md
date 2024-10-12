

# ApplicationsHealthEvaluation

Represents health evaluation for applications, containing health evaluations for each unhealthy application that impacted current aggregated health state.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxPercentUnhealthyApplications** | **Integer** | Maximum allowed percentage of unhealthy applications from the ClusterHealthPolicy. |  [optional] |
|**totalCount** | **Long** | Total number of applications from the health store. |  [optional] |
|**unhealthyEvaluations** | [**List&lt;HealthEvaluationWrapper&gt;**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. |  [optional] |



