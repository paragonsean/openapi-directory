

# ApplicationHealth

Represents the health of the application. Contains the application aggregated health state and the service and deployed application health states.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deployedApplicationHealthStates** | [**List&lt;DeployedApplicationHealthState&gt;**](DeployedApplicationHealthState.md) | Deployed application health states as found in the health store. |  [optional] |
|**name** | **String** | The name of the application, including the &#39;fabric:&#39; URI scheme. |  [optional] |
|**serviceHealthStates** | [**List&lt;ServiceHealthState&gt;**](ServiceHealthState.md) | Service health states as found in the health store. |  [optional] |
|**aggregatedHealthState** | **HealthState** |  |  [optional] |
|**healthEvents** | [**List&lt;HealthEvent&gt;**](HealthEvent.md) | The list of health events reported on the entity. |  [optional] |
|**healthStatistics** | [**HealthStatistics**](HealthStatistics.md) |  |  [optional] |
|**unhealthyEvaluations** | [**List&lt;HealthEvaluationWrapper&gt;**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. |  [optional] |



