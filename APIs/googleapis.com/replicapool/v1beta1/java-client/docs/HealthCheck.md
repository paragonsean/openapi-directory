

# HealthCheck


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checkIntervalSec** | **Integer** | How often (in seconds) to make HTTP requests for this healthcheck. The default value is 5 seconds. |  [optional] |
|**description** | **String** | The description for this health check. |  [optional] |
|**healthyThreshold** | **Integer** | The number of consecutive health check requests that need to succeed before the replica is considered healthy again. The default value is 2. |  [optional] |
|**host** | **String** | The value of the host header in the HTTP health check request. If left empty (default value), the localhost IP 127.0.0.1 will be used. |  [optional] |
|**name** | **String** | The name of this health check. |  [optional] |
|**path** | **String** | The localhost request path to send this health check, in the format /path/to/use. For example, /healthcheck. |  [optional] |
|**port** | **Integer** | The TCP port for the health check requests. |  [optional] |
|**timeoutSec** | **Integer** | How long (in seconds) to wait before a timeout failure for this healthcheck. The default value is 5 seconds. |  [optional] |
|**unhealthyThreshold** | **Integer** | The number of consecutive health check requests that need to fail in order to consider the replica unhealthy. The default value is 2. |  [optional] |



