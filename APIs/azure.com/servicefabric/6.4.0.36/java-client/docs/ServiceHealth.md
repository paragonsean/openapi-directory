

# ServiceHealth

Information about the health of a Service Fabric service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The full name of the service with &#39;fabric:&#39; URI scheme. |  [optional] |
|**partitionHealthStates** | [**List&lt;PartitionHealthState&gt;**](PartitionHealthState.md) | The list of partition health states associated with the service. |  [optional] |
|**aggregatedHealthState** | **HealthState** |  |  [optional] |
|**healthEvents** | [**List&lt;HealthEvent&gt;**](HealthEvent.md) | The list of health events reported on the entity. |  [optional] |
|**healthStatistics** | [**HealthStatistics**](HealthStatistics.md) |  |  [optional] |
|**unhealthyEvaluations** | [**List&lt;HealthEvaluationWrapper&gt;**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. |  [optional] |



