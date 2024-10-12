

# PartitionsHealthEvaluation

Represents health evaluation for the partitions of a service, containing health evaluations for each unhealthy partition that impacts current aggregated health state. Can be returned when evaluating service health and the aggregated health state is either Error or Warning.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxPercentUnhealthyPartitionsPerService** | **Integer** | Maximum allowed percentage of unhealthy partitions per service from the ServiceTypeHealthPolicy. |  [optional] |
|**totalCount** | **Long** | Total number of partitions of the service from the health store. |  [optional] |
|**unhealthyEvaluations** | [**List&lt;HealthEvaluationWrapper&gt;**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. |  [optional] |



