# ServiceFabricClientApis.DeployedServicePackageHealthEvaluation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationName** | **String** | The name of the application, including the &#39;fabric:&#39; URI scheme. | [optional] 
**nodeName** | **String** | The name of a Service Fabric node. | [optional] 
**serviceManifestName** | **String** | The name of the service manifest. | [optional] 
**unhealthyEvaluations** | [**[HealthEvaluationWrapper]**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. | [optional] 


