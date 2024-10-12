# ServiceFabricClientApis.DeployedApplicationHealth

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployedServicePackageHealthStates** | [**[DeployedServicePackageHealthState]**](DeployedServicePackageHealthState.md) | List of health states for a service package deployed on a Service Fabric node. | [optional] 
**name** | **String** | The name of the application, including the &#39;fabric:&#39; URI scheme. | [optional] 
**nodeName** | **String** | The name of a Service Fabric node. | [optional] 
**aggregatedHealthState** | [**HealthState**](HealthState.md) |  | [optional] 
**healthEvents** | [**[HealthEvent]**](HealthEvent.md) | The list of health events reported on the entity. | [optional] 
**healthStatistics** | [**HealthStatistics**](HealthStatistics.md) |  | [optional] 
**unhealthyEvaluations** | [**[HealthEvaluationWrapper]**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. | [optional] 


