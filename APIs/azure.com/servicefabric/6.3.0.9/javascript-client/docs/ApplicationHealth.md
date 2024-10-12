# ServiceFabricClientApis.ApplicationHealth

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregatedHealthState** | [**HealthState**](HealthState.md) |  | [optional] 
**healthEvents** | [**[HealthEvent]**](HealthEvent.md) | The list of health events reported on the entity. | [optional] 
**healthStatistics** | [**HealthStatistics**](HealthStatistics.md) |  | [optional] 
**unhealthyEvaluations** | [**[HealthEvaluationWrapper]**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. | [optional] 
**deployedApplicationHealthStates** | [**[DeployedApplicationHealthState]**](DeployedApplicationHealthState.md) | Deployed application health states as found in the health store. | [optional] 
**name** | **String** | The name of the application, including the &#39;fabric:&#39; URI scheme. | [optional] 
**serviceHealthStates** | [**[ServiceHealthState]**](ServiceHealthState.md) | Service health states as found in the health store. | [optional] 


