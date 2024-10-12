

# EndpointHealthData

The health data for an endpoint

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endpointId** | **String** | Id of the endpoint |  [optional] |
|**healthStatus** | [**HealthStatusEnum**](#HealthStatusEnum) | Health statuses have following meanings. The &#39;healthy&#39; status shows that the endpoint is accepting messages as expected. The &#39;unhealthy&#39; status shows that the endpoint is not accepting messages as expected and IoT Hub is retrying to send data to this endpoint. The status of an unhealthy endpoint will be updated to healthy when IoT Hub has established an eventually consistent state of health. The &#39;dead&#39; status shows that the endpoint is not accepting messages, after IoT Hub retried sending messages for the retrial period. See IoT Hub metrics to identify errors and monitor issues with endpoints. The &#39;unknown&#39; status shows that the IoT Hub has not established a connection with the endpoint. No messages have been delivered to or rejected from this endpoint |  [optional] |



## Enum: HealthStatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| HEALTHY | &quot;healthy&quot; |
| UNHEALTHY | &quot;unhealthy&quot; |
| DEAD | &quot;dead&quot; |



