

# EndpointDetail

Current TCP connectivity information from the App Service Environment to a single endpoint.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ipAddress** | **String** | An IP Address that Domain Name currently resolves to. |  [optional] |
|**isAccessible** | **Boolean** | Whether it is possible to create a TCP connection from the App Service Environment to this IpAddress at this Port. |  [optional] |
|**latency** | **Double** | The time in milliseconds it takes for a TCP connection to be created from the App Service Environment to this IpAddress at this Port. |  [optional] |
|**port** | **Integer** | The port an endpoint is connected to. |  [optional] |



