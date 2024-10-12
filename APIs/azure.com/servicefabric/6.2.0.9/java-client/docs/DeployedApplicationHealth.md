

# DeployedApplicationHealth

Information about the health of an application deployed on a Service Fabric node.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregatedHealthState** | **HealthState** |  |  [optional] |
|**healthEvents** | [**List&lt;HealthEvent&gt;**](HealthEvent.md) | The list of health events reported on the entity. |  [optional] |
|**healthStatistics** | [**HealthStatistics**](HealthStatistics.md) |  |  [optional] |
|**unhealthyEvaluations** | [**List&lt;HealthEvaluationWrapper&gt;**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. |  [optional] |
|**deployedServicePackageHealthStates** | [**List&lt;DeployedServicePackageHealthState&gt;**](DeployedServicePackageHealthState.md) | List of health states for a service package deployed on a Service Fabric node. |  [optional] |
|**name** | **String** | The name of the application, including the &#39;fabric:&#39; URI scheme. |  [optional] |
|**nodeName** | **String** | The name of a Service Fabric node. |  [optional] |



