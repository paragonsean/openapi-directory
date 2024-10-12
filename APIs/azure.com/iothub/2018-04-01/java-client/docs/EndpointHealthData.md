

# EndpointHealthData

The health data for an endpoint

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endpointId** | **String** | Id of the endpoint |  [optional] |
|**healthStatus** | [**HealthStatusEnum**](#HealthStatusEnum) | The health status code of the endpoint |  [optional] |



## Enum: HealthStatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| HEALTHY | &quot;healthy&quot; |
| UNHEALTHY | &quot;unhealthy&quot; |
| DEAD | &quot;dead&quot; |



