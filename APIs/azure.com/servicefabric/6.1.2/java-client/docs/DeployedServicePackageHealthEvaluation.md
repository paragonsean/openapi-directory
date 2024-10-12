

# DeployedServicePackageHealthEvaluation

Represents health evaluation for a deployed service package, containing information about the data and the algorithm used by health store to evaluate health. The evaluation is returned only when the aggregated health state is either Error or Warning.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationName** | **String** | The name of the application, including the &#39;fabric:&#39; URI scheme. |  [optional] |
|**nodeName** | **String** | The name of a Service Fabric node. |  [optional] |
|**serviceManifestName** | **String** | The name of the service manifest. |  [optional] |
|**unhealthyEvaluations** | [**List&lt;HealthEvaluationWrapper&gt;**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. |  [optional] |



