

# ServiceHealthEvaluation

Represents health evaluation for a service, containing information about the data and the algorithm used by health store to evaluate health. The evaluation is returned only when the aggregated health state is either Error or Warning.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**serviceName** | **String** | The full name of the service with &#39;fabric:&#39; URI scheme. |  [optional] |
|**unhealthyEvaluations** | [**List&lt;HealthEvaluationWrapper&gt;**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. |  [optional] |



