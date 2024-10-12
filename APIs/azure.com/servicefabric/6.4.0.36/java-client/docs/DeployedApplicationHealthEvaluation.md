

# DeployedApplicationHealthEvaluation

Represents health evaluation for a deployed application, containing information about the data and the algorithm used by the health store to evaluate health.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationName** | **String** | The name of the application, including the &#39;fabric:&#39; URI scheme. |  [optional] |
|**nodeName** | **String** | The name of a Service Fabric node. |  [optional] |
|**unhealthyEvaluations** | [**List&lt;HealthEvaluationWrapper&gt;**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. |  [optional] |



